define oak = Character("Oak", color="#000", who_style = "name_text")
define sunflower = Character("Sunflower", color = '#000', who_style = "name_text")
image bg field = "images/bg/field_no.png"
image bg sunb = "images/bg/sunb.png"
image bg suns = "images/bg/sunsss.png"
image oak normal = "images/characters/3oak/oak_normal.png"
image oak up = "images/characters/3oak/oak_sticks_up.png"
image oak down = "images/characters/3oak/oak_sticks_down.png"
image sunflower leaf = "images/characters/3sunflower/sunflower_leaf.png"
image sunflower normal = "images/characters/3sunflower/sunflower_normal.png"
image sunflower smiling = "images/characters/3sunflower/sunflower_smiling.png"
image bg f = "images/bg/f.png"

define music_oak = "audio/music/oak.mp3"
define music_sf = "audio/music/sunflower.mp3"

style quick_button_text:
    font "gui/font/Tektur-Regular.ttf"
    size 25
    color "#FFFFFF"
    hover_color "#FFCC00"

label chapter3_dialog:
    play music music_oak volume 0.5
    scene bg f with fade
    scene bg field with fade
    show oak normal at left
    voice "audio/voice/3.1.1.mp3"
    oak "I’ve been standing here for so many years, and I’ve never met you before."

    voice "audio/voice/3.1.2.mp3"
    oak "Who are you then?"
    menu:
        oak "Who are you then?"
        "I’m a traveler. I’m curious about space. Oh, Oak, you’ve seen more than a century. Tell me, do trees feel the weather from space?":
            jump oak_ans1

label oak_ans1:
    show oak up at left
    voice "audio/voice/3.3.mp3"
    oak "Yes, we feel it. When the Sun sends its storms toward Earth, the magnetic field changes, and our sap flows differently. Some of us grow slower, some faster."
    menu:
        oak "Yes, we feel it. When the Sun sends its storms toward Earth, the magnetic field changes, and our sap flows differently. Some of us grow slower, some faster."
        "So even your roots know what’s happening on the Sun?":
            jump oak_ans2

        "But you’re so mighty. Can a storm in the sky really hurt you?":
            jump oak_ans3

label oak_ans2:
    show oak down at left
    voice "audio/voice/3.5.1.mp3"
    oak "Exactly. The roots listen to the Earth, and the Earth feels the cosmos."

    show oak normal at left

    voice "audio/voice/3.5.2.mp3"
    oak "Radiation, magnetic disturbances—everything affects the crops, the blooming, the growth of forests."
    menu:
        oak "Radiation, magnetic disturbances—everything affects the crops, the blooming, the growth of forests."
        "So we’re all connected and affected by the storms? Even our breathing?":
            jump oak_ans4

label oak_ans3:
    show oak up at left
    voice "audio/voice/3.7.1.mp3"
    oak "I’m strong because I’ve grown used to it over time. But young shoots are more delicate."

    show oak normal at left
    voice "audio/voice/3.7.2.mp3"
    oak "When the climate changes due to cosmic processes, when the Sun shines stronger or weaker—it’s harder for the young ones to survive."
    menu:
        oak "When the climate changes due to cosmic processes, when the Sun shines stronger or weaker—it’s harder for the young ones to survive."
        "Can we say that space controls nature, like a conductor controls an orchestra?":
            jump oak_ans5

label oak_ans4:
    show oak up at left
    voice "audio/voice/3.9.1.mp3"
    oak "Of course, even breathing—though it’s harder to notice."

    show oak down at left
    voice "audio/voice/3.9.2.mp3"
    oak "Young shoots are more delicate. When the climate changes because of cosmic processes, when the Sun shines stronger or weaker, it’s harder for the young ones to survive."
    menu:
        oak "Young shoots are more delicate. When the climate changes because of cosmic processes, when the Sun shines stronger or weaker, it’s harder for the young ones to survive."
        "So does that mean space controls nature?":
            jump oak_ans6

label oak_ans5:
    show oak normal at left
    voice "audio/voice/3.13.1.mp3"
    oak "Nice comparison. We, the trees, play the notes of light and shadow, of water and warmth."

    show oak down at left
    voice "audio/voice/3.13.2.mp3"
    oak "And sometimes space changes the rhythm. Then the whole music sounds different."
    menu:
        oak "And sometimes space changes the rhythm. Then the whole music sounds different."
        "What about the flowers? They’re so delicate—how do they feel space?":
            jump oak_ans7

label oak_ans6:
    show oak normal at left
    voice "audio/voice/3.15.1.mp3"
    oak "Exactly. The roots listen to the Earth, and the Earth feels space."

    show oak down at left
    voice "audio/voice/3.15.2.mp3"
    oak "Radiation, magnetic disturbances—everything affects the crops, the blooming, the growth of forests."
    menu:
        oak "Radiation, magnetic disturbances—everything affects the crops, the blooming, the growth of forests."
        "Tell me about the forests. How does space touch them?":
            jump oak_ans8

label oak_ans7:
    show oak normal at left
    voice "audio/voice/3.17.1.mp3"
    oak "Flowers need light. If the Sun blazes too brightly, their petals burn faster, and they bloom less."

    voice "audio/voice/3.17.2.mp3"
    oak "If there isn’t enough light, they become fragile, as if they’ve lost their colors. Bees get confused about the blooming time, and then there’s less honey."
    menu:
        oak "If there isn’t enough light, they become fragile, as if they’ve lost their colors. Bees get confused about the blooming time, and then there’s less honey."
        "So that means even beauty depends on space?":
            jump oak_ans9

        "Interesting! Does that mean even our mood is somehow connected to these rhythms?":
            jump oak_ans10
label oak_ans8:
    show oak up at left
    voice "audio/voice/3.23.1.mp3"
    oak "Forests are like the lungs of the Earth."

    show oak down at left
    voice "audio/voice/3.23.2.mp3"
    oak "When solar storms change the climate, some trees grow faster, while others wither."

    show oak normal at left
    voice "audio/voice/3.23.3.mp3"
    oak "Young shoots often can’t withstand sudden heat or cold. And then the forest loses its strength."

    menu:
        oak "Young shoots often can’t withstand sudden heat or cold. And then the forest loses its strength."
        "But you stand so firm. Can space really take away your strength?":
            jump oak_ans11

        "And people? Do they feel it the way you do?":
            jump oak_ans12

label oak_ans9:
    show oak up at left
    voice "audio/voice/3.19.1.mp3"
    oak "Yes. But remember: the beauty of flowers isn’t just for the eyes."

    show oak normal at left
    voice "audio/voice/3.19.2.mp3"
    oak "They feed the bees, and the bees feed the fields. And if the rhythm of blooming changes, so does the harvest that people get."

    menu:
        oak "They feed the bees, and the bees feed the fields. And if the rhythm of blooming changes, so does the harvest that people get."
        "I guess the most important thing for people is the harvest. How does it depend on space?":
            jump oak_ans13

label oak_ans10:
    show oak normal at left
    voice "audio/voice/3.21.mp3"
    oak "You could say that. When flowers bloom late or wither early, the food for bees and birds changes, and then people feel it too—from breakfast to the harvest festival."
    menu:
        oak "You could say that. When flowers bloom late or wither early, the food for bees and birds changes, and then people feel it too—from breakfast to the harvest festival."
        "I guess the most important thing for people is the harvest. How does it depend on space?":
            jump oak_ans13

label oak_ans11:
    show oak up at left
    voice "audio/voice/3.25.1.mp3"
    oak "I stand firm because I’ve been hardened over time. But not all trees have that chance."

    voice "audio/voice/3.25.2.mp3"
    oak "In the mountains, pines wither faster, and in the steppes, acacias bloom more. And all of this comes from the Sun’s echo."

    show oak normal at left
    voice "audio/voice/3.25.3.mp3"
    oak "But the biggest changes aren’t seen deep in the forest… they’re seen where people sow the grain."

    menu:
        oak "But the biggest changes aren’t seen deep in the forest… they’re seen where people sow the grain."
        "I guess the most important thing for people is the harvest. How does it depend on space?":
            jump oak_ans13

label oak_ans12:
    show oak normal at left
    voice "audio/voice/3.27.1.mp3"
    oak "People eat bread. Bread is born in the fields."

    show oak down at left
    voice "audio/voice/3.27.2.mp3"
    oak "But that’s not for me to tell you."

    menu:
        oak "But that’s not for me to tell you."
        "I guess the most important thing for people is the harvest. How does it depend on space?":
            jump oak_ans13

label oak_ans13:
    show oak up at left
    voice "audio/voice/3.28.mp3"
    oak "The Sun can be a friend, but it can also be an enemy. If its storms are too strong, the wheat in the fields burns out."
    menu:
        oak "The Sun can be a friend, but it can also be an enemy. If its storms are too strong, the wheat in the fields burns out."
        "So it all comes down to the bread we eat?":
            jump oak_ans14

label oak_ans14:
    show oak down at left
    voice "audio/voice/3.30.1.mp3"
    oak "Exactly. And if you really want to understand it, go to the one who sows and harvests."

    show oak normal at left
    voice "audio/voice/3.30.2.mp3"
    oak "The farmer will tell you how every storm in the sky echoes across his fields."

    scene bg sunb with fade
    jump sunflower_ans

label sunflower_ans:
    play music music_sf volume 0.5
    scene bg suns with fade
    show sunflower smiling at right

    voice "audio/voice/3.31.mp3"
    sunflower " Hi! Where are you from in our parts? I’m seeing you for the first time."

    menu:
        sunflower " Hi! Where are you from in our parts? I’m seeing you for the first time."
        "Are you always this cheerful?":
            jump sunflower_ans1

        "Why do you always look up at the Sun?":
            jump sunflower_ans2

        "I’m a traveler, and I’m heading to the farmer.":
            jump sunflower_ans3

label sunflower_ans1:
    show sunflower normal at right
    voice "audio/voice/3.33.1.mp3"
    sunflower "Haha! Of course. I look straight at the Sun—I don’t have time to be sad!"

    voice "audio/voice/3.33.2.mp3"
    sunflower "But sometimes it’s too wild… and even I struggle then."
    menu:
        sunflower "But sometimes it’s too wild… and even I struggle then."
        "What exactly is hard?":
            jump sunflower_ans4

        "Are you afraid of the Sun?":
            jump sunflower_ans5

label sunflower_ans4:
    show sunflower leaf at right
    voice "audio/voice/3.35.1.mp3"
    sunflower "When solar storms strike, my petals burn faster, and my leaves lose strength."

    voice "audio/voice/3.35.2.mp3"
    sunflower "I’m still holding on, but my brothers in the field are suffering."

    menu:
        sunflower "I’m still holding on, but my brothers in the field are suffering."
        "You’ve told me a lot. So even your life depends on the storms on the Sun.":
            jump sunflower_rep1

label sunflower_ans5:
    show sunflower smiling at right
    voice "audio/voice/3.37.1.mp3"
    sunflower "Haha! No, it’s my idol! It’s just that sometimes it goes too far."

    voice "audio/voice/3.37.2.mp3"
    sunflower "Like the best friend who can lift your spirits but also hit your shoulder hard enough to hurt."

    menu:
        sunflower "Like the best friend who can lift your spirits but also hit your shoulder hard enough to hurt."
        "You’ve told me a lot. So even your life depends on the storms on the Sun.":
            jump sunflower_rep1

label sunflower_ans2:
    show sunflower normal at right
    voice "audio/voice/3.39.1.mp3"
    sunflower "Because it’s my light, my life. I turn toward it, like a fan chasing their favorite star."

    voice "audio/voice/3.39.2.mp3"
    sunflower "And when the Sun gets angry—I feel it through my whole stem."

    menu:
        sunflower "And when the Sun gets angry—I feel it through my whole stem."
        "So you feel space with your body?":
            jump sunflower_ans6

label sunflower_ans6:
    show sunflower smiling at right
    voice "audio/voice/3.41.1.mp3"
    sunflower "Of course! The leaves tremble from the heat, the stem bends from the dryness, the petals fall earlier."

    voice "audio/voice/3.41.2.mp3"
    sunflower "We are a living barometer of space."
    menu:
        sunflower "We are a living barometer of space."
        "That sounds sad…":
            jump sunflower_ans7

label sunflower_ans7:
    show sunflower leaf at right
    voice "audio/voice/3.43.1.mp3"
    sunflower "Haha! No! Because even on the hardest day, I still turn toward the light."

    voice "audio/voice/3.43.2.mp3"
    sunflower "It’s my nature—not to give up."

    menu:
        sunflower "It’s my nature—not to give up."
        "You’ve told me a lot. So even your life depends on the storms on the Sun.":
            jump sunflower_rep1

label sunflower_ans3:
    show sunflower smiling at right
    voice "audio/voice/3.49.mp3"
    sunflower "He’s working right now, so let me help you. Ask whatever you want!"

    menu:
        sunflower "He’s working right now, so let me help you. Ask whatever you want!"
        "Does space weather affect the harvest?":
            jump sunflower_ans8

label sunflower_ans8:
    show sunflower normal at right
    voice "audio/voice/3.51.1.mp3"
    sunflower "We, sunflowers, are not just beauty. We’re oil, seeds, food for people and birds."

    voice "audio/voice/3.51.2.mp3"
    sunflower "If the Sun gives too much, we burn out. If storms block the rains, the ground turns dry. The harvest drops, and the farmers get sad."
    menu:
        sunflower "If the Sun gives too much, we burn out. If storms block the rains, the ground turns dry. The harvest drops, and the farmers get sad."
        "But the farmer can do something, right?":
            jump sunflower_ans9

label sunflower_ans9:
    show sunflower leaf at right
    voice "audio/voice/3.53.1.mp3"
    sunflower "He can—water, fertilize."

    voice "audio/voice/3.53.2.mp3"
    sunflower "But if the sky and the land burn, he’s powerless. Space is stronger than the plow."

    menu:
        sunflower "But if the sky and the land burn, he’s powerless. Space is stronger than the plow."
        "So, space decides everything?":
            jump sunflower_ans10

label sunflower_ans10:
    show sunflower normal at right
    voice "audio/voice/3.55.mp3"
    sunflower "Hey, not everything! People have power too. But they should remember that it’s not just rain and wind—solar storms affect their bread as well."

    menu:
        sunflower "Hey, not everything! People have power too. But they should remember that it’s not just rain and wind—solar storms affect their bread as well."
        "You’ve told me a lot. So even your life depends on the storms on the Sun.":
            jump sunflower_rep1

label sunflower_rep1:
    show sunflower leaf at right
    voice "audio/voice/3.45.1.mp3"
    sunflower "Yes, mine too, and your bread, and your butter on the table. If you want to know more—talk to the farmer."

    voice "audio/voice/3.45.2.mp3"
    sunflower "He knows how cosmic weather hits his crops directly."
    menu:
        sunflower "He knows how cosmic weather hits his crops directly."
        "Then I’ll go visit him.":
            jump sunflower_rep2

label sunflower_rep2:
    show sunflower smiling at right
    voice "audio/voice/3.47.mp3"
    sunflower "Give him my regards! And may your path always be lit by the right rays."
    stop music
    jump chapter4_dialog