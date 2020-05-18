from collections import defaultdict

from script_scraper.character_dialogue import (_get_character_dialogue_for_page_lines,
                                               _get_spaces_before_line)


def test_script_with_description(script_with_description):
    expected = {
        'RILEY': [
            'I am saying something.',
            'I really am.',
            'They are gone.',
            'They really, really are.',
            'Dang!',
        ],
        'HOBBS': [
            'So am I.',
            "Let's go.",
            'Yes they are.',
            'I know, that was fast!',
        ]
    }
    space_num = _get_spaces_before_line('     Roman is still needling Han --')
    actual = _get_character_dialogue_for_page_lines(page_lines=script_with_description.split('\n'),
                                                    words_spoken=defaultdict(list),
                                                    number_of_spaces_for_script=space_num)

    assert actual == expected


def test_script_with_no_dialogue(script_with_no_dialogue):
    expected = {}
    space_num = _get_spaces_before_line('     Roman is still needling Han --')
    actual = _get_character_dialogue_for_page_lines(page_lines=script_with_no_dialogue.split('\n'),
                                                    words_spoken=defaultdict(list),
                                                    number_of_spaces_for_script=space_num)

    assert actual == expected


def test_script_with_all_dialogue(script_with_all_dialogue):
    expected = {
        'DOM': [
            'Hello.',
            'Well...',
            "It's okay.",
        ],
        'HOBBS': [
            "How's it going being a total",
            'criminal?',
        ]
    }
    space_num = _get_spaces_before_line('     Roman is still needling Han --')
    actual = _get_character_dialogue_for_page_lines(page_lines=script_with_all_dialogue.split('\n'),
                                                    words_spoken=defaultdict(list),
                                                    number_of_spaces_for_script=space_num)

    assert actual == expected


def test_script_with_cues(script_with_cues):
    expected = {
        'DOM': [
            "No.   You don’t.",
            "It's me, Dom.",
        ]
    }
    space_num = _get_spaces_before_line('     Roman is still needling Han --')
    actual = _get_character_dialogue_for_page_lines(page_lines=script_with_cues.split('\n'),
                                                    words_spoken=defaultdict(list),
                                                    number_of_spaces_for_script=space_num)

    assert actual == expected


def test_script_with_dialogue_but_no_character_name(script_with_dialogue_but_no_character_name):
    expected = {
        'RILEY': [
            'I am saying something.',
            'I really am.',
        ]
    }
    space_num = _get_spaces_before_line('     Roman is still needling Han --')
    actual = _get_character_dialogue_for_page_lines(
        page_lines=script_with_dialogue_but_no_character_name.split('\n'),
        words_spoken=defaultdict(list),
        number_of_spaces_for_script=space_num
    )

    assert actual == expected
