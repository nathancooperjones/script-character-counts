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
                                      remove_first_line=False,
                                      debug=False):
    """
    Return all character's dialogue for a film script.

    Parameters
    ---------------
    pdf: pdftotext.PDF
    remove_first_line: bool
        Remove the first line of every page, useful for when scripts have a set header
        (default False)
    debug: bool
        Print each page of the script as well as character dialogue collected for that page
        (default False)

    Returns
    ---------------
    words_spoken: dict
        Dictionary with each key being a character's name and the value being a list of all lines of
        dialogue.

    """
    words_spoken = defaultdict(list)

    for page_number in tqdm(range(len(pdf))) if debug is False else range(len(pdf)):
        page = pdf[page_number]

        page_lines = page.split('\n')
        if remove_first_line:
            page_lines = page_lines[1:]

        words_spoken = _get_character_dialogue_for_page_lines(
            page_lines=page_lines,
            words_spoken=words_spoken,
        )

        if debug:
            words_spoken_for_page = _get_character_dialogue_for_page_lines(
                page_lines=page_lines,
                words_spoken=defaultdict(list),
            )

            print('PAGE TEXT:\n{}'.format(page))
            print('DICTIONARY COLLECTED:\n{}'.format(dict(words_spoken_for_page)))
            print('\n\n---------\n\n')

    return dict(words_spoken)


def _get_character_dialogue_for_page_lines(page_lines,
                                           words_spoken):
    # ASSUMPTION: Dialogue never continues to a new page without character name again on that page.
    # ASSUMPTION: Character names always have at least one space before they speak.
    # ASSUMPTION: All character names and all dialogue have the same number of spaces before each
    #             line.
    # ASSUMPTION: Character names never have "EXT.", "INT.", "TO:", or "SFX:" in the name.
    # ASSUMPTION: Valid character names are in all-caps.
    # ASSUMPTION: Any dialogue occurring within parentheses should not be counted.
    currently_speaking = None
    open_bracket = False
    number_of_spaces_for_dialogue = None
    number_of_spaces_for_character = None
    for idx in range(len(page_lines)):
        line = page_lines[idx]

        should_we_continue, currently_speaking = _initial_line_checks(line, currently_speaking)
        if should_we_continue:
            continue

        potential_name = _prep_potential_name(line)
        spaces_before_line = _get_spaces_before_line(line)
        if (
            potential_name.isupper()
            and spaces_before_line != 0
            and (number_of_spaces_for_character is None
                 or spaces_before_line == number_of_spaces_for_character
                 )
        ):
            if _check_if_potential_name(potential_name):
                if (
                    number_of_spaces_for_character is None
                    and not line.isspace()
                ):
                    number_of_spaces_for_character = spaces_before_line
                currently_speaking = potential_name
            else:
                currently_speaking = None
        else:
            # assume this is dialogue
            line, open_bracket = _handle_parentheses(line, open_bracket)

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
