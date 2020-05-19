from collections import defaultdict

from script_scraper.character_dialogue import (_get_character_dialogue_for_page_lines)


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
    actual = _get_character_dialogue_for_page_lines(page_lines=script_with_description.split('\n'),
                                                    words_spoken=defaultdict(list))

    assert actual == expected


def test_script_with_no_dialogue(script_with_no_dialogue):
    expected = {}
    actual = _get_character_dialogue_for_page_lines(page_lines=script_with_no_dialogue.split('\n'),
                                                    words_spoken=defaultdict(list))

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
    actual = _get_character_dialogue_for_page_lines(page_lines=script_with_all_dialogue.split('\n'),
                                                    words_spoken=defaultdict(list))

    assert actual == expected


def test_script_with_cues(script_with_cues):
    expected = {
        'DOM': [
            "No.   You don’t.",
            "It's me, Dom.",
        ]
    }
    actual = _get_character_dialogue_for_page_lines(page_lines=script_with_cues.split('\n'),
                                                    words_spoken=defaultdict(list))

    assert actual == expected


def test_script_with_dialogue_but_no_character_name(script_with_dialogue_but_no_character_name):
    expected = {
        'RILEY': [
            'I am saying something.',
            'I really am.',
        ]
    }
    actual = _get_character_dialogue_for_page_lines(
        page_lines=script_with_dialogue_but_no_character_name.split('\n'),
        words_spoken=defaultdict(list),
    )

    assert actual == expected


def test_script_with_dialogue_and_parentheses(script_with_dialogue_and_parentheses):
    expected = {
        'SANTIAGO': [
            'Tío, mírate? Conduciendo un nuevo',
            'Ferrari, con los bolsillos lleno',
            'de gita.',
            'I agree!',
        ]
    }
    actual = _get_character_dialogue_for_page_lines(
        page_lines=script_with_dialogue_and_parentheses.split('\n'),
        words_spoken=defaultdict(list),
    )

    assert actual == expected


def test_script_with_dialogue_all_caps_at_end(script_with_dialogue_all_caps_at_end):
    expected = {
        'JACK': [
            '‘Cause the thought alone is killing',
            'me right nowwwwww...',
            'HEYYYYYY YAAAAAAA!',
            'Thanks for coming out!',
        ]
    }
    actual = _get_character_dialogue_for_page_lines(
        page_lines=script_with_dialogue_all_caps_at_end.split('\n'),
        words_spoken=defaultdict(list),
    )

    assert actual == expected


def test_script_with_dialogue_all_caps_at_beginning(script_with_dialogue_all_caps_at_beginning):
    expected = {
        'JACK': [
            'HEEEEEYYYYYY-- YA-',
            'Thank you! We are GIGANTIC!',
            'Hey! There you are! Fucking crushed',
            'it, right? I feel like-',
        ],
        'LAUREN': [
            '-I’m pregnant.',
        ]
    }
    actual = _get_character_dialogue_for_page_lines(
        page_lines=script_with_dialogue_all_caps_at_beginning.split('\n'),
        words_spoken=defaultdict(list),
    )

    assert actual == expected
