import pytest


@pytest.fixture()
def counts_with_complete_sentences():
    return {
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
        ],
    }


@pytest.fixture()
def counts_with_elipses_as_sentence_end():
    return {
        'DOM': [
            'Hello.',
            'Well...',
            "It's okay.",
        ],
        'HOBBS': [
            "How's it going being a total",
            'criminal?',
        ],
    }


@pytest.fixture()
def counts_with_elipses_as_sentence_continuation():
    return {
        'DOM': [
            'Hello.',
            'Well...',
            "it's okay.",
        ],
        'HOBBS': [
            "How's it going being a total",
            'criminal?',
        ],
    }


@pytest.fixture()
def counts_with_multiple_sentences_in_one():
    return {
        'DOM': [
            "No.   You don’t.",
            "It's me, Dom.",
        ]
    }


@pytest.fixture()
def counts_with_sentences_continuing():
    return {
        'SANTIAGO': [
            'Tío, mírate? Conduciendo un nuevo',
            'Ferrari, con los bolsillos lleno',
            'de gita.',
            'I agree!!',
            "I am saying a little, little bit more here - it's true??!!?!"
        ]
    }


@pytest.fixture()
def counts_with_fake_words():
    return {
        'JACK': [
            '‘Cause the thought alone is killing',
            'me right nowwwwww...',
            'HEYYYYYY YAAAAAAA!',
            'Thanks for coming out!',
            'gibbly de. gobbly-dee goop!!',
        ]
    }


@pytest.fixture()
def counts_with_one_small_typo():
    return {
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


@pytest.fixture()
def counts_with_two_small_typos():
    return {
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
        'RALEY': [
            'My name is awful!',
        ],
        'DOCTOR TIFFANY': [
            "I'm a doctor!",
        ],
    }


@pytest.fixture()
def counts_with_one_large_typo():
    return {
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
