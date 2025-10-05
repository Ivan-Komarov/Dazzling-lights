# Define the character
define astro = Character("Astronaut", color="#000", who_style = "name_text")
define father = Character("Father", color = '#000', who_style = "name_text")
define music_1 = "audio/music/1bg.mp3"
define astro_right = Position(xpos = 1100, yalign=0.4)
define father_right = Position(yalign = 0.1)
# Define images
image bg space = "images/bg/back1.png"
image bg kitchen = "images/bg/kitchen.png"
image astro normal = "images/characters/1astro/astronaut_normal.png"
image astro thinking = "images/characters/1astro/astronaut_thinking.png"
image astro smiling = "images/characters/1astro/astronaut_smiling.png"
image astro with_hands = "images/characters/1astro/astronaut_with_hands.png"
image astro rolling_eyes = "images/characters/1astro/astronaut_rolling_eyes.png"
image father normal = "images/characters/1father/father_normal.png"
image father hand = "images/characters/1father/father_hand.png"

# define audio.voice1_36_1 = "audio/voice_ukr/1.36.1.mp3"

style quick_button_text:
    font "gui/font/Tektur-Regular.ttf"
    size 25
    color "#FFFFFF"
    hover_color "#FFCC00"

# Start of the game
label start:
    play music music_1 volume 0.5
    scene bg space with fade

    show astro normal at astro_right
    voice "audio/voice/1.2.1.mp3"
    astro "Hmm. Another satellite… Time to check the sensors again."

    jump chapter1_dialog  # move to the main dialog

# Chapter 1 dialog
label chapter1_dialog:
    show astro thinking at astro_right
    voice "audio/voice/1.2.2.mp3"
    astro "You know, it’s funny: my father went to space too. But back then, nobody really talked about the weather up there."

    voice "audio/voice/1.2.3.mp3"
    astro "Solar storms seemed rare, just a little thing. Something you’d read about in magazines, but never really think of every day."
    menu:

        astro "Solar storms seemed rare, just a little thing. Something you’d read about in magazines, but never really think of every day."
        "Continue listening to the astronaut":
            jump astro_ans1

        "So, what did your father say?":
            jump father_ans

# After choices
label astro_ans1:
    show astro smiling at astro_right
    voice "audio/voice/1.4.1.mp3"
    astro "The Sun has always been—and still is—the main player in our lives, although that might sound obvious (I mean, surely you’re not a total blockhead)."

    voice "audio/voice/1.4.2.mp3"
    astro "But if we dig a little deeper, the Sun’s influence goes far beyond just heat and light."

    voice "audio/voice/1.4.3.mp3"
    astro "Over the past few decades, scientists have been observing a noticeable increase in solar and geomagnetic activity."

    voice "audio/voice/1.4.4.mp3"
    astro "This shows up in several ways: the number of solar flares has gone up, massive coronal mass ejections are happening more often, and the solar wind has grown stronger."

    voice "audio/voice/1.4.5"
    astro "Interestingly, this is also linked to variations in galactic cosmic radiation, which are directly influenced by the cycles of solar activity."


    menu:
        astro "It’s also interesting that this is related to variations in galactic cosmic radiation, which directly depend on the cyclic nature of solar activity."
        "Sounds interesting! Tell me more.":
            jump astro_ans2

        "Oh, and you mentioned your father — was he spouting the same nonsense?":
            jump father_ans

label father_ans:
    scene bg kitchen with fade

    show father normal at father_right
    voice "audio/voice/1.26.1.mp3"
    father "Oh, son, space isn’t about some storms. It’s about silence and emptiness."

    show father hand at father_right
    voice "audio/voice/1.26.2.mp3"
    father "You’re flying above the Earth — below you are storms, lightning, oceans. But up here — not a drop of rain, not a breath of wind."

    show father normal at father_right
    voice "audio/voice/1.26.3.mp3"
    father "Weather in space? Ha! What weather? It’s a vacuum out here!"

    scene bg space with fade

    show astro rolling_eyes at astro_right
    voice "audio/voice/1.30.1.mp3"
    astro "But why are you only interested in my father’s stories — don’t you care for me? Then answer my questions!"

    voice "audio/voice/1.30.2.mp3"
    astro "Just appeared on the air, and already annoying me!"
    menu:
        astro "Just appeared on the air, and already annoying me!"
        "Oh, I’d better listen to you after all. I’m sorry.":
            voice "audio/voice/1.28.mp3"
            astro "That’s great!"
            jump astro_ans2

        "No problem! I’m listening to your questions.":
            jump astro_q1

label astro_q1:
    show astro thinking at astro_right
    voice "audio/voice/1.32.1.mp3"
    astro "Alright! Listen up!"
    voice "audio/voice/1.32.2.mp3"
    astro "What is the Sun’s 11-year cycle?"
    menu:

        astro "What is the Sun’s 11-year cycle?"
        "It’s the time it takes for the Sun to rotate around its own axis.":
            jump astro_rep1

        "It’s a long-term cycle of solar activity lasting about a century.":
            jump astro_q2

label astro_rep1:
    show astro rolling_eyes at astro_right
    voice "audio/voice/1.34.mp3"
    astro "Nonsense, not an answer! Now you are interesting to me!"
    jump astro_ans3

label astro_q2:
    show astro smiling at astro_right
    voice "audio/voice/1.36.mp3"
    astro "Alright, you do have some sense after all. Let’s continue! What’s special about the 25th solar cycle?"
    menu:
        astro "Alright, you do have some sense after all. Let’s continue! What’s special about the 25th solar cycle?"
        "It is lasting longer than all previously known cycles.":
            jump astro_rep2

        "Its maximum turned out to be more active than scientists had expected.":
            jump astro_q3

label astro_rep2:
    show astro rolling_eyes at astro_right
    voice "audio/voice/1.38.mp3"
    astro "I was wrong after all! Listen to a sensible person."
    jump astro_ans5

label astro_q3:
    show astro with_hands at astro_right
    voice "audio/voice/1.40.1.mp3"
    astro "Ah, well done!"

    show astro thinking at astro_right
    voice "audio/voice/1.40.2.mp3"
    astro "Then the last question won’t be a problem for you. What do scientists say about the influence of the Solar System’s position in the galaxy?"
    menu:

        astro "Then the last question won’t be a problem for you. What do scientists say about the influence of the Solar System’s position in the galaxy?"
        "It has been proven that the position in the galaxy directly determines the climate on Earth.":
            jump astro_rep4

        "It’s just a hypothesis that so far lacks sufficient evidence.":
            jump astro_q4

label astro_rep4:
    show astro with_hands at astro_right
    voice "audio/voice/1.42.1.mp3"
    astro "Oh, you must be tired. Unfortunately, that’s wrong."

    show astro thinking at astro_right
    voice "audio/voice/1.42.2.mp3"
    astro "Against the backdrop of solar changes, Earth is also exposed to galactic cosmic radiation, the intensity of which also depends on the level of solar activity: it increases during minima and decreases during maxima."

    show astro smiling at astro_right
    voice "audio/voice/1.42.3.mp3"
    astro "Some scientists also consider the possible influence of the Solar System’s position in the galaxy, but these are still just hypotheses."

    jump astro_rep3

label astro_q4:
    show astro with_hands at astro_right
    voice "audio/voice/1.44.mp3"
    astro "Wisely!!!"

    jump astro_rep3

label astro_ans2:
    show astro with_hands at astro_right
    voice "audio/voice/1.6.mp3"
    astro "The increase in solar and geomagnetic activity happens for many reasons, which are still being studied."
    menu:

        astro "The increase in solar and geomagnetic activity happens for many reasons, which are still being studied."
        "Really? Can you show me these studies too, it’s not confidential, right?":
            jump astro_ans3

label astro_ans3:
    show astro normal at astro_right
    voice "audio/voice/1.8.1.mp3"
    astro "Of course!"

    voice "audio/voice/1.8.2.mp3"
    astro "One of the reasons is the Sun’s internal processes. For example, the 11-year cycle."

    voice "audio/voice/1.8.3.mp3"
    menu:

        astro "Do you know what that is?"
        "Yes, I know. I’m listening—tell me more about your research!":
            jump astro_ans4

        "No, I don’t know. Please explain.":
            jump astro_expl

label astro_expl:
    show astro thinking at astro_right
    voice "audio/voice/1.24.1.mp3"
    astro "The 11-year solar cycle (the Schwabe cycle) defines periods of higher and lower activity. During the maximum phase, activity increases—more sunspots and solar flares are observed."

    show astro normal at astro_right
    voice "audio/voice/1.24.2.mp3"
    astro "Now do you understand?"

    jump astro_ans4

label astro_ans4:
    show astro smiling at astro_right
    voice "audio/voice/1.10.1.mp3"
    astro "Great! Then listen up."

    show astro with_hands at astro_right
    voice "audio/voice/1.10.2.mp3"
    astro "Besides the 11-year cycle, there are longer periods too (for example, the Gleissberg cycle—about 80–100 years)."
    menu:

        astro "Besides the 11-year cycle, there are longer periods too (for example, the Gleissberg cycle—about 80–100 years)."
        "Can cycles overlap like that sometimes?":
            jump astro_ans5

label astro_ans5:
    show astro normal at astro_right
    voice "audio/voice/1.12.1.mp3"
    astro "When these cycles “overlap,” they can trigger particularly strong peaks in solar activity."

    show astro thinking at astro_right
    voice "audio/voice/1.12.2.mp3"
    astro "By the way, the Sun has just recently reached the maximum of the 25th cycle (2024–2026), which turned out to be stronger than expected."

    show astro with_hands at astro_right
    voice "audio/voice/1.13.mp3"
    astro "Do you want to hear about the external factors that affect Earth?"

    menu:

        astro "Do you want to hear about the external factors that affect Earth?"
        "Yep!":
            jump astro_ans6

        "No":
            jump astro_ans7

label astro_ans6:
    show astro smiling at astro_right
    voice "audio/voice/1.15.1.mp3"
    astro "Amid these solar changes, Earth is also exposed to galactic cosmic radiation, the intensity of which depends on the level of solar activity: it increases during solar minimums and decreases during maximums."

    show astro thinking at astro_right
    voice "audio/voice/1.15.2.mp3"
    astro "Some scientists also consider the possible influence of the Solar System’s position in the galaxy, but for now, that remains just a hypothesis."

    jump astro_rep3

label astro_ans7:
    show astro rolling_eyes at astro_right
    voice "audio/voice/1.17.mp3"
    astro "It’s even worse for you!"

    jump astro_rep3

label astro_rep3:
    show astro thinking at astro_right
    voice "audio/voice/1.18.mp3"
    astro "So, what brought you here?"
    menu:

        astro "So, what brought you here?"
        "I’ve always been curious about space, so I found you and want to chat with others too.":
            jump astro_ans8

        "Lately I’ve been having headaches. The doctor said it’s all because of magnetic storms.":
            jump astro_ans9



label astro_ans8:
    show astro smiling at astro_right
    voice "audio/voice/1.20.1.mp3"
    astro "Great!"

    voice "audio/voice/1.20.2.mp3"
    astro "You know, go visit the Fox. She’ll tell you more, because it’s my time to go. Bye!"
    stop music fadeout 1.0
    jump chapter2_dialog

label astro_ans9:
    show astro with_hands at astro_right
    voice "audio/voice/1.22.1.mp3"
    astro "Yeah, that could be magnetic storms."

    show astro normal at astro_right
    voice "audio/voice/1.22.2.mp3"
    astro "You know, they don’t just affect people—they affect animals too."

    voice "audio/voice/1.22.3.mp3"
    astro "Go visit the Fox. She’ll tell you more about magnetic storms and fields, and how they affect all of us."

    show astro smiling at astro_right
    voice "audio/voice/1.22.4.mp3"
    astro "It’s my time to go now—good luck!"
    stop music fadeout 1.0
    jump chapter2_dialog




