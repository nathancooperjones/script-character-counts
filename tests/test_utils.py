from unittest import mock

import pytest

from script_scraper.utils import combine_similar_names, word_and_sentence_count


def test_counts_with_complete_sentences(counts_with_complete_sentences):
    expected_riley = (15, 5)
    expected_hobbs = (13, 4)

    actual_riley = word_and_sentence_count(
        single_characters_dialogue=counts_with_complete_sentences['RILEY'],
    )
    actual_hobbs = word_and_sentence_count(
        single_characters_dialogue=counts_with_complete_sentences['HOBBS'],
    )

    assert actual_riley == expected_riley
    assert actual_hobbs == expected_hobbs


def test_counts_with_elipses_as_sentence_end(counts_with_elipses_as_sentence_end):
    expected_dom = (4, 3)
    expected_hobbs = (7, 1)

    actual_dom = word_and_sentence_count(
        single_characters_dialogue=counts_with_elipses_as_sentence_end['DOM'],
    )
    actual_hobbs = word_and_sentence_count(
        single_characters_dialogue=counts_with_elipses_as_sentence_end['HOBBS'],
    )

    assert actual_dom == expected_dom
    assert actual_hobbs == expected_hobbs


def test_counts_with_elipses_as_sentence_continuation(counts_with_elipses_as_sentence_continuation):
    expected_dom = (4, 2)
    expected_hobbs = (7, 1)

    actual_dom = word_and_sentence_count(
        single_characters_dialogue=counts_with_elipses_as_sentence_continuation['DOM'],
    )
    actual_hobbs = word_and_sentence_count(
        single_characters_dialogue=counts_with_elipses_as_sentence_continuation['HOBBS'],
    )

    assert actual_dom == expected_dom
    assert actual_hobbs == expected_hobbs


def test_counts_with_multiple_sentences_in_one(counts_with_multiple_sentences_in_one):
    expected = (6, 3)

    actual = word_and_sentence_count(
        single_characters_dialogue=counts_with_multiple_sentences_in_one['DOM'],
    )

    assert actual == expected


def test_counts_with_sentences_continuing(counts_with_sentences_continuing):
    expected = (25, 4)

    actual = word_and_sentence_count(
        single_characters_dialogue=counts_with_sentences_continuing['SANTIAGO'],
    )

    assert actual == expected


def test_counts_with_fake_words(counts_with_fake_words):
    expected = (19, 4)

    actual = word_and_sentence_count(
        single_characters_dialogue=counts_with_fake_words['JACK'],
    )

    assert actual == expected


@pytest.mark.parametrize('interactive', [False, True])
@mock.patch('builtins.input')
def test_combine_similar_names_with_one_small_typo(input_mock,
                                                   interactive,
                                                   counts_with_one_small_typo):
    expected = {
        'HOBBS': [
            'So am I.',
            "Let's go.",
            'Yes they are.',
            'I know, that was fast!',
        ],
        'RILEY': [
            'Who said that earlier?',
            'Sounds like it was a typo.',
            'The screenwriter should have checked that.',
            'Dang!',
            'I am saying something.',
            'I really am.',
            'They are gone.',
        ],
        'DOCTOR TIFFANY': [
            "I'm a doctor!",
        ],
    }

    input_mock.side_effect = 'yes'

    actual = combine_similar_names(words_spoken_dict=counts_with_one_small_typo,
                                   interactive=interactive)

    assert actual == expected


@mock.patch('builtins.input')
def test_combine_similar_names_with_one_small_typo_interactive_no_combine(
    input_mock, counts_with_one_small_typo
):
    expected = {
        'ROLEY': [
            'I am saying something.',
            'I really am.',
            'They are gone.',
        ],
        'HOBBS': [
            'So am I.',
            "Let's go.",
            'Yes they are.',
            'I know, that was fast!',
        ],
        'RILEY': [
            'Who said that earlier?',
            'Sounds like it was a typo.',
            'The screenwriter should have checked that.',
            'Dang!',
        ],
        'DOCTOR TIFFANY': [
            "I'm a doctor!",
        ],
    }

    input_mock.side_effect = 'no'

    actual = combine_similar_names(words_spoken_dict=counts_with_one_small_typo,
                                   interactive=True)

    assert actual == expected


@mock.patch('builtins.input')
def test_combine_similar_names_with_one_small_typo_interactive_wrong_initial_input(
    input_mock, counts_with_one_small_typo
):
    expected = {
        'ROLEY': [
            'I am saying something.',
            'I really am.',
            'They are gone.',
        ],
        'HOBBS': [
            'So am I.',
            "Let's go.",
            'Yes they are.',
            'I know, that was fast!',
        ],
        'RILEY': [
            'Who said that earlier?',
            'Sounds like it was a typo.',
            'The screenwriter should have checked that.',
            'Dang!',
        ],
        'DOCTOR TIFFANY': [
            "I'm a doctor!",
        ],
    }

    input_mock.side_effect = ['idk', 'no']

    actual = combine_similar_names(words_spoken_dict=counts_with_one_small_typo,
                                   interactive=True)

    assert actual == expected


def test_combine_similar_names_with_two_large_typos(counts_with_two_small_typos):
    expected = {
        'HOBBS': [
            'So am I.',
            "Let's go.",
            'Yes they are.',
            'I know, that was fast!',
        ],
        'RILEY': [
            'Who said that earlier?',
            'Sounds like it was a typo.',
            'The screenwriter should have checked that.',
            'Dang!',
            'I am saying something.',
            'I really am.',
            'They are gone.',
            'My name is awful!',
        ],
        'DOCTOR TIFFANY': [
            "I'm a doctor!",
        ],
    }

    actual = combine_similar_names(words_spoken_dict=counts_with_two_small_typos)

    assert actual == expected


def test_combine_similar_names_with_one_large_typo(counts_with_one_large_typo):
    expected = {
        'RILEY RL': [
            'I am saying something.',
            'I really am.',
            'They are gone.',
        ],
        'HOBBS': [
            'So am I.',
            "Let's go.",
            'Yes they are.',
            'I know, that was fast!',
        ],
        'RILEY': [
            'Who said that earlier?',
            'Sounds like it was a typo.',
            'The screenwriter should have checked that.',
            'Dang!',
        ],
        'DOCTOR TIFFANY': [
            "I'm a doctor!",
        ],
    }

    actual = combine_similar_names(words_spoken_dict=counts_with_one_large_typo)

    assert actual == expected


def test_combine_similar_names_with_one_large_typo_larger_distance(counts_with_one_large_typo):
    expected = {
        'HOBBS': [
            'So am I.',
            "Let's go.",
            'Yes they are.',
            'I know, that was fast!',
        ],
        'RILEY': [
            'Who said that earlier?',
            'Sounds like it was a typo.',
            'The screenwriter should have checked that.',
            'Dang!',
            'I am saying something.',
            'I really am.',
            'They are gone.',
        ],
        'DOCTOR TIFFANY': [
            "I'm a doctor!",
        ],
    }

    actual = combine_similar_names(words_spoken_dict=counts_with_one_large_typo,
                                   max_levenshtein_distance=5)

    assert actual == expected
