# Define the character
define astro = Character("Астронавт", color="#000", who_style = "name_text")
define father = Character("Батько", color = '#000', who_style = "name_text")
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
    astro "Хм. Ще один супутник… Знову потрібно перевірити сенсори."

    jump chapter1_dialog  # move to the main dialog

# Chapter 1 dialog
label chapter1_dialog:
    show astro thinking at astro_right
    voice "audio/voice/1.2.2.mp3"
    astro "Знаєте, цікаво: мій батько теж літав у космос. Але тоді ніхто серйозно не говорив про погоду в ньому."

    voice "audio/voice/1.2.3.mp3"
    astro "Сонячні бурі здавались рідкістю, дрібницею. Чимось, про що пишуть у журналах, але не думають щодня."
    menu:

        astro "Сонячні бурі здавались рідкістю, дрібницею. Чимось, про що пишуть у журналах, але не думають щодня."
        "Продовжити слухати астронавта":
            jump astro_ans1

        "А що казав твій батько?":
            jump father_ans

# After choices
label astro_ans1:
    show astro smiling at astro_right
    voice "audio/voice/1.4.1.mp3"
    astro "Сонце завжди було і лишається головним гравцем у нашому житті, хоча це й звучить очевидно (ну, хіба ви не маєте IQ пенька)."

    voice "audio/voice/1.4.2.mp3"
    astro "Але якщо копнути глибше, то вплив Сонця далеко не обмежується теплом і світлом."

    voice "audio/voice/1.4.3.mp3"
    astro "За останні десятиліття науковці все частіше фіксують зростання сонячної та геомагнітної активності."

    voice "audio/voice/1.4.4.mp3"
    astro "Це проявляється у різних формах: кількість сонячних спалахів помітно збільшилась, усе частіше відбуваються масивні викиди корональної маси, посилився потік сонячного вітру."

    voice "audio/voice/1.4.5"
    astro "А ще цікаво, що з цим пов’язані й варіації галактичного космічного випромінювання, які напряму залежать від циклічності сонячної активності."


    menu:
        astro "А ще цікаво, що з цим пов’язані й варіації галактичного космічного випромінювання, які напряму залежать від циклічності сонячної активності."
        "Звучить цікаво! Розкажи детальніше.":
            jump astro_ans2

        "Ой, а Ви там згадували свого батька, він так само нудотину ніс?":
            jump father_ans

label father_ans:
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

    scene bg space with fade

    show astro rolling_eyes at astro_right
    voice "audio/voice/1.30.1.mp3"
    astro "Але що ж Вам цікаві лише історії мого батька, а я Вам не любий, то відповідайте на мої запитання!"

    voice "audio/voice/1.30.2.mp3"
    astro "Тільки в ефірі з’явилась, а вже мене дратує!"
    menu:
        astro "Тільки в ефірі з’явилась, а вже мене дратує!"
        "Ой, краще я все ж таки послухаю Вас. Вибачте":
            voice "audio/voice/1.28.mp3"
            astro "От і чудово!"
            jump astro_ans2

        "Без проблем! Я слухаю Ваші запитання.":
            jump astro_q1

label astro_q1:
    show astro thinking at astro_right
    voice "audio/voice/1.32.1.mp3"
    astro "Гаразд! Слухайте!"
    voice "audio/voice/1.32.2.mp3"
    astro "Що таке 11-річний цикл Сонця?"
    menu:

        astro "Що таке 11-річний цикл Сонця?"
        "Це час, за який Сонце обертається навколо власної осі.":
            jump astro_rep1

        "Це довготривалий цикл сонячної активності тривалістю близько століття.":
            jump astro_q2

label astro_rep1:
    show astro rolling_eyes at astro_right
    voice "audio/voice/1.34.mp3"
    astro "Дурість, а не відповідь! Тепер же я Вам цікавий!"
    jump astro_ans3

label astro_q2:
    show astro smiling at astro_right
    voice "audio/voice/1.36.mp3"
    astro "Гаразд, все ж таки клепка є. Продовжимо! Яка особливість 25-го сонячного циклу?"
    menu:
        astro "Гаразд, все ж таки клепка є. Продовжимо! Яка особливість 25-го сонячного циклу?"
        "Він триває довше за всі попередні відомі цикли.":
            jump astro_rep2

        "Його максимум виявився активнішим, ніж очікували вчені.":
            jump astro_q3

label astro_rep2:
    show astro rolling_eyes at astro_right
    voice "audio/voice/1.38.mp3"
    astro "Все ж таки я помилився! Слухайте розумну людину."
    jump astro_ans5

label astro_q3:
    show astro with_hands at astro_right
    voice "audio/voice/1.40.1.mp3"
    astro "Ай, молодца!"

    show astro thinking at astro_right
    voice "audio/voice/1.40.2.mp3"
    astro "Тоді останнє питання для тебе проблемою не буде. Що кажуть вчені про вплив положення Сонячної системи в галактиці?"
    menu:

        astro "Тоді останнє питання для тебе проблемою не буде. Що кажуть вчені про вплив положення Сонячної системи в галактиці?"
        "Доведено, що положення у галактиці напряму визначає клімат на Землі.":
            jump astro_rep4

        "Це лише гіпотеза, яка поки не має достатньо доказів.":
            jump astro_q4

label astro_rep4:
    show astro with_hands at astro_right
    voice "audio/voice/1.42.1.mp3"
    astro "Ох, втомились Ви видно. На жаль, неправильно."

    show astro thinking at astro_right
    voice "audio/voice/1.42.2.mp3"
    astro "На фоні сонячних змін Земля додатково піддається впливу галактичного космічного випромінювання, інтенсивність якого також залежить від рівня сонячної активності: під час мінімумів воно зростає, а під час максимумів зменшується."

    show astro smiling at astro_right
    voice "audio/voice/1.42.3.mp3"
    astro "Деякі вчені також розглядають можливість впливу положення Сонячної системи у галактиці, але це поки що гіпотези."

    jump astro_rep3

label astro_q4:
    show astro with_hands at astro_right
    voice "audio/voice/1.44.mp3"
    astro "Розумно!"

    jump astro_rep3

label astro_ans2:
    show astro with_hands at astro_right
    voice "audio/voice/1.6.mp3"
    astro "Взагалі зростання сонячної та геомагнітної активності відбувається з багатьох причин, які зараз досліджуються."
    menu:

        astro "Взагалі зростання сонячної та геомагнітної активності відбувається з багатьох причин, які зараз досліджуються."
        "Справді? А можеш і мені показати ці дослідження, це не конфіденційно?":
            jump astro_ans3

label astro_ans3:
    show astro normal at astro_right
    voice "audio/voice/1.8.1.mp3"
    astro "Звичайно!"

    voice "audio/voice/1.8.2.mp3"
    astro "Одною з причин є внутрішні процеси сонця. Наприклад, 11 річний цикл."

    voice "audio/voice/1.8.3.mp3"
    menu:

        astro "Знаєте, що це таке?"
        "Так, знаю. Я слухаю далі, про ваші дослідження!":
            jump astro_ans4

        "Ні, не знаю. Поясни, буль ласка.":
            jump astro_expl

label astro_expl:
    show astro thinking at astro_right
    voice "audio/voice/1.24.1.mp3"
    astro "11-річний сонячний цикл (цикл Швабе) визначає періоди підвищеної та зниженої активності. У фазі максимуму активність зростає, спостерігається більше плям і спалахів Сонця."

    show astro normal at astro_right
    voice "audio/voice/1.24.2.mp3"
    astro "Тепер Ви зрозуміли ж?"

    jump astro_ans4

label astro_ans4:
    show astro smiling at astro_right
    voice "audio/voice/1.10.1.mp3"
    astro "Чудово! Тоді слухайте."

    show astro with_hands at astro_right
    voice "audio/voice/1.10.2.mp3"
    astro "Крім 11-річного циклу існують довші періоди (наприклад, цикл Гляйсберга — ~80–100 років)."
    menu:

        astro "Крім 11-річного циклу існують довші періоди (наприклад, цикл Гляйсберга — ~80–100 років)."
        "Чи буває таке, що цикли накладаються?":
            jump astro_ans5

label astro_ans5:
    show astro normal at astro_right
    voice "audio/voice/1.12.1.mp3"
    astro "Коли цикли «накладаються», вони викликають особливо сильні максимуми активності."

    show astro thinking at astro_right
    voice "audio/voice/1.12.2.mp3"
    astro "До речі, саме от нещодавно Сонце досягло максимуму: 25-го циклу (2024–2026 рр.), який виявився сильнішим, ніж очікувалося."

    show astro with_hands at astro_right
    voice "audio/voice/1.13.mp3"
    astro "Хочеш почути про зовнішні фактори впливу на Землю?"

    menu:

        astro "Хочеш почути про зовнішні фактори впливу на Землю?"
        "Так!":
            jump astro_ans6

        "Ні.":
            jump astro_ans7

label astro_ans6:
    show astro smiling at astro_right
    voice "audio/voice/1.15.1.mp3"
    astro "На фоні сонячних змін Земля додатково піддається впливу галактичного космічного випромінювання, інтенсивність якого також залежить від рівня сонячної активності: під час мінімумів воно зростає, а під час максимумів зменшується."

    show astro thinking at astro_right
    voice "audio/voice/1.15.2.mp3"
    astro "Деякі вчені також розглядають можливість впливу положення Сонячної системи у галактиці, але це поки що гіпотези."

    jump astro_rep3

label astro_ans7:
    show astro rolling_eyes at astro_right
    voice "audio/voice/1.17.mp3"
    astro "Вам же гірше!"

    jump astro_rep3

label astro_rep3:
    show astro thinking at astro_right
    voice "audio/voice/1.18.mp3"
    astro "Що ж Вас занесло сюди?"
    menu:

        astro "Що ж Вас занесло сюди?"
        "Мені завжди був цікавий космос, тому я знайшов вас і хочу побалакати ще з іншими.":
            jump astro_ans8

        "Останнім часом в мене болить голова. Лікар казала, що це все магнітні бурі.":
            jump astro_ans9



label astro_ans8:
    show astro smiling at astro_right
    voice "audio/voice/1.20.1.mp3"
    astro "Чудово!"

    voice "audio/voice/1.20.2.mp3"
    astro "Знаєте, сходи до Лисиці. Вона тобі більше розповість, бо мені вже час. Бувай!"
    stop music fadeout 1.0
    jump chapter2_dialog

label astro_ans9:
    show astro with_hands at astro_right
    voice "audio/voice/1.22.1.mp3"
    astro "Та, то можуть бути магнітні бурі."

    show astro normal at astro_right
    voice "audio/voice/1.22.2.mp3"
    astro "Знаєте, вони впливають не лише на людей, а ще й на тварин."

    voice "audio/voice/1.22.3.mp3"
    astro "Сходи до Лисиці. Вона тобі більше розповість про магнітні бурі та поля і як вони впливають на нас всіх."

    show astro smiling at astro_right
    voice "audio/voice/1.22.4.mp3"
    astro "Мені вже час йти, вдачі!"
    stop music fadeout 1.0
    jump chapter2_dialog




