define answer = 0
define fox = Character("Fox", color = "#000", who_style = "name_text")
define bird = Character("Bird", color = "#000", who_style = "name_text")
define hero = Character("You", color = '#000', who_style = "name_text")

define music2_1 = "audio/music/forestbg.mp3"
define music2_2 = "audio/music/minigame.mp3"

image fox angry = "images/characters/2fox/fox_angry.png"
image fox frightened = "images/characters/2fox/fox_frightened.png"
image fox normal = "images/characters/2fox/fox_normal.png"
image fox smile = "images/characters/2fox/fox_smile.png"
image fox telling = "images/characters/2fox/fox_telling.png"
image fox head = "images/characters/2fox/fox_head.png"
image fox mouth = "images/characters/2fox/fox_mouth.png"

image bird normal = "images/characters/2bird/bird_normal.png"
image bird happy = "images/characters/2bird/bird_happy.png"
image bird telling = "images/characters/2bird/bird_telling.png"
image bird frightened = "images/characters/2bird/bird_frightened.png"
image bird head = "images/characters/2bird/bird_head.png"
image bird mouth = "images/characters/2bird/bird_mouth.png"

image bg fox = "images/bg/foxbg.png"
image bg bird = "images/bg/birdbg.png"

image mov0 = Movie(size = (1920, 1080), play = "images/movies/mov.webm", loop=True)
image mov1 = Movie(size = (1920, 1080), play = "images/movies/mov-1.webm", loop=True)
image mov2 = Movie(size = (1920, 1080), play = "images/movies/mov-2.webm", loop=True)
image mov3 = Movie(size = (1920, 1080), play = "images/movies/mov-3.webm", loop=True)
image mov4 = Movie(size = (1920, 1080), play = "images/movies/mov-4.webm", loop=True)
image mov5 = Movie(size = (1920, 1080), play = "images/movies/mov-5.webm", loop=True)

image mov_1 = Movie(size = (1920, 1080), play = "images/movies/mov+1.webm", loop=True)
image mov_2 = Movie(size = (1920, 1080), play = "images/movies/mov+2.webm", loop=True)
image mov_3 = Movie(size = (1920, 1080), play = "images/movies/mov+3.webm", loop=True)
image mov_4 = Movie(size = (1920, 1080), play = "images/movies/mov+4.webm", loop=True)
image mov_5 = Movie(size = (1920, 1080), play = "images/movies/mov+5.webm", loop=True)

image bg bird_saved = "images/bg/field_no.png"
style quick_button_text:
    font "gui/font/Tektur-Regular.ttf"
    size 25
    color "#FFFFFF"
    hover_color "#FFCC00"

label chapter2_dialog:
    play music music2_1 volume 0.5
    scene bg fox with fade
    show fox frightened at left

    voice "audio/voice/2.1.1.mp3"
    fox "Oh my gosh, you scared me!"
    show fox normal at left
    voice "audio/voice/2.1.2.mp3"
    fox "Well, hello there, traveler."

    voice "audio/voice/2.1.3.mp3"
    fox "What do you want from me?"
    menu:
        fox "What do you want from me?"
        "I want to know more about the magnetic field and storms.":
            show fox telling at left
            voice "audio/voice/2.3.1.mp3"
            fox "Magnetic storms are a natural phenomenon, when Earth’s magnetic field gets disturbed by a strong flow of charged particles from the Sun."
            voice "audio/voice/2.3.2.mp3"
            fox "Such bursts of solar energy are called solar flares."

            show fox smile at left
            voice "audio/voice/2.3.3.mp3"
            fox "Want to hear how the magnetic field and storms affect us animals?"
            menu:
                fox "Want to hear how the magnetic field and storms affect us animals?"
                "Yes, of course":
                    jump fox_story
                "Honestly, I’m not that eager.":
                    show fox angry at left
                    voice "audio/voice/2.7.mp3"
                    fox "I just can’t deal with you anymore! Go find a bird—maybe it will put up with you!"
                    jump bird_story

label fox_story:
    show bg fox with fade
    show fox normal at left
    voice "audio/voice/2.5.mp3"
    fox "Oh, I don’t even know where to start—maybe you have a question?"
    menu:
        fox "Oh, I don’t even know where to start—maybe you have a question?"
        "Is it true that magnetic storms affect your behavior?":
            show fox telling at left
            voice "audio/voice/2.9.1.mp3"
            fox "Magnetic storms really do affect us, the animals. We can become more anxious, restless, sometimes even aggressive—or, on the contrary, withdrawn and sluggish."
            voice "audio/voice/2.9.2.mp3"
            fox "Blah-blah-blah… are you really interested in that?"
            menu:
                fox "Blah-blah-blah… are you really interested in that?"
                "Yes!":
                    show fox normal at left
                    voice "audio/voice/2.11.1.mp3"
                    fox "Alright then, I’ll tell you something else."

                    show fox telling at left
                    voice "audio/voice/2.11.2.mp3"
                    fox "Magnetic storms can also affect their ability to navigate, messing up migration routes."

                    show fox angry at left
                    voice "audio/voice/2.11.3.mp3"
                    fox "Now shoo, I’ve got better things to do at night — I’m hungry."
                    jump bird_story
                "No, just the facts, no extra details.":
                    show fox angry at left
                    voice "audio/voice/2.13.1.mp3"
                    fox "Oh, go on to the bird then, I’ve got nothing better to do than wander around with you."

                    show fox normal at left
                    voice "audio/voice/2.13.2.mp3"
                    fox "All I want is food anyway…"
                    jump bird_story

        "Is it true that during a storm it’s harder to fly and find your way in the sky?":
            show fox angry at left
            voice "audio/voice/2.15.mp3"
            fox "Take that question to a bird instead—and if possible, don’t come back."
            jump bird_story

label bird_story:
    hide fox
    show bg bird with fade
    show bird normal at right
    voice "audio/voice/2.16.1.mp3"
    bird "Oh, heeey there!"

    show bird telling at right
    voice "audio/voice/2.16.2.mp3"
    bird "You also came to learn how the magnetic field and storms affect the birdie clan?"
    menu:
        bird "You also came to learn how the magnetic field and storms affect the birdie clan?"
        "Yep!":
            show bird happy at right
            voice "audio/voice/2.18.1.mp3"
            bird "Then make yourself comfy!"

            show bird telling at right
            voice "audio/voice/2.18.2.mp3"
            bird "Birds react a bit differently, they can use…"
            menu:
                bird "Birds react a bit differently, they can use…"
                "Hey, hey, hey! Slow down, little one.":
                    voice "audio/voice/2.20.1.mp3"
                    bird "Oh, fine! But don’t interrupt me again!"
                    voice "audio/voice/2.20.2.mp3"
                    bird "Birds, well… react a bit differently, they can use the magnetic field for navigation, so when it changes, uhhh, their routes can get messed up."

                    show bird normal at right
                    voice "audio/voice/2.20.3.mp3"
                    bird "What else am I supposed to tell you? I don’t really remember anything else, honestly."
                    voice "audio/voice/2.20.4.mp3"
                    bird "Well, I think I told you the basics. Go back to the fox, maybe she’ll add something."
                    menu:
                        bird "Well, I think I told you the basics. Go back to the fox, maybe she’ll add something."
                        "She ran off somewhere, please take me to her.":
                            show bird happy at right
                            voice "audio/voice/2.22.mp3"
                            bird "Well, fine, let’s go!"
                            jump pregame_catch

label pregame_catch:

    scene bg fox with fade
    show bird normal at right
    show fox smile at left
    hero "Fox, we’ve got a question…"
    voice "audio/voice/2.24.mp3"
    fox "Oh, you’ve brought me lunch!"
    show bird frightened at right
    voice "audio/voice/2.25.mp3"
    bird "Uh, what exactly are you implying?!"
    voice "audio/voice/2.26.mp3"
    fox "You’re about to find out."
    voice "audio/voice/2.27.mp3"
    bird "ААААААААААААААААА!!!"
    jump game_catch

label game_catch:
    play music music2_2 volume 0.5
    show mov0
    menu:
        "Can marine animals, like whales or dolphins, get their route confused due to changes in the magnetic field?"
        "Yes, sometimes changes in the magnetic field disrupt their built-in navigation, causing disorientation.":
            $ answer += 1
            show mov1
        "No, they navigate exclusively by the stars and the position of the Sun.":
            $ answer -= 1
            show mov_1
    menu:
        "Which animals rely most on Earth's magnetic field for survival?"
        "Migratory birds, sea turtles, and fish that travel long distances.":
            $ answer += 1
            show mov2
        "Large land predators like lions and tigers, because they use the magnetic field for hunting.":
            $ answer -= 1
            show mov_2
    menu:
        "How exactly can magnetic storms change animal behavior in the wild?"
        "Magnetic storms only cause physical fatigue in animals, but don’t affect their instincts or behavior.":
            $ answer -= 1
            show mov3
        "They affect the orientation of animals that use Earth's magnetic field — for example, birds or fish — so they may change migration routes or get lost.":
            $ answer += 1
            show mov_3
    menu:
        "Can we say that space weather shapes certain evolutionary mechanisms in animals?"
        "Yes, constant exposure to cosmic factors has forced animals to develop the ability to 'read' the magnetic field.":
            $ answer += 1
            show mov4
        "No, evolution depends only on climate and the availability of food on the planet.":
            $ answer -= 1
            show mov_4
    menu:
        "Which animals are most vulnerable to changes in space, and which hardly notice them?"
        "Only insects are vulnerable; all large animals hardly feel cosmic changes at all.":
            $ answer -= 1
            show mov5
        "The most sensitive are migratory species (birds, whales, turtles), while the least sensitive are those living locally and not migrating.":
            $ answer += 1
            show mov_5
    if answer > 0:
        jump catch_good_ending
    else:
        jump catch_bad_ending

label catch_good_ending:
    scene bg bird_saved with fade
    show bird happy at right
    voice "audio/voice/2.30.mp3"
    bird "Huh!"
    menu:
        bird "Huh!"
        "Fox almost caught you":
            voice "audio/voice/2.32.mp3"
            bird "But it was fun, yeeeeee! If you go across the field to the river, you’ll reach the lonely wise oak… it’ll tell you way more than I ever could, yeah."
            stop music
            jump chapter3_dialog

label catch_bad_ending:

    scene bg fox with fade
    show fox smile at left
    voice "audio/sound/crunch.mp3"
    fox "Oh, well, I’m grateful to you for fetching such a tasty lunch."
    voice "audio/voice/2.28.mp3"
    fox "Oh, well, I’m grateful to you for fetching such a tasty lunch."
    menu:
        fox "Oh, well, I’m grateful to you for fetching such a tasty lunch."
        "What did u do...":
            show fox telling at left
            voice "audio/voice/2.29.mp3"
            fox "Don’t worry too much—look on the bright side. Since you helped me, here’s a map that will lead you to the oak tree."
            stop music
            jump chapter3_dialog