from collections import defaultdict
import re

import nltk
from nltk.tokenize import sent_tokenize
import pdftotext
from tqdm import tqdm


def open_pdf(path):
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


def get_character_dialogue_for_script(pdf,
                                      non_dialogue_sentence=None,
                                      remove_first_line=True):
    """
    Return all character's dialogue for a film script.

    Parameters
    ---------------
    pdf: pdftotext.PDF
    non_dialogue_sentence: str
        A sentence of the script that is not dialogue. This is used for calculating the number of
        spaces that start an average sentence in the script (default None)
    remove_first_line: bool
        Remove the first line of every page, useful for when scripts have a set header
        (default True)

    Returns
    ---------------
    words_spoken: dict
        Dictionary with each key being a character's name and the value being a list of all lines of
        dialogue.

    """
    words_spoken = defaultdict(list)

    number_of_spaces_for_script = _get_spaces_before_line(non_dialogue_sentence)

    for page_number in tqdm(range(len(pdf))):
        page = pdf[page_number]

        page_lines = page.split('\n')
        if remove_first_line:
            page_lines = page_lines[1:]

        words_spoken = _get_character_dialogue_for_page_lines(
            page_lines=page_lines,
            words_spoken=words_spoken,
            number_of_spaces_for_script=number_of_spaces_for_script,
        )

    return dict(words_spoken)


def _get_character_dialogue_for_page_lines(page_lines,
                                           words_spoken,
                                           number_of_spaces_for_script):
    # ASSUMPTION: Dialogue never continues to a new page without character name again on that page.
    currently_speaking = None

    # First thing we need to do is check if there is any non-dialogue / character lines.
    all_dialogue = None
    open_bracket = False

    for idx in range(len(page_lines)):
        line = page_lines[idx]

        should_we_continue, currently_speaking = _initial_line_checks(line, currently_speaking)
        if should_we_continue:
            continue

        if re.match(r'\S', line):
            continue

        potential_name = _prep_potential_name(line)
        if potential_name.isupper() and _check_if_potential_name(potential_name):
            while all_dialogue is None and idx < len(page_lines) - 1:
                next_line = page_lines[idx + 1]
                # assume this is dialogue
                next_line, open_bracket = _handle_parentheses(next_line, open_bracket)

                if all_dialogue is None and len(next_line) > 0 and open_bracket is False:
                    all_dialogue = bool(re.match(r'\S', next_line))
                    break

                idx += 1
        else:
            # assume this is dialogue
            line, open_bracket = _handle_parentheses(line, open_bracket)

            if (
                all_dialogue is None
                and re.match(r'\s', line)
                and len(line) > 0
                and open_bracket is False
            ):
                all_dialogue = False

    # Main character counting loop.
    open_bracket = False
    number_of_spaces_for_dialogue = None
    for idx in range(len(page_lines)):
        line = page_lines[idx]

        # if all_dialogue is False:
        #     line = line[number_of_spaces_for_script:]

        should_we_continue, currently_speaking = _initial_line_checks(line, currently_speaking)
        if should_we_continue:
            continue

        potential_name = _prep_potential_name(line)
        if potential_name.isupper():
            if _check_if_potential_name(potential_name):
                currently_speaking = potential_name
            else:
                currently_speaking = None
        else:
            # assume this is dialogue
            line, open_bracket = _handle_parentheses(line, open_bracket)

            spaces_before_line = _get_spaces_before_line(line)

            if (
                currently_speaking is not None
                and number_of_spaces_for_dialogue is None
                and not line.isspace()
            ):
                number_of_spaces_for_dialogue = spaces_before_line

            if (
                spaces_before_line == number_of_spaces_for_dialogue
                and currently_speaking is not None
                and open_bracket is False
            ):
                line = line.strip()
                if len(line) > 0:
                    words_spoken[currently_speaking].append(line)

    return words_spoken


def _prep_potential_name(line):
    return _remove_everything_between_parentheses(line).replace('*', '').strip()


def _check_if_potential_name(potential_name):
    return (
        'EXT.' not in potential_name
        and 'INT.' not in potential_name
        and 'TO:' not in potential_name
        and 'SFX:' not in potential_name
    )


def _initial_line_checks(line, currently_speaking):
    we_should_continue = False

    if len(line) == 0:
        currently_speaking = None
        we_should_continue = True

    return we_should_continue, currently_speaking


def _handle_parentheses(line, open_bracket):
    line = _remove_everything_between_parentheses(line)
    if '(' in line:
        open_bracket = True
    if ')' in line:
        line = line.split(')', 1)[-1]
        open_bracket = False

    return line, open_bracket


def _remove_everything_between_parentheses(line):
    return re.sub('\([^\)]+\)', '', line)


def _get_spaces_before_line(line):
    return len(line) - len(line.lstrip(' ')) if line else 0


def word_and_sentence_count(single_characters_dialogue):
    """
    Open a PDF file for analysis.

    Parameters
    ---------------
    single_characters_dialogue: List of dialogue

    Returns
    ---------------
    word_count: int
    sentence_count: int

    """
    nltk.download('punkt')

    # TODO: sentence count needs to be better
    pattern = re.compile('[\W]', re.IGNORECASE | re.UNICODE)

    single_characters_dialogue = ' '.join(single_characters_dialogue)
    words = single_characters_dialogue.split()

    word_list = list()
    for word in words:
        word = pattern.sub('', word).lower()

        if word and not word.isspace():
            word_list.append(word)

    sentence_list = sent_tokenize(single_characters_dialogue)

    return len(word_list), len(sentence_list)
