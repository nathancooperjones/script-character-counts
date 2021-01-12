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
def counts_with_elipses():
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
