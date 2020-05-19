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
        '''
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
        '''
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
        '''
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
        '''
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
        '''
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
        '''
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
        '''
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
        '''
    )
