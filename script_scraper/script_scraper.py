from collections import defaultdict
import re
from typing import List, Union

from pdftotext import PDF
from tqdm import tqdm

from script_scraper.utils import (_check_if_potential_name,
                                  _get_spaces_before_line,
                                  _handle_parentheses,
                                  _initial_line_checks,
                                  _prep_potential_name)


def script_scraper(pdf: Union[PDF, List[str]],
                   remove_first_line: bool = False,
                   verbose: bool = True,
                   debug: bool = False):
    """
    Return all character's dialogue for a film script.

    Parameters
    ---------------
    pdf: pdftotext.PDF
    remove_first_line: bool
        Remove the first line of every page, useful for when scripts have a set header
    verbose:
        Print character name and dialogue output for each the page
    debug: bool
        Print each page of the script as well as character dialogue collected for that page

    Returns
    ---------------
    words_spoken: dict
        Dictionary with each key being a character's name and the value being a list of all lines of
        dialogue.

    """
    words_spoken = defaultdict(list)

    for page_number in tqdm(range(1, len(pdf))) if debug is True else range(1, len(pdf)):
        page = pdf[page_number]

        page_lines = page.split('\n')
        if remove_first_line:
            page_lines = page_lines[1:]

        words_spoken = _get_character_dialogue_for_page_lines(
            page_lines=page_lines,
            words_spoken=words_spoken,
            verbose=verbose,
        )

        if debug:
            words_spoken_for_page = _get_character_dialogue_for_page_lines(
                page_lines=page_lines,
                words_spoken=defaultdict(list),
                verbose=False,
            )

            print('PAGE TEXT:\n{}'.format(page))
            print('DICTIONARY COLLECTED:\n{}'.format(dict(words_spoken_for_page)))
            print('\n\n---------\n\n')

    return dict(words_spoken)


def _get_character_dialogue_for_page_lines(page_lines, words_spoken, verbose):
    # ASSUMPTION: Dialogue never continues to a new page without character name again on that page.
    # ASSUMPTION: Character names always have at least one space before they speak.
    # ASSUMPTION: All character names and all dialogue have the same number of spaces before each
    #             line.
    # ASSUMPTION: Character names never have "EXT.", "INT.", "TO:", or "SFX:" in the name.
    # ASSUMPTION: Valid character names are in all-caps.
    # ASSUMPTION: Any dialogue occurring within parentheses should not be counted.
    margin_of_error = 2
    currently_speaking = None
    open_bracket = False
    number_of_spaces_for_character = None
    number_of_spaces_for_dialogue = None

    for idx in range(len(page_lines)):
        line = page_lines[idx]
        line = line.rstrip('*')

        spaces_before_line = _get_spaces_before_line(line)

        should_we_continue, currently_speaking = _initial_line_checks(line, currently_speaking)
        if should_we_continue:
            continue

        potential_name = _prep_potential_name(line)
        if (
            potential_name.strip().isupper()
            and potential_name[0] == ' '
            and _get_spaces_before_line(potential_name) >= 9
            and _get_spaces_before_line(potential_name) <= 31
        ):
            if (
                _check_if_potential_name(potential_name)
                and (
                    number_of_spaces_for_character is None
                    or '   ' in potential_name.strip()
                    or spaces_before_line >= number_of_spaces_for_character
                )
            ):
                currently_speaking = potential_name.strip()

                if number_of_spaces_for_character is None and '   ' not in currently_speaking:
                    number_of_spaces_for_character = spaces_before_line - margin_of_error

                if verbose:
                    print('\n', currently_speaking)

                continue

        # assume this is dialogue
        line, open_bracket = _handle_parentheses(line, open_bracket)

        if currently_speaking is not None and '   ' in currently_speaking.strip():
            # we have a case where two characters are speaking
            character_1, character_2 = re.split(r' {2,}', currently_speaking)
            character_1 = character_1.strip()
            character_2 = character_2.strip()

            try:
                line_1, line_2 = re.split(r' {2,}', line.strip())
                line_1 = line_1.strip()
                line_2 = line_2.strip()
            except ValueError:
                number_of_leading_spaces = _get_spaces_before_line(line)
                if number_of_spaces_for_dialogue is None:
                    if number_of_leading_spaces >= 5:
                        line_1 = ''
                        line_2 = line.strip()
                    else:
                        line_1 = line.strip()
                        line_2 = ''
                elif number_of_leading_spaces >= number_of_spaces_for_dialogue:
                    line_1 = ''
                    line_2 = line.strip()
                else:
                    line_1 = line.strip()
                    line_2 = ''

            if line_1:
                words_spoken[character_1].append(line_1)
                if verbose:
                    print(f'     {line_1} [{character_1}]')

            if line_2:
                words_spoken[character_2].append(line_2)
                if verbose:
                    print(f'     {line_2} [{character_2}]')

            if verbose:
                print()

            continue

        if (
            line
            and currently_speaking is not None
            and number_of_spaces_for_dialogue is None
            and not line.isspace()
            and open_bracket is False
        ):
            number_of_spaces_for_dialogue = spaces_before_line

        if (
            number_of_spaces_for_dialogue is not None
            and abs(spaces_before_line - number_of_spaces_for_dialogue) <= margin_of_error
            and currently_speaking is not None
            and open_bracket is False
        ):
            line = line.strip()
            if len(line) > 0:
                words_spoken[currently_speaking].append(line)
                if verbose:
                    print('    ', line)

    return words_spoken
