define farmer = Character("Фермер", color="#000", who_style = "name_text")
define doctor = Character("Лікар", color = '#000', who_style = "name_text")
define scientist = Character("Вчена", color = '#000', who_style = "name_text")
define hero = Character("Ви", color = '#000', who_style = "name_text")
define nurse = Character("Мед-сестра", color = '#000', who_style = "name_text")

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
    farmer "Хто це там ходить по моєму полі? Всі врожаї затопчеш!"
    voice "audio/voice/4.1.2.mp3"
    farmer "Киш-киш-киш! Ай, навіть не хлопчисько по кукурудзу… "

    scene bg farmer_field with fade
    show farmer normal at left
    voice "audio/voice/4.1.3.mp3"
    farmer "Мандрівник? Ну, раз уже прийшов, слухаю. Що тебе цікавить?"

    hero "Соняшник сказав, що Ви багато знаєте про врожаї та їхню залежність від погоди."

    hero "Я шукаю відповідь: як небо й космос впливають на землю і на вашу працю?"

    show farmer laughs at left
    voice "audio/voice/4.3.1.mp3"
    farmer "О, ще один шукач мудрості? Ха! Краще б ти сапку в руки взяв, ніж дурниці про космос слухав…"

    scene bg farm with fade
    show farmer normal at left
    voice "audio/voice/4.3.2.mp3"
    farmer "Але гаразд, сідай, поговоримо."
    menu:
        farmer "Але гаразд, сідай, поговоримо."
        "Чув, що Сонце впливає на врожай. Це правда?":
            jump farmer_ans1

        "А що з землею від космосу?":
            jump farmer_ans2

label farmer_ans1:
    scene bg farmer_close with fade
    show farmer tired at left
    voice "audio/voice/4.5.1.mp3"
    farmer "Правда, ще й яка. От у мене торік пшениця стояла, як солдати в строю."
    voice "audio/voice/4.5.2.mp3"
    farmer "А як сонячні спалахи пішли — спека та суховій. Думав, буду збирати пір’їну, а не зерно."

    show farmer laughs at left
    voice "audio/voice/4.5.3.mp3"
    farmer "Космос! Ха! Наче я з ним контракт підписував."
    menu:
        farmer "Космос! Ха! Наче я з ним контракт підписував."
        "Дерева теж відчувають космос?":
            jump farmer_ans3

label farmer_ans2:
    scene bg farmer_close with fade
    show farmer laughs at left
    voice "audio/voice/4.7.1.mp3"
    farmer "Земля — як, тьху, старий мішок: трісне від спеки, розбухне від дощів."
    voice "audio/voice/4.7.2.mp3"
    farmer "У мене кури минулого літа плавати вчилися, стільки води було. Кажеш, магнітні бурі? Я кажу — знову космос кепкує."
    menu:
        farmer "У мене кури минулого літа плавати вчилися, стільки води було. Кажеш, магнітні бурі? Я кажу — знову космос кепкує."
        "А чи відчуваєш ти вплив космічної радіації на екосистема полів?":
            jump farmer_ans5

label farmer_ans3:
    show farmer normal at left
    voice "audio/voice/4.9.1.mp3"
    farmer "А ти чого, дуба не зустрічав? Але правда."

    show farmer laughs at left
    voice "audio/voice/4.9.2.mp3"
    farmer "Молоді яблуні сохнуть, немов сонця бояться. Старі ще тримаються, але врожай — сміх один."
    voice "audio/voice/4.9.3.mp3"
    farmer "Яблуко менше за куряче яйце! То заморозки, то сонце кляте."
    menu:
        farmer "Яблуко менше за куряче яйце! То заморозки, то сонце кляте."
        "Діду, а правда, що космічні бурі можуть впливати на GPS-системи у тракторах?":
            jump farmer_anss

label farmer_ans5:
    show farmer tired at left
    voice "audio/voice/4.11.1.mp3"
    farmer "Еко... що?"

    show farmer laughs at left
    voice "audio/voice/4.11.2.mp3"
    farmer "Ха! Ой, дитя, я старий дурний, таких слів навіть вимовити не зможу."
    voice "audio/voice/4.11.3.mp3"
    farmer "Я знаю одне: якщо сонце пече — то врожай пропав. Якщо дощ заливає — то теж пропав. От тобі й вся наука!"
    menu:
        farmer "Я знаю одне: якщо сонце пече — то врожай пропав. Якщо дощ заливає — то теж пропав. От тобі й вся наука!"
        "Діду, а правда, що космічні бурі можуть впливати на GPS-системи у тракторах?":
            jump farmer_anss

label farmer_anss:
    show farmer normal at left
    voice "audio/voice/4.13.1.mp3"
    farmer "Та яка там космічна наука… От дивись, у мене навігатор в тракторі."

    show farmer laughs at left
    voice "audio/voice/4.13.2.mp3"
    farmer "Як сонце тих своїх бур накидає – так він мені показує, шо я орю поле десь у Чорному морі!"

    show farmer normal at left
    voice "audio/voice/4.13.3.mp3"
    farmer "То я й без книжок знаю: космос нам часом таку маячню в ті прилади жене, шо краще вже по старих кілочках землю міряти."
    menu:
        farmer "То я й без книжок знаю: космос нам часом таку маячню в ті прилади жене, шо краще вже по старих кілочках землю міряти."
        "Можливо...":
            jump farmer_ans6

label farmer_ans6:
    show farmer tired at left
    voice "audio/voice/4.15.1.mp3"
    farmer "Давай вже закругляйся, бо я від спеки помру!"
    voice "audio/voice/4.15.2.mp3"
    farmer "І знаєш, от тобі на всі твої розумні запитання може тьоть Люба розкаже, лікарка наша,  передавай їй вітання."

    show farmer laughs at left
    voice "audio/voice/4.15.3.mp3"
    farmer "А тепер киш звідси!"
    menu:
        farmer "А тепер киш звідси!"
        "А куди йти то хоч?":
            jump farmer_ans7
label farmer_ans7:
    show farmer tired at left
    voice "audio/voice/4.17.1.mp3"
    farmer "Що ж ти стару мою голову вантажиш, по дорозі піди звичайній, то там через годинку і до містечка дійдеш."
    voice "audio/voice/4.17.2.mp3"
    farmer "От молодь пішла, навіть дійти до міста самі не можуть, тьху вас!"

    hide farmer
    scene bg farmer_close with fade
    scene bg b9 with fade
    scene bg hospital2 with fade
    hero "Вибачте? А Ви не підкажете, де тут тітка Люба? Терапевт, сімейний лікар."
    jump nurse_ans

label nurse_ans:
    show nurse at right
    voice "audio/voice/4.19.mp3"
    nurse "Щось зі шкірою? По коридору і праворуч буде 103 кабінет."

    scene bg hospital with fade

    hero "Вибачте? Я з приводу шкіри."
    jump doctor_ans1

label doctor_ans1:
    play music music_doc volume 0.5
    show doctor normal at right
    voice "audio/voice/4.21.mp3"
    doctor "Заходьте, заходьте. Що Вас турбує?"
    menu:
        doctor "Заходьте, заходьте. Що Вас турбує?"
        "Мені цікаво послухати про вплив сонця на шкіру людини.":
            jump doctor_ans2

label doctor_ans2:
    scene bg hospital1 with fade
    show doctor thinking at right
    voice "audio/voice/4.23.1.mp3"
    doctor "Знаєте, я вже трохи втомилась за сьогодні."

    show doctor normal at right
    voice "audio/voice/4.23.2.mp3"
    doctor "Пацієнтів вистачає, та й космічна погода також дає про себе знати - під час магнітних бур люди нерідко скаржаться на головний біль, проблемну шкіру або ж виснаженісь."
    voice "audio/voice/4.23.3.mp3"
    doctor "Можливо, хочете зіграти в гру та самі все побачити?"
    menu:
        doctor "Можливо, хочете зіграти в гру та самі все побачити?"
        "Вже так грали в гру з лисицею та пташкою... Давайте щось звичайніше.":
            jump doctor_ans3

        "Все ж таки гра непогана ідея.":
            jump doctor_q1

label doctor_ans3:
    voice "audio/voice/4.25.mp3"
    doctor "Гаразд, але то буде дорожче!"
    menu:
        doctor "Гаразд, але то буде дорожче!"
        "В мене є тільки яблука від фермера...":
            jump doctor_ans4

label doctor_ans4:
    voice "audio/voice/4.29.mp3"
    doctor "Тоді броцак на плече і за водою! Я вже не знаю що робити з тими яблуками від старого."
    menu:
        doctor "Тоді броцак на плече і за водою! Я вже не знаю що робити з тими яблуками від старого."
        "Все ж таки гра непогана ідея.":
                jump doctor_q1

label doctor_scene:
    $ answer = 0   # initialize score
    jump doctor_q1

label doctor_q1:
    show doctor thinking at right
    show arm30 at arm_left
    voice "audio/voice/4.30.1.mp3"
    doctor "Дивіться, шкіра червоніє, помітно пересушена, а людина постійно на городі працює."

    show doctor normal at right
    voice "audio/voice/4.30.2.mp3"
    doctor "Що ми зробимо в першу чергу?"
    menu:
        doctor "Що ми зробимо в першу чергу?"
        "Нанести сонцезахисний крем SPF50":
            show arm31 at arm_left
            $ answer += 1
            jump doctor_q2

        "Залишити шкіру відкритою, бо сонячні промені корисні.":
            show arm32 at arm_left
            $ answer -= 1
            jump doctor_q2

label doctor_q2:
    voice "audio/voice/4.33.mp3"
    doctor "Зараз важливо відновити шкіру зсередини. Що обереш?"
    menu:
        doctor "Зараз важливо відновити шкіру зсередини. Що обереш?"
        "Пити енергетики, їсти багато солодкого та фастфуд.":
            show arm34 at arm_left
            $ answer -= 1
            jump doctor_q3

        "Пити воду, вітаміни C і E, їсти більше фруктів і овочів.":
            show arm35 at arm_left
            $ answer += 1
            jump doctor_q3

label doctor_q3:
    voice "audio/voice/4.36.mp3"
    doctor "Ще одна річ — сон і відпочинок. Що радимо?"
    menu:
        doctor "Ще одна річ — сон і відпочинок. Що радимо?"
        "Працювати на сонці весь день, але вдягненим.":
            $ answer -= 1
            jump end
        "Лягати спати вчасно, уникати пік денного сонця.":
            $ answer += 1
            jump end
    label end:
        if answer >= 3:
            show arm38 at arm_left
            voice "audio/voice/4.41.mp3"
            doctor "А Ви молодець! Слідкуйте за своєю шкірою!"
            menu:
                doctor "А Ви молодець! Слідкуйте за своєю шкірою!"
                "Дякую! Мені подобається з Вами балакати, але мушу вже тікати до астронавта.":
                    voice "audio/voice/4.42.1.mp3"
                    doctor "Заждіть!"
                    voice "audio/voice/4.42.2.mp3"
                    doctor "Попередньо зайдіть до моєї подруги-вченої, вона живе в центрі і розповість Вам ще багато цікавого."
                    jump scientist_ans1

        else:
            show arm37 at arm_left
            voice "audio/voice/4.39.mp3"
            doctor "От тобі на! Пройдемо ще раз."
            $ answer == 0
            jump doctor_q1

label scientist_ans1:
    scene bg lab with fade
    show scientist normal at right
    play music music_sc volume 0.5
    voice "audio/sound/opendador.mp3"
    scientist "Ой, привіт, я не почула, як ти стукав. Ти вже довго тут стоїш?"
    voice "audio/voice/4.43.mp3"
    scientist "Ой, привіт, я не почула, як ти стукав. Ти вже довго тут стоїш?"
    hero "Ну, хвилин з 10 точно, я вже думала, що тебе немає вдома."
    voice "audio/voice/4.45.1.mp3"
    scientist "Є лише два місця, де я можу бути: лабораторія та тут. А доки лабораторію ремонтують, то шанси, що я буду деінде - рівні нулю."

    show scientist hand at right
    voice "audio/voice/4.45.2.mp3"
    scientist "Що ж ми в проході стоїмо, заходь."

    show scientist normal at right
    voice "audio/voice/4.45.3.mp3"
    scientist "То що ти хочеш дізнатися?"

    menu:
        scientist "То що ти хочеш дізнатися?"
        "Як впливають сонячні бурі на техніку?":
            jump scientist_ans2

label scientist_ans2:
    show scientist finger at right
    voice "audio/voice/4.47.1.mp3"
    scientist "Дивись. Є три основні напрями впливу: супутники, електромережі, зв’язок."

    show scientist hand at right
    voice "audio/voice/4.47.2.mp3"
    scientist "З чого ти хочеш почати?"
    menu:
        scientist "З чого ти хочеш почати?"
        "Хочу спершу почути про супутники.":
            jump scientist_ans3

        "Хочу почати з електромереж":
            jump scientist_ans4

        "Може спершу поговоримо про зв’язок?":
            jump scientist_ans5

label scientist_ans3:
    show scientist normal at right
    voice "audio/voice/4.49.1.mp3"
    scientist "Коли заряджені частинки від Сонця досягають орбіти, вони вдаряють по супутниках."

    show scientist hand at right
    voice "audio/voice/4.49.2.mp3"
    scientist "Вони пошкоджують мікросхеми, викликають збої в навігації, іноді супутник виходить з ладу повністю."

    menu:
        scientist "Вони пошкоджують мікросхеми, викликають збої в навігації, іноді супутник виходить з ладу повністю."
        "Тобто навіть GPS у телефоні може перестати працювати?":
            jump scientist_ans6

label scientist_ans6:
    show scientist finger at right
    voice "audio/voice/4.51.mp3"
    scientist "Так. Якщо супутники втрачають стабільність, наші карти, навігація кораблів і літаків стають ненадійними."

    menu:
        scientist "Так. Якщо супутники втрачають стабільність, наші карти, навігація кораблів і літаків стають ненадійними."
        "Розкажи тепер мені про електромережі.":
            jump scientist_ans7

label scientist_ans7:
    show scientist book at right
    voice "audio/voice/4.53.1.mp3"
    scientist "Сонячні бурі створюють потужні магнітні поля. Вони наводять струм у довгих лініях електропередач."
    voice "audio/voice/4.53.2.mp3"
    scientist "Трансформатори перегріваються. Лінії електропередач можуть вийти з ладу. Іноді цілі країни залишаються без світла."

    menu:
        scientist "Трансформатори перегріваються. Лінії електропередач можуть вийти з ладу. Іноді цілі країни залишаються без світла."
        "Це справді можливо?":
            jump scientist_ans8

label scientist_ans8:
    show scientist normal at right
    voice "audio/voice/4.55.mp3"
    scientist "Так, у 1989 році в Канаді за кілька хвилин без електрики залишилися мільйони людей."

    menu:
        scientist "Так, у 1989 році в Канаді за кілька хвилин без електрики залишилися мільйони людей."
        "Який жах. Що ж тоді відбувається зі зв’язком?":
            jump scientist_ans9

label scientist_ans9:
    show scientist hand at right
    voice "audio/voice/4.57.1.mp3"
    scientist "Радіосигнали під час бурь спотворюються або зовсім зникають."

    show scientist finger at right
    voice "audio/voice/4.57.2.mp3"
    scientist "Авіація втрачає можливість зв’язку з диспетчерами. Морські судна не отримують навігаційні дані. Інтернет і телефонія працюють із перебоями."

    menu:
        scientist "Авіація втрачає можливість зв’язку з диспетчерами. Морські судна не отримують навігаційні дані. Інтернет і телефонія працюють із перебоями."
        "Це небезпечно для польотів, правда?":
            jump scientist_ans10

label scientist_ans10:
    show scientist normal at right
    voice "audio/voice/4.59.mp3"
    scientist "Дуже. Тому під час сильних бурь рейси можуть відкладати."

    menu:
        scientist "Дуже. Тому під час сильних бурь рейси можуть відкладати."
        "Тобто буря на Сонці може залишити нас без світла, зв’язку й навіть супутників?":
            jump scientist_rep

label scientist_ans4:
    show scientist normal at right
    voice "audio/voice/4.61.1.mp3"
    scientist "Сонячні бурі створюють потужні магнітні поля. Вони наводять струм у довгих лініях електропередач."

    show scientist hand at right
    voice "audio/voice/4.61.2.mp3"
    scientist "Трансформатори перегріваються. Лінії електропередач можуть вийти з ладу. Іноді цілі країни залишаються без світла."

    menu:
        scientist "Трансформатори перегріваються. Лінії електропередач можуть вийти з ладу. Іноді цілі країни залишаються без світла."
        "Це справді можливо?":
            jump scientist_ans11

label scientist_ans11:
    show scientist normal at right
    voice "audio/voice/4.63.mp3"
    scientist "Так, у 1989 році в Канаді за кілька хвилин без електрики залишилися мільйони людей."

    menu:
        scientist "Так, у 1989 році в Канаді за кілька хвилин без електрики залишилися мільйони людей."
        "А що ж тоді відбувається з супутниками?":
            jump scientist_ans12

label scientist_ans12:
    show scientist normal at right
    voice "audio/voice/4.49.1.mp3"
    scientist "Коли заряджені частинки від Сонця досягають орбіти, вони вдаряють по супутниках."

    show scientist hand at right
    voice "audio/voice/4.49.2.mp3"
    scientist "Вони пошкоджують мікросхеми, викликають збої в навігації, іноді супутник виходить з ладу повністю."

    menu:
        scientist "Вони пошкоджують мікросхеми, викликають збої в навігації, іноді супутник виходить з ладу повністю."
        "Тобто навіть GPS у телефоні може перестати працювати?":
            jump scientist_ans13

label scientist_ans13:
    show scientist finger at right
    voice "audio/voice/4.51.mp3"
    scientist "Так. Якщо супутники втрачають стабільність, наші карти, навігація кораблів і літаків стають ненадійними."

    menu:
        scientist "Так. Якщо супутники втрачають стабільність, наші карти, навігація кораблів і літаків стають ненадійними."
        "Який жах. Зв’язок теж потерпає від сонячних бурь?":
            jump scientist_ans14

label scientist_ans14:
    show scientist normal at right
    voice "audio/voice/4.69.1.mp3"
    scientist "На жаль, так. Радіосигнали під час бурь спотворюються або зовсім зникають."

    voice "audio/voice/4.69.2.mp3"
    scientist "Авіація втрачає можливість зв’язку з диспетчерами. Морські судна не отримують навігаційні дані. Інтернет і телефонія працюють із перебоями."

    menu:
        scientist "Авіація втрачає можливість зв’язку з диспетчерами. Морські судна не отримують навігаційні дані. Інтернет і телефонія працюють із перебоями."
        "Це небезпечно для польотів, правда?":
            jump scientist_ans15

label scientist_ans15:
    show scientist hand at right
    voice "audio/voice/4.59.mp3"
    scientist "Дуже. Тому під час сильних бурь рейси можуть відкладати."
    menu:
        scientist "Дуже. Тому під час сильних бурь рейси можуть відкладати."
        "Тобто буря на Сонці може залишити нас без світла, зв’язку й навіть супутників?":
            jump scientist_rep

label scientist_ans5:
    show scientist hand at right
    voice "audio/voice/4.57.1.mp3"
    scientist "Радіосигнали під час бурь спотворюються або зовсім зникають."

    show scientist finger at right
    voice "audio/voice/4.57.2.mp3"
    scientist "Авіація втрачає можливість зв’язку з диспетчерами. Морські судна не отримують навігаційні дані. Інтернет і телефонія працюють із перебоями."

    menu:
        scientist "Дуже. Тому під час сильних бурь рейси можуть відкладати."
        "Це небезпечно для польотів, правда?":
            jump scientist_ans16

label scientist_ans16:
    show scientist hand at right
    voice "audio/voice/4.59.mp3"
    scientist "Дуже. Тому під час сильних бурь рейси можуть відкладати."

    menu:
        scientist "Дуже. Тому під час сильних бурь рейси можуть відкладати."
        "А що ж тоді відбувається з супутниками?":
            jump scientist_ans17

label scientist_ans17:
    show scientist normal at right
    voice "audio/voice/4.49.1.mp3"
    scientist "Коли заряджені частинки від Сонця досягають орбіти, вони вдаряють по супутниках."

    show scientist hand at right
    voice "audio/voice/4.49.2.mp3"
    scientist "Вони пошкоджують мікросхеми, викликають збої в навігації, іноді супутник виходить з ладу повністю."

    menu:
        scientist "Вони пошкоджують мікросхеми, викликають збої в навігації, іноді супутник виходить з ладу повністю."
        "Тобто навіть GPS у телефоні може перестати працювати?":
            jump scientist_ans18

label scientist_ans18:
    show scientist finger at right
    voice "audio/voice/4.51.mp3"
    scientist "Так. Якщо супутники втрачають стабільність, наші карти, навігація кораблів і літаків стають ненадійними."

    menu:
        scientist "Так. Якщо супутники втрачають стабільність, наші карти, навігація кораблів і літаків стають ненадійними."
        "Електромережі теж так сильно страждають від сонячних бур?":
            jump scientist_ans19

label scientist_ans19:
    show scientist normal at right
    voice "audio/voice/4.81.1.mp3"
    scientist "На жаль, так. Сонячні бурі створюють потужні магнітні поля. Вони наводять струм у довгих лініях електропередач."

    voice "audio/voice/4.81.2.mp3"
    scientist " Трансформатори перегріваються. Лінії електропередач можуть вийти з ладу. Іноді цілі країни залишаються без світла."

    menu:
        scientist " Трансформатори перегріваються. Лінії електропередач можуть вийти з ладу. Іноді цілі країни залишаються без світла."
        "Це справді можливо?":
            jump scientist_ans20

label scientist_ans20:
    show scientist book at right
    voice "audio/voice/4.55.mp3"
    scientist "Так, у 1989 році в Канаді за кілька хвилин без електрики залишилися мільйони людей."
    menu:
        scientist "Так, у 1989 році в Канаді за кілька хвилин без електрики залишилися мільйони людей."
        "Тобто буря на Сонці може залишити нас без світла, зв’язку й навіть супутників?":
            jump scientist_rep

label scientist_rep:
    show scientist hand at right
    voice "audio/voice/4.85.mp3"
    scientist "Так. А тепер питання для тебе: яка з цих сфер найбільш уразлива в перші години після бурі?"

    menu:
        scientist "Так. А тепер питання для тебе: яка з цих сфер найбільш уразлива в перші години після бурі?"
        "Супутники. Вони ж у космосі без жодного захисту, тож удар по них відбувається одразу.":
            jump scientist_rep1

        "Електромережі. Вони пов’язані одна з одною, і навіть невелике перевантаження може швидко поширитися.":
            jump scientist_rep1

        "Зв’язок. Якщо зникають сигнали, то це відчувають усі — від пілотів до людей із телефонами.":
            jump scientist_rep1

label scientist_rep1:
    show scientist finger at right
    voice "audio/voice/4.89.mp3"
    scientist "Правильно. Ось чому NASA запускає нові апарати — щоб попереджати нас заздалегідь. Хочеш побачити, як це відбувається?"
    menu:
        scientist "Правильно. Ось чому NASA запускає нові апарати — щоб попереджати нас заздалегідь. Хочеш побачити, як це відбувається?"
        "Авжеж!":
            voice "audio/voice/4.91.mp3"
            scientist "Тоді ходімо на базу — сьогодні стартує ракета, яка буде стежити за Сонцем."
            stop music
            jump chapter5_dialog
