import itertools
from pathlib import Path
import re
from typing import Dict, List, Tuple, Union

import Levenshtein
import nltk
from nltk.tokenize import sent_tokenize
import pdftotext


def open_pdf(path: Union[str, Path]) -> pdftotext.PDF:
    """
    Open a PDF file for analysis.

    Parameters
    ---------------
    path: Path or str
        Path to PDF file.

    Returns
    ---------------
    pdf: pdftotext.PDF

    """
    with open(str(path), 'rb') as f:
        return pdftotext.PDF(f)


def word_and_sentence_count(single_characters_dialogue: List[str]) -> Tuple[int, int]:
    """
    Compute word and sentence count for a character's dialogue.

    Parameters
    ---------------
    single_characters_dialogue: list of str

    Returns
    ---------------
    word_count: int
    sentence_count: int

    """
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')

    pattern = re.compile('[\W]', re.IGNORECASE | re.UNICODE)

    single_characters_dialogue = ' '.join(single_characters_dialogue)

    # bug fix: duplicated punctuation is counted as separate lines - remove this
    previous_single_characters_dialogue_length = -1
    while previous_single_characters_dialogue_length != len(single_characters_dialogue):
        previous_single_characters_dialogue_length = len(single_characters_dialogue)
        single_characters_dialogue = single_characters_dialogue.replace('!!', '!')
        single_characters_dialogue = single_characters_dialogue.replace('??', '?')
        single_characters_dialogue = single_characters_dialogue.replace('!?', '!')
        single_characters_dialogue = single_characters_dialogue.replace('?!', '?')

    words = single_characters_dialogue.split(' ')

    word_list = list()
    for word in words:
        word = pattern.sub('', word).lower()

        if word and not word.isspace():
            word_list.append(word)

    sentence_list = sent_tokenize(single_characters_dialogue)

    return len(word_list), len(sentence_list)


def combine_similar_names(words_spoken_dict: Dict[str, List[str]],
                          max_levenshtein_distance: int = 2,
                          interactive: bool = False,
                          verbose: bool = True) -> Dict[str, List[str]]:
    """
    Combine similar names in `words_spoken_dict` with low Levenshtein distances. This function
    handles scripts with occassional typos in a character's name by combining the character with
    the least lines in with the character with the most lines if the Levenshtein distance between
    the two is low.

    Parameters
    ---------------
    words_spoken_dict: dict
        Dictionary with each key being a character's name and the value being a list of all lines of
        dialogue, output of `script_scraper`
    max_levenshtein_distance: int
        Max edit distance allowed between two names to combine (default 2)
    interactive: bool
        Prompt for input before combining names (default False)
    verbose: bool
        Print after each name combination (default True)

    Returns
    ---------------
    words_spoken_combined_dict: dict
        `words_spoken_dict` with similar names combined

    """
    words_spoken = words_spoken_dict.copy()
    all_name_pairs = list(itertools.combinations(words_spoken.keys(), 2))

    for (name_1, name_2) in all_name_pairs:
        if (
            Levenshtein.distance(name_1, name_2) < max_levenshtein_distance
            and name_1 in words_spoken
            and name_2 in words_spoken
        ):
            most_lines_name, least_lines_name = (
                (name_1, name_2)
                if len(words_spoken[name_1]) > len(words_spoken[name_2])
                else (name_2, name_1)
            )

            if interactive:
                prompt = f'Combine lines spoken from {least_lines_name} into {most_lines_name}?'

                while True:
                    reply = str(input(prompt + ' (y/n): ')).lower().strip()
                    if reply.lower().startswith('y') or reply.lower().startswith('n'):
                        break
                    else:
                        print(f'{reply} reply not valid. Try again.')

                if reply.lower().startswith('n'):
                    print('Skipping...')
                    continue

            if interactive or verbose:
                print(f'Combining lines spoken from {least_lines_name} into {most_lines_name}.')

            words_spoken[most_lines_name] += words_spoken.pop(least_lines_name)

    return words_spoken
