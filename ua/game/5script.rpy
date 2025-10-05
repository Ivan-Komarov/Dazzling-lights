define astro = Character("Астронавт", color = "#000", who_style = "name_text")
define father = Character("Батько", color = "#000", who_style = "name_text")
define child = Character("Дитина", color = "#000", who_style = "name_text")
define hero = Character("Ви", color = "#000", who_style = "name_text")

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
    astro "Так, ми вже встигли повернутися на Землю. І, знаєш, мені здається, що світ сильно змінився від часів мого батька..."

    menu:
        astro "Так, ми вже встигли повернутися на Землю. І, знаєш, мені здається, що світ сильно змінився від часів мого батька..."
        "Справді? Розкажіть більше про батька!":
            jump father_ans1

        "Давайте на цей раз побалакаємо про майбутнє. О, це твоя дитина?":
            jump child_ans

label father_ans1:
    scene bg kitchen with fade

    show father normal at father_right
    voice "audio/voice/1.26.1.mp3"
    father "О, синку, космос — це не про якісь там бурі. Це про тишу й порожнечу."

    show father hand at father_right
    voice "audio/voice/1.26.2.mp3"
    father "Ти летиш над Землею — а внизу грози, блискавки, океани. А тут — ні краплі дощу, ні подиху вітру."

    show father normal at father_right
    voice "audio/voice/1.26.3.mp3"
    father "Погода в космосі? Ха! Яка ще погода? У нас тут вакуум!"

    menu:
        father "Погода в космосі? Ха! Яка ще погода? У нас тут вакуум!"
        "Астронавте, а в тебе є діти?":
            jump child_ans

label child_ans:
    scene bg final with fade
    show child anxiety at right

    voice "audio/voice/5.6.1.mp3"
    child "Ми вже бачимо проблеми, які чекають на нас: сонячна радіація, нестабільні врожаї, нові виклики для здоров’я людей."

    voice "audio/voice/5.6.2.mp3"
    show child smile at right
    child "Але ми можемо діяти."

    menu:
        child "Але ми можемо діяти."
        "Захист від сонячної радіації?":
            jump child_ans1
        "Як нам зберігти врожаї?":
            jump child_ans2

label child_ans1:
    show child smile at right
    voice "audio/voice/5.9.1.mp3"
    child "Ми створюємо нові супутники і щити для мереж та людей."

    show child normal at right
    voice "audio/voice/5.9.2.mp3"
    child "Вони допомагають передбачати та зменшувати наслідки сонячних бурь."

    menu:
        child "Вони допомагають передбачати та зменшувати наслідки сонячних бурь."
        "А як щодо нових методів лікування і адаптації?":
            jump child_ans3

label child_ans2:
    show child smile at right
    voice "audio/voice/5.11.mp3"
    child "Розумні ферми, сенсори ґрунту та теплиці, що підлаштовуються під сонце, допомагають нам отримувати врожаї навіть у складних умовах."

    menu:
        child "Розумні ферми, сенсори ґрунту та теплиці, що підлаштовуються під сонце, допомагають нам отримувати врожаї навіть у складних умовах."
        "А як щодо нових методів лікування і адаптації?":
            jump child_ans3

label child_ans3:
    show child normal at right
    voice "audio/voice/5.13.1.mp3"
    child "Клініки вже тестують передові методи лікування шкіри, а генетичні технології допомагають людям адаптуватися до ультрафіолету."

    show child smile at right
    voice "audio/voice/5.13.2.mp3"
    child "Бачиш? Це лише перший крок."

    show child normal at right
    voice "audio/voice/5.13.3.mp3"
    child "Якщо люди навчаться правильно захищати себе та використовувати нові методи, ми можемо зменшити шкоду від сонця."

    menu:
        child "Якщо люди навчаться правильно захищати себе та використовувати нові методи, ми можемо зменшити шкоду від сонця."
        "Це безпечно для всіх?":
            jump child_ans4

label child_ans4:
    show child normal at right
    voice "audio/voice/5.15.mp3"
    child "Так, якщо правильно застосовувати технології. Але ми ще вчимося — адаптація триває постійно."

    menu:
        child "Так, якщо правильно застосовувати технології. Але ми ще вчимося — адаптація триває постійно."
        "І ти будеш приймати в цьому всьому участь, цікаво?":
            jump child_ans5

        "Все ж таки, чи можна перемогти хвороби?":
            jump child_ans6

label child_ans5:
    show child smile at right
    voice "audio/voice/5.17.mp3"
    child "Ага! Такі, як мій батько працюють над тим, щоб наступні покоління народжувалися здоровими і знали, як адаптуватися до сонця та космічної погоди."
    jump anim

label child_ans6:
    show child smile at right
    voice "audio/voice/5.19.mp3"
    child "Так, правильна дієта, вітаміни, захисні засоби та нові технології разом можуть мінімізувати ризики."
    jump anim

label anim:
    window hide
    scene black
    show end_scene
    $ renpy.pause(17, hard=True)
    hide end_scene with fade
    return