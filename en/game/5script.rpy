define astro = Character("Astronaut", color = "#000", who_style = "name_text")
define father = Character("Father", color = "#000", who_style = "name_text")
define child = Character("Child", color = "#000", who_style = "name_text")
define hero = Character("You", color = "#000", who_style = "name_text")

define astro_right = Position(xpos = 1100, yalign=0.4)
define father_right = Position(yalign = 0.1)

style quick_button_text:
    font "gui/font/Tektur-Regular.ttf"
    size 25
    color "#FFFFFF"
    hover_color "#FFCC00"

image end_scene = Movie(size = (1920, 1080), play = "images/movies/end_scene.webm", loop=False)

image astro normal = "images/characters/1astro/astronaut_normal.png"
image astro thinking = "images/characters/1astro/astronaut_thinking.png"
image astro smiling = "images/characters/1astro/astronaut_smiling.png"
image astro with_hands = "images/characters/1astro/astronaut_with_hands.png"
image astro rolling_eyes = "images/characters/1astro/astronaut_rolling_eyes.png"
image father normal = "images/characters/1father/father_normal.png"
image father hand = "images/characters/1father/father_hand.png"
image child normal = "images/characters/5child/child_normal.png"
image child anxiety = "images/characters/5child/child_anxiety.png"
image child smile = "images/characters/5child/child_smile.png"
image animation = Movie(size = (1920, 1080), play = "images/bg/animation.webm", loop=True)

image bg final = "images/bg/final.png"

define child_mus = "audio/music/child.mp3"

label chapter5_dialog:
    play music child_mus volume 0.5
    scene bg final with fade
    show astro smiling at astro_right
    voice "audio/voice/5.2.mp3"
    astro "Yes, we’ve already made it back to Earth. And, you know, I feel like the world has changed a lot since my father’s time"

    menu:
        astro "Yes, we’ve already made it back to Earth. And, you know, I feel like the world has changed a lot since my father’s time"
        "Really? Tell me more about your father!":
            jump father_ans1

        "This time, let’s talk about the future. Oh, is this your child?":
            jump child_ans

label father_ans1:
    scene bg kitchen with fade

    show father normal at father_right
    voice "audio/voice/1.26.1.mp3"
    father "Oh, kiddo, space isn’t about storms or anything like that. It’s about silence and emptiness."

    show father hand at father_right
    voice "audio/voice/1.26.2.mp3"
    father "You fly over Earth—and below, there are thunderstorms, lightning, oceans. But here? Not a drop of rain, not a breath of wind."

    show father normal at father_right
    voice "audio/voice/1.26.3.mp3"
    father "Space weather? Ha! What weather? We’ve got vacuum up here!"

    menu:
        father "Space weather? Ha! What weather? We’ve got vacuum up here!"
        "Astronaut, do you have kids?":
            jump child_ans

label child_ans:
    scene bg final with fade
    show child anxiety at right

    voice "audio/voice/5.6.1.mp3"
    child "We already see the problems waiting for us: solar radiation, unstable crops, new challenges for people’s health."

    voice "audio/voice/5.6.2.mp3"
    show child smile at right
    child "But we can do something about it."

    menu:
        child "But we can do something about it."
        "Protection from solar radiation?":
            jump child_ans1
        "How can we preserve crops?":
            jump child_ans2

label child_ans1:
    show child smile at right
    voice "audio/voice/5.9.1.mp3"
    child "We’re building new satellites and shields for networks and people."

    show child normal at right
    voice "audio/voice/5.9.2.mp3"
    child "They help predict and reduce the effects of solar storms."

    menu:
        child "They help predict and reduce the effects of solar storms."
        "What about new treatments and adaptation methods?":
            jump child_ans3

label child_ans2:
    show child smile at right
    voice "audio/voice/5.11.mp3"
    child "Smart farms, soil sensors, and greenhouses that adjust to the sun help us grow crops even under challenging conditions."

    menu:
        child "Smart farms, soil sensors, and greenhouses that adjust to the sun help us grow crops even under challenging conditions."
        "What about new treatments and adaptation methods?":
            jump child_ans3

label child_ans3:
    show child normal at right
    voice "audio/voice/5.13.1.mp3"
    child "Clinics are already testing advanced skin treatments, and genetic technologies help people adapt to UV exposure."

    show child smile at right
    voice "audio/voice/5.13.2.mp3"
    child "See? This is just the first step."

    show child normal at right
    voice "audio/voice/5.13.3.mp3"
    child "If people learn to protect themselves properly and use these new methods, we can reduce the harm from the sun."

    menu:
        child "Якщо люди навчаться правильно захищати себе та використовувати нові методи, ми можемо зменшити шкоду від сонця."
        "Is this safe for everyone?":
            jump child_ans4

label child_ans4:
    show child normal at right
    voice "audio/voice/5.15.mp3"
    child "Yes, if the technologies are used correctly. But we’re still learning—adaptation is ongoing."

    menu:
        child "Yes, if the technologies are used correctly. But we’re still learning—adaptation is ongoing."
        "And will you be part of all this, sounds exciting?":
            jump child_ans5

        "Still, can we actually beat diseases?":
            jump child_ans6

label child_ans5:
    show child smile at right
    voice "audio/voice/5.17.mp3"
    child "Yep! People like my father are working to make sure the next generations are born healthy and know how to adapt to the sun and space weather."
    jump anim

label child_ans6:
    show child smile at right
    voice "audio/voice/5.19.mp3"
    child "Yes, a proper diet, vitamins, protective measures, and new technologies together can minimize the risks."
    jump anim

label anim:
    window hide
    scene black
    show end_scene
    $ renpy.pause(17, hard=True)
    hide end_scene with fade
    return