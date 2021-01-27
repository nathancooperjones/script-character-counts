import pytest


@pytest.fixture()
def script_with_description():
    return(
        '''
                         RILEY (CONT'D)
               I am saying something.
               I really am.
     Hobbs studies the location.
                         HOBBS
               So am I.
                   (beat)
               Let's go.
     And as they both look at the particular building, PUSH IN AND
     MATCH DISSOLVE TO:

77   EXT. DECOMMISSIONED BUS DEPOT - (SHAW’S HQ) - DAY            77
     Hobbs and Riley sneak up on the place, guns drawn. Reaching
     the threshold, they look in to find the place completely
     empty.
                         RILEY
               They are gone.
     Hobbs and Riley share a look. Begin walking around,
     inspecting Shaw’s hideout.
                         RILEY (CONT’D)
               They really, really are.
                         HOBBS
               Yes they are.
     And Hobbs bends down.
     And he points at something so small, we can’t see it until he
     takes his knife and scrapes it off the ground: a MICROSCOPIC
     DOT OF OLIVE-DRAB PAINT.
     Hobbs digs in his gear and takes out a BLACKLIGHT, which he
     switches on. The dot of paint on his knife LUMINESCES.
     And then he sweeps the light over the floor REVEALING AN
     OUTLINE OF LUMINESCING PAINT FLECKS.
     Riley looks at Hobbs in awe and respect.
                         RILEY
               Dang!
                         HOBBS
               I know, that was fast!

     Hobbs uses his knife to scrape up a swath of the paint flecks
     and slides them into an evidence baggie.
        '''.split('\n')
    )


@pytest.fixture()
def script_with_no_dialogue():
    return(
        '''
28   DOM AND HOBBS                                                28

     react as -- BOOOOOOOOM!! -- a massive explosion rips through
     the building.

     And then -- ZOOOM! -- Shaw’s Flip Car comes ripping out of
     the building, heading straight for a SQUAD OF POLICE CRUISERS
     racing toward him down the road.

     Instantly, the police OPEN FIRE, but --


29   INT. FLIP CAR - CONTINUOUS                                   29

     -- the bullets BOUNCE harmlessly off the Lexan windshield.
     Bulletproof. Shaw doesn’t even flinch as they spark an inch
     from his face. Totally in control.


30   EXT. SHAW’S HIDEOUT - CONTINUOUS                             30

     The Flip Car streaks head-on for the cops. The Police react,
     trying to swerve out of his way...but Shaw does the one thing
     they don’t expect -- AND SWERVES BACK INTO THE COPS’ PATH
     LIKE AN AUTOMOTIVE KAMIKAZE!


31   EXT. BUILDING ROOFTOP - SAME TIME                            31

     Dom and Hobbs sees the view of this from above. The Cops try
     to avoid a collision, but Shaw is a far better driver,
     SWERVING DIRECTLY BACK INTO THEIR PATH. Shaw hits head-on at
     speed -- and now we see why we call it a “Flip Car”. Shaw’s
     wedge-shaped vehicle acts as a mobile ramp and FLIPS the
     police vehicles -- sending them SMASHING INTO WALLS and the
     other BARREL-ROLLING OFF THE ROAD! (Now we know how that
     police car got stuck on that overpass 50 feet in the air!)

     And a heartbeat later, the Flip Car speeds around a corner
     and disappears into the city.


32   THE PURSUIT (TEAM VS TEAM SEQUENCE)                          32

     TO BE WRITTEN PER DIRECTOR BEATS:

     Canary Wharf

     1. Dom sends team to Interpol.

     2. Shaw driving out.

     3. Implosion.

     4. Shaw driving away.

     Location A
        '''.split('\n')
    )


@pytest.fixture()
def script_with_all_dialogue():
    return(
        '''
          DOM
Hello.

          HOBBS
How's it going being a total
criminal?

          DOM
Well...
    (beat)
It's okay.
        '''.split('\n')
    )


@pytest.fixture()
def script_with_cues():
    return(
        '''
                         DOM
               No.   You don’t.

                                                        CUT TO:


47   EXT. LOOKOUT SPOT - OUTSIDE FIRUZ’S                            47

     Roman is still needling Han --

                         DOM
               It's me, Dom.
        '''.split('\n')
    )


@pytest.fixture()
def script_with_dialogue_but_no_character_name():
    return(
        '''
                         RILEY (CONT'D)
               I am saying something.
               I really am.

               So am I.
                   (beat)
               Let's go.
        '''.split('\n')
    )


@pytest.fixture()
def script_with_dialogue_and_parentheses():
    return(
        '''
B16   EXT. COSTA RICA, DAY                                           B16
      WE FLOAT PAST A BRAND NEW FERRARI towards --
      TEJ, shirtless in the blistering afternoon sun, sporting
      slick headphones blasting muffled beats, stands in front of a
      street ATM kiosk. He busies himself, punching numbers on his
      phone -- then takes out the money he’s withdrawn, pocketing
      the wad of bills. It’s a Tej we’ve never seen before, laid
      back, cash-filled pockets, a baller’s swagger as he heads
      towards - his Ferrari.
      A group of STREET KIDS surround his car admiring it.
      Two buddies come out of a store, SANTIAGO and BENITO, see Tej
      and his new wheels, shaking their heads --
                         SANTIAGO
                    (to Tej, in Spanish)
                Tío, mírate? Conduciendo un nuevo
                Ferrari, con los bolsillos lleno
                de gita.
                (Man, look at you? Rolling up in a
                brand new Ferrari, pockets full of
                cash --)
                I agree!
        '''.split('\n')
    )


@pytest.fixture()
def script_with_dialogue_all_caps_at_end():
    return(
        '''
                     JACK
          ‘Cause the thought alone is killing
          me right nowwwwww...

Jack then turns to the rest of the band, gives them a few
words OFF-MIC, making sure they’re all on the same page. He’s
not just the singer, but the leader. Then-

GUITAR AND BASS BURST IN right with the chorus and the place
EXPLODES WITH PURE ROCK ENERGY-

                     JACK
          HEYYYYYY YAAAAAAA!
          Thanks for coming out!
        '''.split('\n')
    )


@pytest.fixture()
def script_with_dialogue_all_caps_at_beginning():
    return(
        '''

                                                          5.


IN A DINER, same night, they eat french fries, and HIGH-FIVE-

THE BEDROOM, they have sex, reaching climax-


INT. COLLEGE IRISH PUB - NEW NIGHT

THE SONG CLIMAXES- A NEW NIGHT. NEW RAUCOUS CROWD.

                     JACK
          HEEEEEYYYYYY-- YA-

At THAT the band HARD STOPS. A beat. Then THE CROWD GOES NUTS-

                     JACK
          Thank you! We are GIGANTIC!

He steps off the stage, buzzing, as Lauren rushes over-

                     JACK
          Hey! There you are! Fucking crushed
          it, right? I feel like-

                     LAUREN
          -I’m pregnant.
        '''.split('\n')
    )


@pytest.fixture()
def script_with_asterisks_at_the_end():
    return(
        '''
                      Blue Rev. (mm/dd/yy)              84.
                                                        80.

As the carriage approaches a black limousine also approaches
from the other direction. It pulls up and a driver gets out
and opens the rear door.

                      GREGORY                                   *
          Look sad.                                             *
Tashkar gets out.

Tashkar glances across the street at Gregory. Gregory nods.
Leon is quietly astonished.                                     *
                     LUDA                                       *
          Fake or not. Inviting our brother’s                   *
          killer to his funeral might look                      *
          like weakness. Might even look like                   *
          surrender.                                            *
Luda looks at the shocked reactions of the other mourners as    *
Tashkar crosses the street. The horse drawn carriage is
close.

                    GREGORY
          I want everyone to witness Tashkar                    *
          is here and that London is now at                     *
          peace...
The carriage arrives and the black horse halts in the church
doorway. It blows steam into the air. We see Tashkar
approaching through the refracted glass panels of the horse
drawn hearse.

                    GREGORY (CONT'D)
          ....And I want everyone to
          understand that vengeance is the
          business only of the Lord God
          Almighty.
Luda hears something in Gregory’s voice and reacts. Tashkar     *
appears around the black horse and approaches, flanked by two
men. Luda still has time to say softly....                      *

                    LUDA                                        *
          Gregory? You don’t believe in the
          Lord God Almighty.
Gregory’s face is made of stone as Tashkar arrives and holds
out a gloved hand. As the other mourners look on, Gregory
takes his hand and they shake. People react with some
astonishment.

                    TASHKAR
          For reasons of faith I will not
          come into your place of worship.
        '''.split('\n')
    )


@pytest.fixture()
def script_with_character_name_having_more_than_one_word_and_more_than_one_space():
    return(
        '''
                                                         86.


                    SUMMERTIME    FALLTIME    WINTERTIME    SPRING
          These are the seasons that make a person, a person.

Mike starts to cry.

                    KIT
          That was a weird edge case...
        '''.split('\n')
    )


@pytest.fixture()
def script_with_two_characters_talking_at_once_second_more_so():
    return(
        '''
                                                         86.


                    DR. DAVIS
          The radiation won you some time.
          But at this point all we can really
          do is address your symptoms and...
          manage your pain.

Mike starts to cry.

                    KIT
          Thank you for letting us know,
          doctor.

Mike ends the call. Kit remains silent. Mike puts his arms
around him.

                    MIKE
          I hate her so much.

Suddenly, Mike lets go of Kit and snaps open his lap top.
Mike starts typing feverishly.

                    KIT
          What are you doing?

                    MIKE
          I read about a targeted treatment
          for NETs being developed in
          Germany. It’s called...

             KIT                          MIKE (CONT'D)            *
Mike...                           Afinitor. It blocks this like    *
                                  protein signaling pathway        *
                                  that can malfunction and        **
                                  contribute to--                  *

                     KIT
          We’re going to Germany now?
              (beat)
          It’s everywhere. It’s in my brain.

                    MIKE
          Afinitor reduced the risk of
          disease progression or death by
          seventy-nine percent in--

Kit reaches over, closes the lap top. Mike can’t believe it.

                    MIKE (CONT'D)
          There’s a lot of experimental
          research going on right now.

                    KIT
          Stop it. Please stop.
        '''.split('\n')
    )


@pytest.fixture()
def script_with_two_characters_talking_at_once_first_more_so():
    return(
        '''
                                                         86.


                    DR. DAVIS
          The radiation won you some time.
          But at this point all we can really
          do is address your symptoms and...
          manage your pain.

Mike starts to cry.

                    KIT
          Thank you for letting us know,
          doctor.

Mike ends the call. Kit remains silent. Mike puts his arms
around him.

                    MIKE
          I hate her so much.

Suddenly, Mike lets go of Kit and snaps open his lap top.
Mike starts typing feverishly.

                    KIT
          What are you doing?

                    MIKE
          I read about a targeted treatment
          for NETs being developed in
          Germany. It’s called...

             KIT                          MIKE (CONT'D)            *
Mike...                           Afinitor. It blocks this like.   *
I am talking more than you.
Yes, I am.                        But now I am talking too!

                     KIT
          We’re going to Germany now?
              (beat)
          It’s everywhere. It’s in my brain.

                    MIKE
          Afinitor reduced the risk of
          disease progression or death by
          seventy-nine percent in--

Kit reaches over, closes the lap top. Mike can’t believe it.

                    MIKE (CONT'D)
          There’s a lot of experimental
          research going on right now.

                    KIT
          Stop it. Please stop.
        '''.split('\n')
    )


@pytest.fixture()
def script_with_just_two_characters_talking_at_once_second_more_so():
    return(
        '''
                                                         86.

             KIT                          MIKE (CONT'D)            *
Mike...                           Afinitor. It blocks this like    *
                                  protein signaling pathway        *
                                  that can malfunction and        **
                                  contribute to--                  *

                     KIT
          We’re going to Germany now?
              (beat)
          It’s everywhere. It’s in my brain.

                    MIKE
          Afinitor reduced the risk of
          disease progression or death by
          seventy-nine percent in--

Kit reaches over, closes the lap top. Mike can’t believe it.

                    MIKE (CONT'D)
          There’s a lot of experimental
          research going on right now.

                    KIT
          Stop it. Please stop.
        '''.split('\n')
    )


@pytest.fixture()
def script_with_just_two_characters_talking_at_once_first_more_so():
    return(
        '''
                                                         86.

             KIT                          MIKE (CONT'D)            *
Mike...                           Afinitor. It blocks this like.   *
I am talking more than you.
Yes, I am.                        But now I am talking too!

                     KIT
          We’re going to Germany now?
              (beat)
          It’s everywhere. It’s in my brain.

                    MIKE
          Afinitor reduced the risk of
          disease progression or death by
          seventy-nine percent in--

Kit reaches over, closes the lap top. Mike can’t believe it.

                    MIKE (CONT'D)
          There’s a lot of experimental
          research going on right now.

                    KIT
          Stop it. Please stop.
        '''.split('\n')
    )


@pytest.fixture()
def script_with_two_characters_talking_at_once_non_dialogue_line_following():
    return(
        '''
                              ACT FOUR
36  EXT. HOUSE FOR SALE – EARLY MORNING (D4)                    36
    Luna is a character that is really happy. We are about to talk now.
    Here we go.
                         NATALIA
               Hey, kiddos.
                  MAX                             LUNA
    Hi.                              Hey Mom, hey Abuela.
    As the kids buckle their seat belts, Cora takes in Luna’s
    outfit. What did you think of this test?
        '''.split('\n')
    )


@pytest.fixture()
def script_with_two_characters_talking_together_slash():
    return(
        '''
Mike starts to cry.

                    KIT/MIKE
          Thank you./You too.

Mike ends the call. Kit remains silent. Mike puts his arms
around him.

                    MIKE/KIT
          I hate her so much.

                    MIKE/KIT
          I agree./Weird, who is the third person./Me.
        '''.split('\n')
    )


@pytest.fixture()
def script_with_two_characters_talking_together_and():
    return(
        '''
Mike starts to cry.

                    KIT AND MIKE
          Thank you./You too.

Mike ends the call. Kit remains silent. Mike puts his arms
around him.

                    MIKE AND KIT
          I hate her so much.

                    MIKE AND KIT
          I agree./Weird, who is the third person./Me.
        '''.split('\n')
    )


@pytest.fixture()
def script_with_character_name_punctuation():
    return(
        '''
Mike starts to cry.

                    DR. MIKE
          I am a doctor!

Mike ends the call. Kit remains silent. Mike puts his arms
around him.

                    KIT V.O.
          I wish I was in this scene!

                    DR MIKE.
          Spell my name right!
        '''.split('\n')
    )


@pytest.fixture(params=['right_only', 'left_only'])
def script_with_just_two_character_groups_talking_at_once(request):
    if request.param == 'right_only':
        return(
            '''
                 MIKE/MARIAH                  KIT/JIM (CONT'D)     *
    We are saying the same thing!       We are not./Yup, we are not.   *
            '''.split('\n')
        )
    elif request.param == 'left_only':
        return(
            '''
                 KIT/JIM                      MIKE/MARIAH (CONT'D)     *
    We are not./Yup, we are not.       We are saying the same thing!   *
            '''.split('\n')
        )


@pytest.fixture()
def script_with_just_two_character_groups_talking_at_once_both(request):
    return(
        '''
             KIT/JIM                      MIKE/MARIAH (CONT'D)          *
We are not./Yup, we are not.       We are saying the same thing!/Not!   *
        '''.split('\n')
    )
