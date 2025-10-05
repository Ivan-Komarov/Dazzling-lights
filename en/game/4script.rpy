define farmer = Character("Farmer", color="#000", who_style = "name_text")
define doctor = Character("Doctor", color = '#000', who_style = "name_text")
define scientist = Character("Scientist", color = '#000', who_style = "name_text")
define hero = Character("You", color = '#000', who_style = "name_text")
define nurse = Character("Nurse", color = '#000', who_style = "name_text")

define arm_left = Position(yalign = 1)

image bg sunb = "images/bg/sunb.png"
image bg lab = "images/bg/lab.png"
image bg hospital = "images/bg/hospital.png"
image bg hospital1 = "images/bg/hospital1.png"
image bg hospital2 = "images/bg/hospital2.png"
image bg farm = "images/bg/farmm.png"
image bg farmer_field = "images/bg/farmer_field.png"
image bg farmer_close = "images/bg/farmer_close.png"
image bg b9 = "images/bg/b9.png"
image farmer normal = "images/characters/4farmer/farmer_normal.png"
image farmer tired = "images/characters/4farmer/farmer_tired.png"
image farmer laughs = "images/characters/4farmer/farmer_laughs.png"
image doctor normal = "images/characters/4doctor/doctor_normal.png"
image doctor thinking = "images/characters/4doctor/doctor_thinking.png"
image nurse = "images/characters/4nurse/nurse.png"
image arm30 = "images/characters/4arm/arm30.png"
image arm31 = "images/characters/4arm/arm31.png"
image arm34 = "images/characters/4arm/arm34.png"
image arm35 = "images/characters/4arm/arm35.png"
image arm37 = "images/characters/4arm/arm37.png"
image arm38 = "images/characters/4arm/arm38.png"
image arm38 = "images/characters/4arm/arm38.png"
image scientist finger = "images/characters/4scientist/scientist_finger_raised.png"
image scientist normal = "images/characters/4scientist/scientist_normal.png"
image scientist hand = "images/characters/4scientist/scientist_raised_hand.png"
image scientist thinking = "images/characters/4scientist/scientist_thinking.png"
image scientist book = "images/characters/4scientist/scientist_with_book.png"

define music_sc = "audio/music/scientist.mp3"
define music_doc = "audio/music/doctor.mp3"
define music_farm = "audio/music/farmer.mp3"

style quick_button_text:
    font "gui/font/Tektur-Regular.ttf"
    size 25
    color "#FFFFFF"
    hover_color "#FFCC00"

label chapter4_dialog:
    play music music_farm volume 0.5
    scene bg sunb with fade
    show farmer tired at left
    voice "audio/voice/4.1.1.mp3"
    farmer "Who’s wandering through my field? You’ll trample all the crops!"
    voice "audio/voice/4.1.2.mp3"
    farmer "Sss-sss-sss! Oh, not even a kid after the corn…"

    scene bg farmer_field with fade
    show farmer normal at left
    voice "audio/voice/4.1.3.mp3"
    farmer "A traveler? Well, since you’re here, sit down. What do you want to know?"

    hero "The sunflower said you know a lot about crops and how they depend on the weather"

    hero "I’m looking for an answer: how do the sky and space affect the Earth and your work?"

    show farmer laughs at left
    voice "audio/voice/4.3.1.mp3"
    farmer "Oh, another seeker of wisdom? Ha! You’d be better off picking up a hoe than listening to nonsense about space…"

    scene bg farm with fade
    show farmer normal at left
    voice "audio/voice/4.3.2.mp3"
    farmer "But alright, sit down, let’s talk."
    menu:
        farmer "But alright, sit down, let’s talk."
        "I heard that the Sun affects the harvest. Is that true?":
            jump farmer_ans1

        "And what about the Earth—how does space affect it?":
            jump farmer_ans2

label farmer_ans1:
    scene bg farmer_close with fade
    show farmer tired at left
    voice "audio/voice/4.5.1.mp3"
    farmer "It’s true, and how! Last year, my wheat stood tall like soldiers in formation."
    voice "audio/voice/4.5.2.mp3"
    farmer "Then the solar flares came—heat and dry wind. I thought I’d be harvesting chaff, not grain."

    show farmer laughs at left
    voice "audio/voice/4.5.3.mp3"
    farmer "Space! Ha! As if I’d signed a contract with it."
    menu:
        farmer "Space! Ha! As if I’d signed a contract with it."
        "Do trees feel space too?":
            jump farmer_ans3

label farmer_ans2:
    scene bg farmer_close with fade
    show farmer laughs at left
    voice "audio/voice/4.7.1.mp3"
    farmer "The Earth is like, ugh, an old sack: it cracks from the heat, swells from the rains."
    voice "audio/voice/4.7.2.mp3"
    farmer "Last summer my chickens had to learn to swim—there was so much water. You say magnetic storms? I say—space is teasing us again."
    menu:
        farmer "Last summer my chickens had to learn to swim—there was so much water. You say magnetic storms? I say—space is teasing us again."
        "Do you feel the effects of cosmic radiation on field ecosystems?":
            jump farmer_ans5

label farmer_ans3:
    show farmer normal at left
    voice "audio/voice/4.9.1.mp3"
    farmer "Haven’t you met the oak? But it’s true."

    show farmer laughs at left
    voice "audio/voice/4.9.2.mp3"
    farmer "Young apple trees wither as if they’re afraid of the Sun. The old ones still hold on, but the harvest—what a joke."
    voice "audio/voice/4.9.3.mp3"
    farmer "Apples smaller than a chicken egg! Either frost or that cursed Sun."
    menu:
        farmer "Apples smaller than a chicken egg! Either frost or that cursed Sun."
        "Grandpa, is it true that solar storms can affect GPS systems in tractors?":
            jump farmer_anss

label farmer_ans5:
    show farmer tired at left
    voice "audio/voice/4.11.1.mp3"
    farmer "Eco… what?"

    show farmer laughs at left
    voice "audio/voice/4.11.2.mp3"
    farmer "Ha! Oh, child, I’m an old fool—I can’t even pronounce such words."
    voice "audio/voice/4.11.3.mp3"
    farmer "I know one thing: if the sun scorches, the crops are gone. If the rain floods, the crops are gone too. And that’s all the “science” you need!"
    menu:
        farmer "I know one thing: if the sun scorches, the crops are gone. If the rain floods, the crops are gone too. And that’s all the “science” you need!"
        "Grandpa, is it true that solar storms can affect GPS systems in tractors?":
            jump farmer_anss

label farmer_anss:
    show farmer normal at left
    voice "audio/voice/4.13.1.mp3"
    farmer "Oh, science-schmience… Look, I’ve got a GPS in my tractor."

    show farmer laughs at left
    voice "audio/voice/4.13.2.mp3"
    farmer "When the sun throws one of its storms, it tells me I’m plowing a field somewhere in the Black Sea!"

    show farmer normal at left
    voice "audio/voice/4.13.3.mp3"
    farmer "So I know without any books: sometimes space messes with these gadgets so much that it’s better to measure the land using the old stakes."
    menu:
        farmer "So I know without any books: sometimes space messes with these gadgets so much that it’s better to measure the land using the old stakes."
        "Perhaps...":
            jump farmer_ans6

label farmer_ans6:
    show farmer tired at left
    voice "audio/voice/4.15.1.mp3"
    farmer "Alright, wrap it up already, or I'll die from this heat! "
    voice "audio/voice/4.15.2.mp3"
    farmer "And you know what, Aunt Lyuba can tell you all about your smart questions - our doctor lady, send her my regards. "

    show farmer laughs at left
    voice "audio/voice/4.15.3.mp3"
    farmer "Now shoo, get out of here!"
    menu:
        farmer "Now shoo, get out of here!"
        "But where should I even go?":
            jump farmer_ans7
label farmer_ans7:
    show farmer tired at left
    voice "audio/voice/4.17.1.mp3"
    farmer "Why are you loading up my old head with this? Just go down the regular road, and in about an hour you'll get to the town. "
    voice "audio/voice/4.17.2.mp3"
    farmer "Kids these days, can't even make it to town on their own, pfft!"

    hide farmer
    scene bg farmer_close with fade
    scene bg b9 with fade
    scene bg hospital2 with fade
    hero "Excuse me? Could you tell me where Aunt Lyuba is around here? The therapist, family doctor"
    jump nurse_ans

label nurse_ans:
    show nurse at right
    voice "audio/voice/4.19.mp3"
    nurse "Something with your skin? Down the hallway and to the right, room 103."

    scene bg hospital with fade

    hero "I'm curious to hear about the sun's effect on human skin."
    jump doctor_ans1

label doctor_ans1:
    play music music_doc volume 0.5
    show doctor normal at right
    voice "audio/voice/4.21.mp3"
    doctor "Come in, come in. What's bothering you?"
    menu:
        doctor "Come in, come in. What's bothering you?"
        "I'm curious to hear about the sun's effect on human skin.":
            jump doctor_ans2

label doctor_ans2:
    scene bg hospital1 with fade
    show doctor thinking at right
    voice "audio/voice/4.23.1.mp3"
    doctor "You know, I’m already a bit tired today."

    show doctor normal at right
    voice "audio/voice/4.23.2.mp3"
    doctor "There are plenty of patients, and space weather also makes itself felt—during magnetic storms, people often complain about headaches, skin problems, or just feeling exhausted."
    voice "audio/voice/4.23.3.mp3"
    doctor "Maybe you’d like to play a little game and see it all for yourself?"
    menu:
        doctor "Maybe you’d like to play a little game and see it all for yourself?"
        "We already played a game like that with a fox and a bird... Let's do something more ordinary.":
            jump doctor_ans3

        "You know what, a game isn't such a bad idea.":
            jump doctor_q1

label doctor_ans3:
    voice "audio/voice/4.25.mp3"
    doctor "Fair enough, but that's gonna be pricier!"
    menu:
        doctor "Fair enough, but that's gonna be pricier!"
        "I only have apples from the farmer...":
            jump doctor_ans4

label doctor_ans4:
    voice "audio/voice/4.29.mp3"
    doctor "Then grab a sack on your shoulder and off to get water! I already don't know what to do with those apples from the old guy."
    menu:
        doctor "Then grab a sack on your shoulder and off to get water! I already don't know what to do with those apples from the old guy."
        "You know what, a game isn't such a bad idea.":
                jump doctor_q1

label doctor_scene:
    $ answer = 0   # initialize score
    jump doctor_q1

label doctor_q1:
    show doctor thinking at right
    show arm30 at arm_left
    voice "audio/voice/4.30.1.mp3"
    doctor "Look, the skin is red, noticeably dry, and the person works in the garden all the time."

    show doctor normal at right
    voice "audio/voice/4.30.2.mp3"
    doctor "What should we do first?"
    menu:
        doctor "What should we do first?"
        "Apply SPF50 sunscreen.":
            show arm31 at arm_left
            $ answer += 1
            jump doctor_q2

        "Keep the skin uncovered since sunlight is good for you.":
            show arm32 at arm_left
            $ answer -= 1
            jump doctor_q2

label doctor_q2:
    voice "audio/voice/4.33.mp3"
    doctor "Right now, it’s important to restore your skin from the inside. What will you choose?"
    menu:
        doctor "Right now, it’s important to restore your skin from the inside. What will you choose?"
        "Drink energy drinks, eat lots of sweets and fast food.":
            show arm34 at arm_left
            $ answer -= 1
            jump doctor_q3

        "Drink water, take vitamins C and E, eat more fruits and vegetables.":
            show arm35 at arm_left
            $ answer += 1
            jump doctor_q3

label doctor_q3:
    voice "audio/voice/4.36.mp3"
    doctor "One more thing—sleep and rest. What do we recommend?"
    menu:
        doctor "One more thing—sleep and rest. What do we recommend?"
        "Work in the sun all day, but stay clothed.":
            $ answer -= 1
            jump end
        "Go to bed on time, avoid the peak midday sun.":
            $ answer += 1
            jump end
    label end:
        if answer >= 3:
            show arm38 at arm_left
            voice "audio/voice/4.41.mp3"
            doctor "You’re doing great! Take care of your skin!"
            menu:
                doctor "You’re doing great! Take care of your skin!"
                "Thank you! I enjoy chatting with you, but I have to run off to the astronaut now.":
                    voice "audio/voice/4.42.1.mp3"
                    doctor "Wait!"
                    voice "audio/voice/4.42.2.mp3"
                    doctor "Stop by my scientist friend first—she lives downtown and will tell you even more interesting stuff."
                    jump scientist_ans1

        else:
            show arm37 at arm_left
            voice "audio/voice/4.39.mp3"
            doctor "Here you go! Let’s go through it once more."
            $ answer == 0
            jump doctor_q1

label scientist_ans1:
    scene bg lab with fade
    show scientist normal at right
    play music music_sc volume 0.5
    voice "audio/sound/opendador.mp3"
    scientist "Oh, hi! I didn’t hear you knock. Have you been standing there long?"
    voice "audio/voice/4.43.mp3"
    scientist "Oh, hi! I didn’t hear you knock. Have you been standing there long?"
    hero "Well, about 10 minutes for sure. I was starting to think you weren’t home."
    voice "audio/voice/4.45.1.mp3"
    scientist "There are only two places I can be: the lab or here. And while the lab is being renovated, the chances of me being anywhere else are zero. "

    show scientist hand at right
    voice "audio/voice/4.45.2.mp3"
    scientist "Since we’re standing in the hallway anyway, come on in."

    show scientist normal at right
    voice "audio/voice/4.45.3.mp3"
    scientist "So, what do you want to know?"

    menu:
        scientist "So, what do you want to know?"
        "How do solar storms affect technology?":
            jump scientist_ans2

label scientist_ans2:
    show scientist finger at right
    voice "audio/voice/4.47.1.mp3"
    scientist "Look, there are three main areas of impact: satellites, power grids, and communications."

    show scientist hand at right
    voice "audio/voice/4.47.2.mp3"
    scientist "Which one do you want to start with?"
    menu:
        scientist "Which one do you want to start with?"
        "I want to hear about satellites first.":
            jump scientist_ans3

        "I want to start with power grids.":
            jump scientist_ans4

        "Maybe we should start with communications?":
            jump scientist_ans5

label scientist_ans3:
    show scientist normal at right
    voice "audio/voice/4.49.1.mp3"
    scientist "When charged particles from the Sun reach orbit, they hit satellites."

    show scientist hand at right
    voice "audio/voice/4.49.2.mp3"
    scientist "They can damage microchips, cause navigation errors, and sometimes the satellite stops working entirely."

    menu:
        scientist "They can damage microchips, cause navigation errors, and sometimes the satellite stops working entirely."
        "So even the GPS on my phone could stop working?":
            jump scientist_ans6

label scientist_ans6:
    show scientist finger at right
    voice "audio/voice/4.51.mp3"
    scientist "Yes. If satellites lose stability, our maps, ship, and plane navigation become unreliable."

    menu:
        scientist "Yes. If satellites lose stability, our maps, ship, and plane navigation become unreliable."
        "Now tell me about power grids.":
            jump scientist_ans7

label scientist_ans7:
    show scientist book at right
    voice "audio/voice/4.53.1.mp3"
    scientist "Solar storms create strong magnetic fields. They induce currents in long power lines."
    voice "audio/voice/4.53.2.mp3"
    scientist "Transformers can overheat. Power lines can fail. Sometimes whole countries are left without electricity."

    menu:
        scientist "Transformers can overheat. Power lines can fail. Sometimes whole countries are left without electricity."
        "That’s really possible?":
            jump scientist_ans8

label scientist_ans8:
    show scientist normal at right
    voice "audio/voice/4.55.mp3"
    scientist "Yes, in 1989, millions of people in Canada were without power in just a few minutes."

    menu:
        scientist "Yes, in 1989, millions of people in Canada were without power in just a few minutes."
        "That is terrible. What about communications then?":
            jump scientist_ans9

label scientist_ans9:
    show scientist hand at right
    voice "audio/voice/4.57.1.mp3"
    scientist "Radio signals get distorted or disappear completely during storms."

    show scientist finger at right
    voice "audio/voice/4.57.2.mp3"
    scientist "Airplanes can’t communicate with air traffic controllers. Ships lose navigation data. Internet and phone services work intermittently."

    menu:
        scientist "Airplanes can’t communicate with air traffic controllers. Ships lose navigation data. Internet and phone services work intermittently."
        "That’s dangerous for flights, right?":
            jump scientist_ans10

label scientist_ans10:
    show scientist normal at right
    voice "audio/voice/4.59.mp3"
    scientist "Very. That’s why during strong storms, flights can be delayed."

    menu:
        scientist "Very. That’s why during strong storms, flights can be delayed."
        "So a solar storm can leave us without electricity, communication, and even satellites?":
            jump scientist_rep

label scientist_ans4:
    show scientist normal at right
    voice "audio/voice/4.61.1.mp3"
    scientist "Solar storms create strong magnetic fields. They induce currents in long power lines."

    show scientist hand at right
    voice "audio/voice/4.61.2.mp3"
    scientist "Transformers can overheat. Power lines can fail. Sometimes whole countries are left without electricity."

    menu:
        scientist "Transformers can overheat. Power lines can fail. Sometimes whole countries are left without electricity"
        "That’s really possible?":
            jump scientist_ans11

label scientist_ans11:
    show scientist normal at right
    voice "audio/voice/4.63.mp3"
    scientist "Yes, in 1989, millions of people in Canada lost power within just a few minutes."

    menu:
        scientist "Yes, in 1989, millions of people in Canada lost power within just a few minutes."
        "What about satellites then?":
            jump scientist_ans12

label scientist_ans12:
    show scientist normal at right
    voice "audio/voice/4.49.1.mp3"
    scientist "When charged particles from the Sun reach orbit, they hit satellites."

    show scientist hand at right
    voice "audio/voice/4.49.2.mp3"
    scientist "They can damage microchips, cause navigation errors, and sometimes the satellite stops working completely."

    menu:
        scientist "They can damage microchips, cause navigation errors, and sometimes the satellite stops working completely."
        "So even the GPS on my phone could stop working?":
            jump scientist_ans13

label scientist_ans13:
    show scientist finger at right
    voice "audio/voice/4.51.mp3"
    scientist "Yes. If satellites lose stability, our maps and ship and plane navigation become unreliable."

    menu:
        scientist "Yes. If satellites lose stability, our maps and ship and plane navigation become unreliable."
        "That’s awful. Does communication also suffer from solar storms?":
            jump scientist_ans14

label scientist_ans14:
    show scientist normal at right
    voice "audio/voice/4.69.1.mp3"
    scientist "Unfortunately, yes. Radio signals get distorted or disappear completely during storms."

    voice "audio/voice/4.69.2.mp3"
    scientist "Airplanes lose contact with controllers. Ships can’t get navigation data. Internet and phone services work intermittently."

    menu:
        scientist "Airplanes lose contact with controllers. Ships can’t get navigation data. Internet and phone services work intermittently."
        "That’s dangerous for flights, right?":
            jump scientist_ans15

label scientist_ans15:
    show scientist hand at right
    voice "audio/voice/4.59.mp3"
    scientist "Very. That’s why during strong storms, flights can be delayed."
    menu:
        scientist "Very. That’s why during strong storms, flights can be delayed."
        "So a solar storm can leave us without electricity, communication, and even satellites?":
            jump scientist_rep

label scientist_ans5:
    show scientist hand at right
    voice "audio/voice/4.57.1.mp3"
    scientist "Radio signals get distorted or disappear completely during storms."

    show scientist finger at right
    voice "audio/voice/4.57.2.mp3"
    scientist "Airplanes lose contact with controllers. Ships don’t get navigation data. Internet and phone services work intermittently."

    menu:
        scientist "Very. That’s why during strong storms, flights can be delayed."
        "That’s dangerous for flights, right?":
            jump scientist_ans16

label scientist_ans16:
    show scientist hand at right
    voice "audio/voice/4.59.mp3"
    scientist "Very. That’s why during strong storms, flights can be delayed."

    menu:
        scientist "Very. That’s why during strong storms, flights can be delayed."
        "What about satellites then?":
            jump scientist_ans17

label scientist_ans17:
    show scientist normal at right
    voice "audio/voice/4.49.1.mp3"
    scientist "When charged particles from the Sun reach orbit, they hit satellites."

    show scientist hand at right
    voice "audio/voice/4.49.2.mp3"
    scientist "They can damage microchips, cause navigation errors, and sometimes the satellite stops working entirely."

    menu:
        scientist "They can damage microchips, cause navigation errors, and sometimes the satellite stops working entirely."
        "So even GPS on my phone could stop working?":
            jump scientist_ans18

label scientist_ans18:
    show scientist finger at right
    voice "audio/voice/4.51.mp3"
    scientist "Yes. If satellites lose stability, our maps and ship and plane navigation become unreliable."

    menu:
        scientist "Yes. If satellites lose stability, our maps and ship and plane navigation become unreliable."
        "Do power grids also suffer this badly from solar storms?":
            jump scientist_ans19

label scientist_ans19:
    show scientist normal at right
    voice "audio/voice/4.81.1.mp3"
    scientist "Unfortunately, yes. Solar storms create strong magnetic fields. They induce currents in long power lines."

    voice "audio/voice/4.81.2.mp3"
    scientist "Transformers can overheat. Power lines can fail. Sometimes whole countries are left without electricity."

    menu:
        scientist "Transformers can overheat. Power lines can fail. Sometimes whole countries are left without electricity."
        "That’s really possible?":
            jump scientist_ans20

label scientist_ans20:
    show scientist book at right
    voice "audio/voice/4.55.mp3"
    scientist " Yes, in 1989, millions of people in Canada lost power within just a few minutes."
    menu:
        scientist " Yes, in 1989, millions of people in Canada lost power within just a few minutes."
        "So a solar storm can leave us without electricity, communication, and even satellites?":
            jump scientist_rep

label scientist_rep:
    show scientist hand at right
    voice "audio/voice/4.85.mp3"
    scientist "Exactly. Now a question for you: which of these areas is most vulnerable in the first hours after a storm?"

    menu:
        scientist "Exactly. Now a question for you: which of these areas is most vulnerable in the first hours after a storm?"
        "Satellites. They’re in space with no protection, so the hit is immediate.":
            jump scientist_rep1

        "Power grids. They’re all connected, and even a small overload can spread quickly.":
            jump scientist_rep1

        "Communications. If signals disappear, everyone feels it—from pilots to people with phones.":
            jump scientist_rep1

label scientist_rep1:
    show scientist finger at right
    voice "audio/voice/4.89.mp3"
    scientist "Correct. That’s why NASA launches new instruments—to warn us in advance. Want to see how that works?"
    menu:
        scientist "Correct. That’s why NASA launches new instruments—to warn us in advance. Want to see how that works?"
        "OFC!":
            voice "audio/voice/4.91.mp3"
            scientist "Then let’s go to the base—today a rocket is launching that will monitor the Sun."
            stop music
            jump chapter5_dialog
