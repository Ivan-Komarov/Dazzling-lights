define answer = 0
define fox = Character("Лисиця", color = "#000", who_style = "name_text")
define bird = Character("Пташка", color = "#000", who_style = "name_text")
define hero = Character("Ви", color = '#000', who_style = "name_text")

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
    fox "О господи, налякав!"
    show fox normal at left
    voice "audio/voice/2.1.2.mp3"
    fox "Ну привіт, мандрівник."

    voice "audio/voice/2.1.3.mp3"
    fox "Що тобі від мене потрібно?"
    menu:
        fox "Що тобі від мене потрібно?"
        "Хочу більше дізнатися про магнітне поле та бурі":
            show fox telling at left
            voice "audio/voice/2.3.1.mp3"
            fox "Магнітні бурі — це природне явище, коли магнітне поле Землі порушується під дією потужного потоку заряджених частинок із Сонця."
            voice "audio/voice/2.3.2.mp3"
            fox "Такі викиди сонячної енергії називаються сонячними спалахами."

            show fox smile at left
            voice "audio/voice/2.3.3.mp3"
            fox "Хочеш почути, як впливають на нас, тварин, магнітне поле та бурі?"
            menu:
                fox "Хочеш почути, як впливають на нас, тварин, магнітне поле та бурі?"
                "Так, звичайно!":
                    jump fox_story
                "Немає сильного бажання, якщо чесно.":
                    show fox angry at left
                    voice "audio/voice/2.7.mp3"
                    fox "Сил в мене на тебе нема! Йди до пташки, може вона тебе витримає!"
                    jump bird_story

label fox_story:
    show bg fox with fade
    show fox normal at left
    voice "audio/voice/2.5.mp3"
    fox "Ой, навіть не знаю з чого й почати, може в тебе є якесь питання?"
    menu:
        fox "Ой, навіть не знаю з чого й почати, може в тебе є якесь питання?"
        "Це правда, що магнітні бурі впливають на твою поведінку?":
            show fox telling at left
            voice "audio/voice/2.9.1.mp3"
            fox "Магнітні бурі справді впливають на нас, тварин. Ми можемо ставати тривожними, неспокійними, іноді навіть агресивними, а буває — навпаки, замкненими й млявими."
            voice "audio/voice/2.9.2.mp3"
            fox "Бла-бла-бла, тобі це точно цікаво?"
            menu:
                fox "Бла-бла-бла, тобі це точно цікаво?"
                "Так! Досить мене до пташки відправляти!":
                    show fox normal at left
                    voice "audio/voice/2.11.1.mp3"
                    fox "Гаразд, розповім тобі ще дещо."

                    show fox telling at left
                    voice "audio/voice/2.11.2.mp3"
                    fox "Магнітні бурі також можуть впливати на їхню здатність орієнтуватися в просторі, що порушує міграційні шляхи."

                    show fox angry at left
                    voice "audio/voice/2.11.3.mp3"
                    fox "Давай, брись звідси, робити мені більше нічого, їсти хочу..."
                    jump bird_story
                "Та ні, лише по факту все, не треба деталей.":
                    show fox angry at left
                    voice "audio/voice/2.13.1.mp3"
                    fox "Ой, йди давай до птиці, робити мені нічого, що з тобою вештатись."

                    show fox normal at left
                    voice "audio/voice/2.13.2.mp3"
                    fox "Їсти тільки хочеться..."
                    jump bird_story

        "А чи правда, що під час бурі важче летіти й знаходити дорогу у небі?":
            show fox angry at left
            voice "audio/voice/2.15.mp3"
            fox "З цим питанням йди до птиці краще, й по можливості, не повертайся."
            jump bird_story

label bird_story:
    hide fox
    show bg bird with fade
    show bird normal at right
    voice "audio/voice/2.16.1.mp3"
    bird "О, привітик!"

    show bird telling at right
    voice "audio/voice/2.16.2.mp3"
    bird "Ти теж прийшов дізнатися про вплив магнітного поля та бурі на пташине братство?"
    menu:
        bird "Ти теж прийшов дізнатися про вплив магнітного поля та бурі на пташине братство?"
        "Саме так!":
            show bird happy at right
            voice "audio/voice/2.18.1.mp3"
            bird "Тоді вмощуйся позручніше!"

            show bird telling at right
            voice "audio/voice/2.18.2.mp3"
            bird "Пернаті реагують трохи інакше, можуть використовувати..."
            menu:
                bird "Пернаті реагують трохи інакше, можуть використовувати..."
                "Гей, гей, гей! Повільніше,  манюня.":
                    voice "audio/voice/2.20.1.mp3"
                    bird "Ой, ну добре! Але не перебивай більше!"
                    voice "audio/voice/2.20.2.mp3"
                    bird "Пернаті, ну, реагують трохи інакше, можуть використовувати магнітне поле для навігації, тому його зміни, аааа, можуть впливати на їхні шляхи..."

                    show bird normal at right
                    voice "audio/voice/2.20.3.mp3"
                    bird "Що ж тобі більше сказати, бо я нічого не пам’ятаю, чесно."
                    voice "audio/voice/2.20.4.mp3"
                    bird "Ну я тобі наче все основне розповіла. Йди до лисиці, може вона тобі щось розкаже."
                    menu:
                        bird "Ну я тобі наче все основне розповіла. Йди до лисиці, може вона тобі щось розкаже."
                        "Вона кудись втекла, проведи мене до неї, будь ласка.":
                            show bird happy at right
                            voice "audio/voice/2.22.mp3"
                            bird "Ну  добре, ходімо!"
                            jump pregame_catch

label pregame_catch:

    scene bg fox with fade
    show bird normal at right
    show fox smile at left
    hero "Лисице, а в нас таке питання..."
    voice "audio/voice/2.24.mp3"
    fox "О, ти приніс мені обід!"
    show bird frightened at right
    voice "audio/voice/2.25.mp3"
    bird "Еее, на що ти натякаєш?!"
    voice "audio/voice/2.26.mp3"
    fox "От зараз ти і побачиш."
    voice "audio/voice/2.27.mp3"
    bird "ААААААААААААААААА!!!"
    jump game_catch

label game_catch:
    play music music2_2 volume 0.5
    show mov0
    menu:
        "Чи можуть морські тварини, наприклад кити або дельфіни, плутати маршрут через зміни магнітного поля?"
        "Так, іноді зміни магнітного поля збивають їхню «вбудовану навігацію», що призводить до дезорієнтації.":
            $ answer += 1
            show mov1
        "Ні, вони орієнтуються виключно за зірками й положенням Сонця.":
            $ answer -= 1
            show mov_1
    menu:
        "Які тварини найбільше залежать від магнітного поля Землі для виживання?"
        "Міграційні птахи, морські черепахи та риби, які долають великі відстані.":
            $ answer += 1
            show mov2

        "Великі хижаки на суші, як-от леви й тигри, бо вони використовують магнітне поле для полювання.":
            $ answer -= 1
            show mov_2


    menu:
        "Як саме магнітні бурі можуть змінювати поведінку тварин у природі?"
        "Магнітні бурі викликають у тварин лише фізичну втому, але не впливають на їхні інстинкти чи поведінку.":
            $ answer -= 1
            show mov3
        "Вони впливають на орієнтацію тварин, які користуються магнітним полем Землі — наприклад, птахів або риб, — тому ті можуть змінювати напрям міграції чи губитися.":
            $ answer += 1
            show mov_3

    menu:
        "Чи можна сказати, що космічна погода формує певні еволюційні механізми у тварин?"
        "Так, постійний вплив космічних факторів змусив тварин виробити здатність «читати» магнітне поле.":
            $ answer += 1
            show mov4
        "Ні, еволюція залежить лише від клімату й кількості їжі на планеті.":
            $ answer -= 1
            show mov_4
    menu:
        "Які тварини найбільш уразливі до змін у космосі, а які — майже не відчувають їх?"
        "Уразливими є тільки комахи, а всі великі тварини взагалі не відчувають космічних змін.":
            $ answer -= 1
            show mov5
        "Найчутливіші — міграційні види (птахи, кити, черепахи), а найменш — ті, що живуть локально й не мігрують.":
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
    bird "Фух!"
    menu:
        bird "Фух!"
        "Лисиця майже наздогнала тебе!":
            voice "audio/voice/2.32.mp3"
            bird "Зате весело було, єєєєє, якщо підеш по полю за річку, то дійдеш до одинокого мудрого дубааа, там він тобі куди більше розповість, а ніж я, там, да."
            stop music
            jump chapter3_dialog

label catch_bad_ending:

    scene bg fox with fade
    show fox smile at left
    voice "audio/sound/crunch.mp3"
    fox "Ой, ну я вдячна тобі, за те що такий смачний обід роздобула."
    voice "audio/voice/2.28.mp3"
    fox "Ой, ну я вдячна тобі, за те що такий смачний обід роздобула."
    menu:
        fox "Ой, ну я вдячна тобі, за те що такий смачний обід роздобула."
        "Що ти зробила...":
            show fox telling at left
            voice "audio/voice/2.29.mp3"
            fox "Та не переживай ти сильно, шукай позитив. За те, що допомогла мені, тримай карту, яка приведе тебе до дуба."
            stop music
            jump chapter3_dialog