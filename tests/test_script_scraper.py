from collections import defaultdict
import pathlib

from script_scraper.script_scraper import _get_character_dialogue_for_page_lines, script_scraper
from script_scraper.utils import open_pdf


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
        ],
    }
    actual = _get_character_dialogue_for_page_lines(
        page_lines=script_with_description.split('\n'),
        words_spoken=defaultdict(list),
        verbose=True,
    )

    assert actual == expected


def test_script_with_no_dialogue(script_with_no_dialogue):
    expected = {}
    actual = _get_character_dialogue_for_page_lines(
        page_lines=script_with_no_dialogue.split('\n'),
        words_spoken=defaultdict(list),
        verbose=True,
    )

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
        ],
    }
    actual = _get_character_dialogue_for_page_lines(
        page_lines=script_with_all_dialogue.split('\n'),
        words_spoken=defaultdict(list),
        verbose=True,
    )

    assert actual == expected


def test_script_with_cues(script_with_cues):
    expected = {
        'DOM': [
            "No.   You don’t.",
            "It's me, Dom.",
        ]
    }
    actual = _get_character_dialogue_for_page_lines(
        page_lines=script_with_cues.split('\n'),
        words_spoken=defaultdict(list),
        verbose=True,
    )

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
        verbose=True,
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
        verbose=True,
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
        verbose=True,
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
        ],
    }
    actual = _get_character_dialogue_for_page_lines(
        page_lines=script_with_dialogue_all_caps_at_beginning.split('\n'),
        words_spoken=defaultdict(list),
        verbose=True,
    )

    assert actual == expected


def test_script_with_asterisks_at_the_end(script_with_asterisks_at_the_end):
    expected = {
        'GREGORY': [
            'Look sad.',
            'I want everyone to witness Tashkar',
            'is here and that London is now at',
            'peace...',
            '....And I want everyone to',
            'understand that vengeance is the',
            'business only of the Lord God',
            'Almighty.',
        ],
        'LUDA': [
            'Fake or not. Inviting our brother’s',
            'killer to his funeral might look',
            'like weakness. Might even look like',
            'surrender.',
            'Gregory? You don’t believe in the',
            'Lord God Almighty.',
        ],
        'TASHKAR': [
            'For reasons of faith I will not',
            'come into your place of worship.',
        ],
    }
    actual = _get_character_dialogue_for_page_lines(
        page_lines=script_with_asterisks_at_the_end.split('\n'),
        words_spoken=defaultdict(list),
        verbose=True,
    )

    assert actual == expected


def test_script_with_two_characters_talking_at_once_second_more_so(
    script_with_two_characters_talking_at_once_second_more_so
):
    expected = {
        'DR DAVIS': [
            'The radiation won you some time.',
            'But at this point all we can really',
            'do is address your symptoms and...',
            'manage your pain.',
        ],
        'KIT': [
            'Thank you for letting us know,',
            'doctor.',
            'What are you doing?',
            'Mike...',
            'We’re going to Germany now?',
            'It’s everywhere. It’s in my brain.',
            'Stop it. Please stop.',
        ],
        'MIKE': [
            'I hate her so much.',
            'I read about a targeted treatment',
            'for NETs being developed in',
            'Germany. It’s called...',
            'Afinitor. It blocks this like',
            'protein signaling pathway',
            'that can malfunction and',
            'contribute to--',
            'Afinitor reduced the risk of',
            'disease progression or death by',
            'seventy-nine percent in--',
            'There’s a lot of experimental',
            'research going on right now.',
        ],
    }
    actual = _get_character_dialogue_for_page_lines(
        page_lines=script_with_two_characters_talking_at_once_second_more_so.split('\n'),
        words_spoken=defaultdict(list),
        verbose=True,
    )

    assert actual == expected


def test_script_with_two_characters_talking_at_once_first_more_so(
    script_with_two_characters_talking_at_once_first_more_so
):
    expected = {
        'DR DAVIS': [
            'The radiation won you some time.',
            'But at this point all we can really',
            'do is address your symptoms and...',
            'manage your pain.',
        ],
        'KIT': [
            'Thank you for letting us know,',
            'doctor.',
            'What are you doing?',
            'Mike...',
            'I am talking more than you.',
            'Yes, I am.',
            'We’re going to Germany now?',
            'It’s everywhere. It’s in my brain.',
            'Stop it. Please stop.',
        ],
        'MIKE': [
            'I hate her so much.',
            'I read about a targeted treatment',
            'for NETs being developed in',
            'Germany. It’s called...',
            'Afinitor. It blocks this like.',
            'But now I am talking too!',
            'Afinitor reduced the risk of',
            'disease progression or death by',
            'seventy-nine percent in--',
            'There’s a lot of experimental',
            'research going on right now.',
        ],
    }
    actual = _get_character_dialogue_for_page_lines(
        page_lines=script_with_two_characters_talking_at_once_first_more_so.split('\n'),
        words_spoken=defaultdict(list),
        verbose=True,
    )

    assert actual == expected


def test_script_with_just_two_characters_talking_at_once_second_more_so(
    script_with_just_two_characters_talking_at_once_second_more_so
):
    expected = {
        'KIT': [
            'Mike...',
            'We’re going to Germany now?',
            'It’s everywhere. It’s in my brain.',
            'Stop it. Please stop.',
        ],
        'MIKE': [
            'Afinitor. It blocks this like',
            'protein signaling pathway',
            'that can malfunction and',
            'contribute to--',
            'Afinitor reduced the risk of',
            'disease progression or death by',
            'seventy-nine percent in--',
            'There’s a lot of experimental',
            'research going on right now.',
        ],
    }
    actual = _get_character_dialogue_for_page_lines(
        page_lines=script_with_just_two_characters_talking_at_once_second_more_so.split('\n'),
        words_spoken=defaultdict(list),
        verbose=True,
    )

    assert actual == expected


def test_script_with_just_two_characters_talking_at_once_first_more_so(
    script_with_just_two_characters_talking_at_once_first_more_so
):
    expected = {
        'KIT': [
            'Mike...',
            'I am talking more than you.',
            'Yes, I am.',
            'We’re going to Germany now?',
            'It’s everywhere. It’s in my brain.',
            'Stop it. Please stop.',
        ],
        'MIKE': [
            'Afinitor. It blocks this like.',
            'But now I am talking too!',
            'Afinitor reduced the risk of',
            'disease progression or death by',
            'seventy-nine percent in--',
            'There’s a lot of experimental',
            'research going on right now.',
        ],
    }
    actual = _get_character_dialogue_for_page_lines(
        page_lines=script_with_just_two_characters_talking_at_once_first_more_so.split('\n'),
        words_spoken=defaultdict(list),
        verbose=True,
    )

    assert actual == expected


def test_script_with_two_characters_talking_at_once_non_dialogue_line_following(
    script_with_two_characters_talking_at_once_non_dialogue_line_following
):
    expected = {
        'NATALIA': [
            'Hey, kiddos.',
        ],
        'MAX': [
            'Hi.',
        ],
        'LUNA': [
            'Hey Mom, hey Abuela.'
        ],
    }

    page_lines = script_with_two_characters_talking_at_once_non_dialogue_line_following.split('\n')
    actual = _get_character_dialogue_for_page_lines(
        page_lines=page_lines,
        words_spoken=defaultdict(list),
        verbose=True,
    )

    assert actual == expected


def test_script_with_two_characters_talking_together_slash(
    script_with_two_characters_talking_together_slash
):
    expected = {
        'KIT': [
            'Thank you.',
            'I hate her so much.',
            'I agree./Weird, who is the third person./Me.',
        ],
        'MIKE': [
            'You too.',
            'I hate her so much.',
            'I agree./Weird, who is the third person./Me.',
        ],
    }

    page_lines = script_with_two_characters_talking_together_slash.split('\n')
    actual = _get_character_dialogue_for_page_lines(
        page_lines=page_lines,
        words_spoken=defaultdict(list),
        verbose=True,
    )

    assert actual == expected


def test_script_with_two_characters_talking_together_and(
    script_with_two_characters_talking_together_and
):
    expected = {
        'KIT': [
            'Thank you./You too.',
            'I hate her so much.',
            'I agree./Weird, who is the third person./Me.',
        ],
        'MIKE': [
            'Thank you./You too.',
            'I hate her so much.',
            'I agree./Weird, who is the third person./Me.',
        ],
    }

    page_lines = script_with_two_characters_talking_together_and.split('\n')
    actual = _get_character_dialogue_for_page_lines(
        page_lines=page_lines,
        words_spoken=defaultdict(list),
        verbose=True,
    )

    assert actual == expected


def test_script_with_character_name_punctuation(
    script_with_character_name_punctuation
):
    expected = {
        'DR MIKE': [
            'I am a doctor!',
            'Spell my name right!',
        ],
        'KIT': [
            'I wish I was in this scene!',
        ],
    }

    page_lines = script_with_character_name_punctuation.split('\n')
    actual = _get_character_dialogue_for_page_lines(
        page_lines=page_lines,
        words_spoken=defaultdict(list),
        verbose=True,
    )

    assert actual == expected


def test_full_script_pipeline():
    expected = {
        'SUMMER': [
            'I was very neat and organized.',
            'Anyway, I should get back.',
            'Love? You seriously believe in that',
            'stuff?',
            'Interesting. A real romantic.',
            'I don’t even know what that word',
            'means. I know I’ve never felt it,',
            'whatever it is in all those songs.',
            'And I know that today most marriages',
            'end in divorce. Like my parents.',
            'Oh yeah, And I read in Newsweek,',
            'there were these scientists who',
            'found that by stimulating a part of',
            'the brain with electrodes you can',
            'make a person fall in “love” with a',
            'rock. Is that the love you’re',
            'talking about?',
            'Why, what’s your take on it?',
        ],
        'TOM': [
            'Ok, well, I’ll see you around.',
            'And it turns out she’s read every',
            'Graham Greene novel ever published.',
            'Her desk is lined with Magritte',
            'posters and Edward Hopper.',
            'We’re so compatible it’s insane!',
            'Seriously! It doesn’t make sense!',
            'She’s not like I thought at all.',
            'She’s amazing.',
            'What?',
            'But, what if you meet someone and',
            'fall in love?',
            'Of course I do.',
            'Summer, hold on, you don’t believe',
            'in love?',
            'Well mine too but --',
            'Well--',
        ],
        'RACHEL': [
            'Your favorites.',
            'Oh boy.',
            'You know just cause some cute girl',
            'likes the same bizarro music you do',
            'doesn’t make her “the one.”',
        ],
        'MCKENZIE': [
            'Oh you have no idea. This one--',
            'embarrassing. There was this one',
            'girl,',
            'I gotta tell this story --',
        ]
    }

    data_dir_path = pathlib.Path(__file__).parent.absolute() / 'fixtures'

    pdf = open_pdf(data_dir_path / '500_days_of_summer_sample_script.pdf')

    actual = script_scraper(pdf=pdf, remove_first_line=True, verbose=True, debug=True)

    assert actual == expected
