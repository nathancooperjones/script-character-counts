from collections import defaultdict
import re
from typing import Dict, List, Tuple, Union

from pdftotext import PDF
from tqdm.auto import tqdm


def script_scraper(pdf: Union[PDF, List[str]],
                   remove_first_line: bool = False,
                   start_page_number: int = 1,
                   verbose: bool = True,
                   debug: bool = False) -> Dict[str, List[str]]:
    """
    Return all character's dialogue for a film script.

    Parameters
    ---------------
    pdf: pdftotext.PDF
    remove_first_line: bool
        Remove the first line of every page, useful for when scripts have a set header
    start_page_number: int
        PDF page to begin analyzing, with a 0-based index (default 1)
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

    pdf_loop = range(start_page_number, len(pdf))
    if debug is True:
        pdf_loop = tqdm(pdf_loop)

    for page_number in pdf_loop:
        if verbose:
            print(page_number)

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


def _get_character_dialogue_for_page_lines(page_lines: List[str],
                                           words_spoken: Dict[str, List[str]],
                                           verbose: bool) -> Dict[str, List[str]]:
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
            and _get_spaces_before_line(potential_name) <= 35
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
            try:
                character_1, character_2 = re.split(r' {2,}', currently_speaking)
            except ValueError:
                # TODO: fix this
                currently_speaking = None

                continue

            character_1 = character_1.strip()
            character_2 = character_2.strip()

            try:
                # if ' ' != line[0]:
                #     continue
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

                if len(line_1) > 35:
                    currently_speaking = None

                    continue

            if line_1:
                words_spoken = _add_line_to_words_spoken(
                    words_spoken=words_spoken,
                    currently_speaking=character_1,
                    line=line_1,
                    verbose=verbose,
                    default_print_str=f'     {{}} [{character_1}]',
                )

            if line_2:
                words_spoken = _add_line_to_words_spoken(
                    words_spoken=words_spoken,
                    currently_speaking=character_2,
                    line=line_2,
                    verbose=verbose,
                    default_print_str=f'     {{}} [{character_2}]',
                )

            if verbose:
                print()

            continue

        if '           ' in line.strip():
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
                words_spoken = _add_line_to_words_spoken(words_spoken=words_spoken,
                                                         currently_speaking=currently_speaking,
                                                         line=line,
                                                         verbose=verbose)

    return words_spoken


def _add_line_to_words_spoken(words_spoken: Dict[str, List[str]],
                              currently_speaking: str,
                              line: str,
                              verbose: bool = True,
                              default_print_str: str = '     {}') -> Dict[str, List[str]]:
    """
    Given the character currently speaking, `currently_speaking`, and a line, `line`, determine
    the right addition to the `words_spoken` dictionary.

    There are three potential scenarios handled here:
    * Multiple characters are speaking at once with potentially different dialogue with a `/`
      separator.
    * Multiple characters are speaking at once with the same line with a `AND` separator.
    * A single character is speaking a single line.

    """
    if '/' in currently_speaking:
        # three scenarios here:
        # 1. separate dialogue is spoken by each character at the same time
        characters_split = currently_speaking.split('/')

        if currently_speaking.count('/') == line.count('/'):
            lines_split = line.split('/')
        else:
            lines_split = [line] * len(characters_split)

        for idx in range(len(characters_split)):
            character_stripped = characters_split[idx].strip()
            line_stripped = lines_split[idx].strip()
            (
                words_spoken[character_stripped]
                .append(line_stripped)
            )
            if verbose:
                print(f'     {line_stripped} [{character_stripped}]')
    elif ' AND ' in currently_speaking:
        characters_split = currently_speaking.split('AND')
        lines_split = [line] * len(characters_split)

        for idx in range(len(characters_split)):
            character_stripped = characters_split[idx].strip()
            line_stripped = lines_split[idx].strip()
            (
                words_spoken[character_stripped]
                .append(line_stripped)
            )
            if verbose:
                print(f'     {line_stripped} [{character_stripped}]')
    else:
        words_spoken[currently_speaking].append(line)
        if verbose:
            print(default_print_str.format(line))

    return words_spoken


def _prep_potential_name(line: str) -> str:
    return re.sub("[^a-zA-Z/ ]+", '', (
        re.sub('\([^\)]+\)', '', line)
        .replace('*', '')
        .replace('V.O.', '')
    ))


def _check_if_potential_name(potential_name: str) -> bool:
    return ('EXT.' not in potential_name
            and 'INT.' not in potential_name
            and 'TO:' not in potential_name
            and 'SFX:' not in potential_name
            and 'COLD OPEN' not in potential_name
            # and 'TAG' not in potential_name
            and not potential_name.strip().startswith('ACT '))


def _initial_line_checks(line: str, currently_speaking: str) -> Tuple[bool, str]:
    we_should_continue = False

    if len(line.strip()) == 0:
        currently_speaking = None
        we_should_continue = True

    return we_should_continue, currently_speaking


def _handle_parentheses(line: str, open_bracket: bool) -> Tuple[str, bool]:
    line = re.sub('\([^\)]+\)', '', line)
    if '(' in line:
        open_bracket = True
    if ')' in line:
        line = line.split(')', 1)[-1]
        open_bracket = False

    return line, open_bracket


def _get_spaces_before_line(line: str) -> int:
    return len(line) - len(line.lstrip(' '))
