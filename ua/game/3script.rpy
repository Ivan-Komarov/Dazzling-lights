define oak = Character("Дуб", color="#000", who_style = "name_text")
define sunflower = Character("Соняшник", color = '#000', who_style = "name_text")
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
    oak "Скільки років тут стою, а ніколи Вас не зустрічав."

    voice "audio/voice/3.1.2.mp3"
    oak "Хто ти є?"
    menu:
        oak "Хто ти є?"
        "Мандрівник я. Ось цікавлюся космосом. А, дубе, ти бачив не одне століття. Скажи, чи відчувають дерева погоду з космосу?":
            jump oak_ans1

label oak_ans1:
    show oak up at left
    voice "audio/voice/3.3.mp3"
    oak "Так, ми відчуваємо. Коли Сонце кидає на Землю свої бурі, змінюється магнітне поле, і наш сік рухається інакше. Дехто з нас росте повільніше, дехто — швидше."
    menu:
        oak "Так, ми відчуваємо. Коли Сонце кидає на Землю свої бурі, змінюється магнітне поле, і наш сік рухається інакше. Дехто з нас росте повільніше, дехто — швидше."
        "Тобто, навіть твоє коріння знає, що відбувається на Сонці?":
            jump oak_ans2

        "Але ж ти такий могутній. Хіба буря в небі може тобі зашкодити?":
            jump oak_ans3

label oak_ans2:
    show oak down at left
    voice "audio/voice/3.5.1.mp3"
    oak "Саме так. Коріння чує землю, а земля відчуває космос."

    show oak normal at left

    voice "audio/voice/3.5.2.mp3"
    oak "Радіація, магнітні збурення — усе це впливає на врожаї, на цвітіння, на ріст лісів."
    menu:
        oak "Радіація, магнітні збурення — усе це впливає на врожаї, на цвітіння, на ріст лісів."
        "Всі ми пов’язані та залежні від бурь? Навіть дихання?":
            jump oak_ans4

label oak_ans3:
    show oak up at left
    voice "audio/voice/3.7.1.mp3"
    oak "Я сильний, бо довго звикав. Та молоді паростки ніжніші."

    show oak normal at left
    voice "audio/voice/3.7.2.mp3"
    oak "Коли змінюється клімат від космічних процесів, коли Сонце гріє сильніше чи слабше — паросткам важче вижити."
    menu:
        oak "Коли змінюється клімат від космічних процесів, коли Сонце гріє сильніше чи слабше — паросткам важче вижити."
        "Чи можна сказати, що космос керує природою, як диригент оркестром?":
            jump oak_ans5

label oak_ans4:
    show oak up at left
    voice "audio/voice/3.9.1.mp3"
    oak "Ще б пак, навіть дихання, хоча це і складніше помітити."

    show oak down at left
    voice "audio/voice/3.9.2.mp3"
    oak "А молоді паростки ніжніші. Коли змінюється клімат від космічних процесів, коли сонце гріє сильніше чи слабше — паросткам важче вижити."
    menu:
        oak "А молоді паростки ніжніші. Коли змінюється клімат від космічних процесів, коли сонце гріє сильніше чи слабше — паросткам важче вижити."
        "То це виходить, що космос керує природою?":
            jump oak_ans6

label oak_ans5:
    show oak normal at left
    voice "audio/voice/3.13.1.mp3"
    oak "Природа залежить від космосу, як оркестр від диригента.  Ми, дерева, граємо ноти світла і тіні, води й тепла."

    show oak down at left
    voice "audio/voice/3.13.2.mp3"
    oak "А космос іноді змінює ритм. І тоді вся музика звучить інакше."
    menu:
        oak "А космос іноді змінює ритм. І тоді вся музика звучить інакше."
        "А що з квітами? Вони ж тендітні, як вони відчувають космос?":
            jump oak_ans7

label oak_ans6:
    show oak normal at left
    voice "audio/voice/3.15.1.mp3"
    oak "Саме так. Коріння чує землю, а земля відчуває космос."

    show oak down at left
    voice "audio/voice/3.15.2.mp3"
    oak "Радіація, магнітні збурення — усе це впливає на врожаї, на цвітіння, на ріст лісів."
    menu:
        oak "Радіація, магнітні збурення — усе це впливає на врожаї, на цвітіння, на ріст лісів."
        "Розкажи про ліси. Як космос торкається їх?":
            jump oak_ans8

label oak_ans7:
    show oak normal at left
    voice "audio/voice/3.17.1.mp3"
    oak "Квітам потрібне світло. Якщо Сонце палає надто яскраво, пелюстки згоряють швидше, і вони цвітуть менше."

    voice "audio/voice/3.17.2.mp3"
    oak "Якщо світла бракує — вони стають крихкими, наче втратили фарби. Бджоли плутаються в часі цвітіння, і тоді меду менше."
    menu:
        oak "Якщо світла бракує — вони стають крихкими, наче втратили фарби. Бджоли плутаються в часі цвітіння, і тоді меду менше."
        "То виходить, навіть краса залежить від космосу?":
            jump oak_ans9

        "Цікаво! А це означає, що навіть наш настрій якось пов’язаний із цими ритмами?":
            jump oak_ans10
label oak_ans8:
    show oak up at left
    voice "audio/voice/3.23.1.mp3"
    oak "Ліси — мов легені Землі."

    show oak down at left
    voice "audio/voice/3.23.2.mp3"
    oak "Коли сонячні бурі змінюють клімат, деякі дерева ростуть швидше, а деякі сохнуть."

    show oak normal at left
    voice "audio/voice/3.23.3.mp3"
    oak "Молоді паростки часто не витримують різкої спеки чи холоду. І тоді ліс втрачає силу."

    menu:
        oak "Молоді паростки часто не витримують різкої спеки чи холоду. І тоді ліс втрачає силу."
        "Але ж ти стоїш міцно. Хіба космос може забрати твою силу?":
            jump oak_ans11

        "А люди? Чи вони відчувають це так, як ти?":
            jump oak_ans12

label oak_ans9:
    show oak up at left
    voice "audio/voice/3.19.1.mp3"
    oak "Так. Але пам’ятай: краса квітів — це не лише для очей."

    show oak normal at left
    voice "audio/voice/3.19.2.mp3"
    oak "Вони живлять бджіл, а ті — поля. І якщо змінюється ритм цвітіння, змінюється й урожай, який отримає людина."

    menu:
        oak "Вони живлять бджіл, а ті — поля. І якщо змінюється ритм цвітіння, змінюється й урожай, який отримає людина."
        "Мабуть, найважливіше для людей — це врожаї. Як вони залежать від космосу?":
            jump oak_ans13

label oak_ans10:
    show oak normal at left
    voice "audio/voice/3.21.mp3"
    oak "Можна сказати й так. Коли квіти пізно розцвітають або рано в’януть, їжа для бджіл і птахів змінюється, а потім це відчуває й людина — від сніданку до свята врожаю."
    menu:
        oak "Можна сказати й так. Коли квіти пізно розцвітають або рано в’януть, їжа для бджіл і птахів змінюється, а потім це відчуває й людина — від сніданку до свята врожаю."
        "Мабуть, найважливіше для людей — це врожаї. Як вони залежать від космосу?":
            jump oak_ans13

label oak_ans11:
    show oak up at left
    voice "audio/voice/3.25.1.mp3"
    oak "Я встояв, бо загартувався. Та не всі дерева мають такий час."

    voice "audio/voice/3.25.2.mp3"
    oak "У горах сосни сохнуть швидше, а в степах акації більше цвітуть. І все це від відлуння Сонця."

    show oak normal at left
    voice "audio/voice/3.25.3.mp3"
    oak "Але найбільше ці зміни видно не в глибині лісу… а там, де люди сіють зерно."

    menu:
        oak "Але найбільше ці зміни видно не в глибині лісу… а там, де люди сіють зерно."
        "Мабуть, найважливіше для людей — це врожаї. Як вони залежать від космосу?":
            jump oak_ans13

label oak_ans12:
    show oak normal at left
    voice "audio/voice/3.27.1.mp3"
    oak "Люди їдять хліб. Хліб народжується в полях."

    show oak down at left
    voice "audio/voice/3.27.2.mp3"
    oak "Та не мені це Вам розповідати."

    menu:
        oak "Та не мені це Вам розповідати."
        "Мабуть, найважливіше для людей — це врожаї. Як вони залежать від космосу?":
            jump oak_ans13

label oak_ans13:
    show oak up at left
    voice "audio/voice/3.28.mp3"
    oak "Сонце може бути другом, а може й ворогом. Якщо його бурі занадто сильні — на полях вигоряє пшениця."
    menu:
        oak "Сонце може бути другом, а може й ворогом. Якщо його бурі занадто сильні — на полях вигоряє пшениця."
        "Тобто все сходиться до хліба, який ми їмо?":
            jump oak_ans14

label oak_ans14:
    show oak down at left
    voice "audio/voice/3.30.1.mp3"
    oak "Саме так. І якщо ти хочеш зрозуміти це по-справжньому, іди до того, хто сіє й збирає."

    show oak normal at left
    voice "audio/voice/3.30.2.mp3"
    oak "Фермер розповість тобі, як кожна буря на небі відлунює на його полі."

    scene bg sunb with fade
    jump sunflower_ans

label sunflower_ans:
    play music music_sf volume 0.5
    scene bg suns with fade
    show sunflower smiling at right

    voice "audio/voice/3.31.mp3"
    sunflower "Привіт! Звідки ти в наших краях? Перший раз тебе бачу."

    menu:
        sunflower "Привіт! Звідки ти в наших краях? Перший раз тебе бачу."
        "Ти завжди такий життєрадісний?":
            jump sunflower_ans1

        "Чому ти завжди дивишся вгору, на Сонце?":
            jump sunflower_ans2

        "Я мандрівник, та йду до фермера":
            jump sunflower_ans3

label sunflower_ans1:
    show sunflower normal at right
    voice "audio/voice/3.33.1.mp3"
    sunflower "Ха-ха! Авжеж. Я ж дивлюсь прямо в Сонце — у мене немає часу на сум!"

    voice "audio/voice/3.33.2.mp3"
    sunflower "Але іноді воно занадто шалене… і тоді навіть мені важко."
    menu:
        sunflower "Але іноді воно занадто шалене… і тоді навіть мені важко."
        "Що саме важко?":
            jump sunflower_ans4

        "Ти боїшся Сонця?":
            jump sunflower_ans5

label sunflower_ans4:
    show sunflower leaf at right
    voice "audio/voice/3.35.1.mp3"
    sunflower "Коли сонячні бурі б’ють, мої пелюстки вигорають швидше, листя втрачає силу."

    voice "audio/voice/3.35.2.mp3"
    sunflower "Я ще тримаюсь, але мої брати в полі страждають."

    menu:
        sunflower "Я ще тримаюсь, але мої брати в полі страждають."
        "Ти багато розповів. Виходить, навіть твоє життя залежить від бурь на Сонці.":
            jump sunflower_rep1

label sunflower_ans5:
    show sunflower smiling at right
    voice "audio/voice/3.37.1.mp3"
    sunflower "Ха! Та ні, це мій кумир! Просто він іноді перегинає."

    voice "audio/voice/3.37.2.mp3"
    sunflower "Як найкращий друг, що може і підняти настрій, і вдарити по плечу так, що боляче."

    menu:
        sunflower "Як найкращий друг, що може і підняти настрій, і вдарити по плечу так, що боляче."
        "Ти багато розповів. Виходить, навіть твоє життя залежить від бурь на Сонці.":
            jump sunflower_rep1

label sunflower_ans2:
    show sunflower normal at right
    voice "audio/voice/3.39.1.mp3"
    sunflower "Бо воно моє світло, моє життя. Я обертаюсь за ним, немов фанат за улюбленою зіркою."

    voice "audio/voice/3.39.2.mp3"
    sunflower "А коли Сонце сердиться — відчуваю це всім стеблом."

    menu:
        sunflower "А коли Сонце сердиться — відчуваю це всім стеблом."
        "То ти відчуваєш космос тілом?":
            jump sunflower_ans6

label sunflower_ans6:
    show sunflower smiling at right
    voice "audio/voice/3.41.1.mp3"
    sunflower "Авжеж! Листя тремтить від спеки, стебло гнеться від сухості, пелюстки опадають раніше."

    voice "audio/voice/3.41.2.mp3"
    sunflower "Ми — живий барометр космосу."
    menu:
        sunflower "Ми — живий барометр космосу."
        "Це звучить сумно…":
            jump sunflower_ans7

label sunflower_ans7:
    show sunflower leaf at right
    voice "audio/voice/3.43.1.mp3"
    sunflower "Ха-ха! Ні! Бо навіть у найважчий день я все одно повертаюсь до світла."

    voice "audio/voice/3.43.2.mp3"
    sunflower "Це мій характер — не здаватися."

    menu:
        sunflower "Це мій характер — не здаватися."
        "Ти багато розповів. Виходить, навіть твоє життя залежить від бурь на Сонці.":
            jump sunflower_rep1

label sunflower_ans3:
    show sunflower smiling at right
    voice "audio/voice/3.49.mp3"
    sunflower "Він зараз працює, давай я тобі допоможу. Питай, що хочеш!"

    menu:
        sunflower "Він зараз працює, давай я тобі допоможу. Питай, що хочеш!"
        "Чи впливає космічна погода на врожаї?":
            jump sunflower_ans8

label sunflower_ans8:
    show sunflower normal at right
    voice "audio/voice/3.51.1.mp3"
    sunflower "Ми, соняшники, — це не лише краса. Ми — олія, насіння, їжа для людей і птахів."

    voice "audio/voice/3.51.2.mp3"
    sunflower "Якщо Сонце дає надто багато, ми вигораємо. Якщо бурі збивають дощі — земля стає сухою. Урожай падає, і фермери сумують."
    menu:
        sunflower "Якщо Сонце дає надто багато, ми вигораємо. Якщо бурі збивають дощі — земля стає сухою. Урожай падає, і фермери сумують."
        "Але ж фермер може щось зробити?":
            jump sunflower_ans9

label sunflower_ans9:
    show sunflower leaf at right
    voice "audio/voice/3.53.1.mp3"
    sunflower "Може — поливати, підживлювати."

    voice "audio/voice/3.53.2.mp3"
    sunflower "Та якщо згорить небо й земля — він безсилий. Космос сильніший за плуг."

    menu:
        sunflower "Та якщо згорить небо й земля — він безсилий. Космос сильніший за плуг."
        "Значить, усе вирішує космос?":
            jump sunflower_ans10

label sunflower_ans10:
    show sunflower normal at right
    voice "audio/voice/3.55.mp3"
    sunflower "Ей, не все! Люди теж мають силу. Але їм варто пам’ятати, що не лише дощ і вітер — а й сонячні бурі впливають на їхній хліб."

    menu:
        sunflower "Ей, не все! Люди теж мають силу. Але їм варто пам’ятати, що не лише дощ і вітер — а й сонячні бурі впливають на їхній хліб."
        "Ти багато розповів. Виходить, навіть твоє життя залежить від бурь на Сонці.":
            jump sunflower_rep1

label sunflower_rep1:
    show sunflower leaf at right
    voice "audio/voice/3.45.1.mp3"
    sunflower "Так, і моє, і твій хліб, і твоє масло на столі. Якщо хочеш знати більше — поговори з фермером."

    voice "audio/voice/3.45.2.mp3"
    sunflower "Він знає, як космічна погода б’є прямо по його врожаю."
    menu:
        sunflower "Він знає, як космічна погода б’є прямо по його врожаю."
        "Тоді я вирушу до нього.":
            jump sunflower_rep2

label sunflower_rep2:
    show sunflower smiling at right
    voice "audio/voice/3.47.mp3"
    sunflower "Передай від мене вітання! І хай твій шлях завжди буде освітлений правильним промінням."
    stop music
    jump chapter4_dialog