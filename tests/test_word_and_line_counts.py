from script_scraper.utils import word_and_sentence_count


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


def test_counts_with_elipses(counts_with_elipses):
    expected_riley = (4, 3)
    expected_hobbs = (7, 1)

    actual_riley = word_and_sentence_count(
        single_characters_dialogue=counts_with_elipses['DOM'],
    )
    actual_hobbs = word_and_sentence_count(
        single_characters_dialogue=counts_with_elipses['HOBBS'],
    )

    assert actual_riley == expected_riley
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
