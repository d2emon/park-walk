from dice import d

articles = [
    """… Ты решил съездить в Павловский Парк, заодно убив по дороге репера Шляпогрыза. Сев на поселковую электричку ты
    вскоре выходишь на вокзале. Парк прямо впереди, ты покупаешь билет и входишь. Скоро твое путешествие начнется.""",

    """Ты начинаешь игру в Павловском Парке. У тебя нет ничего, кроме пятидесяти рублей. Войдя в парк с юга, ты 
    двигаешься вперед по длинной алее. Иди на (6)""",
    """2""",
    """Ты идешь прямо  и через пару минут выходишь на развилку. Куда направишься?
    Если прямо, туда где ты замечаешь какое – то строение, похожие на магазин, иди на (76)
    Если свернешь налево, туда, где виднеется какое – то поселение, то иди на (46)
    Если же направо, где ошивается какой – то мужик, то на (15)""",
    """4""",
    """5""",
    """Итак, твоя миссия – убить репера Шляпогрыза, который обитает во дворце Екатерины II. 

    Сверившись с картой ты понимаешь, что этот дворец расположен в самой северной части парка. Пройти туда можно 
    разными путями, и ты знаешь, что некоторые из них на карте не обозначены.

    Как бы то ни было, алея вскоре заканчивается ты подходишь к парку. Недалеко стоит ларек с семечками.

    Если хочешь зайти, иди на (18) если пройдешь мимо – (3)""",
    """7""",
    """8""",
    """9""",
    """10""",

    """11""",
    """12""",
    """13""",
    """14""",
    """15""",
    """16""",
    """17""",
    """Ты подходишь к магазу и видешь:
    Товар                               цена в рублях
    СЭМЕЧКИ                                5
    ОРЕХИ ДЛЯ БЕЛОК               10
    ГРЕЦКИЕ ОРЕХИ                   25
    НОЖ ДЛЯ МЯСА(урон 0.5)   50 
    Чтобы что – нибудь купить, вычеркни на своей ИГРОВОЙ КАРТЕ необходимую сумму денег, и впиши купленный предмет.
    Теперь иди на (3).""",
    """19""",
    """20""",
]

"""
Подготовка к путешествию





А ТЕПЕРЬ ПЕРЕВЕРНИ СТРАНИЦУ!...
1


 
2

Ты заходишь в первую попавшуюся хижину. В ней сидит старый бородатый Дед. 
-- Зрасссь, милок, -- говорит он, покуривая табак.
-- Здарово Дед. Ну чего хорошего расскажешь?
-- Да штож рассказывать… -- он кряхтит и чихает, -- иди кА ты лучше… В озерце искупайся. Только не в нашем, в следующем.
	Он опять начинает кряхтеть и кашлять, а ты выходишь из хижины. Твой путь лежит на север, иди на (39)

3



4

Ты подходишь к прокату катамаранов. Вдруг ты видишь, что на катамаране плывет эта белка, а ее на руках держит какой то бомж.
Иди на (53)

5

Свернув направо и пройдя немного по лесу, ты замечаешь среди деревьев небольшое озеро. Тебя так и тянет в нем искупаться!
Искупаешься (50), или пройдешь мимо (27)?

6



7

	Ты говоришь с ней о всякой фигне, но в разговоре она упоминает кое – что важное. Она говорит: если ты когда ни будь встретишь еврея Абрашу и он предложит тебе выпить одну из жидкостей, то в любом случае не пей желтую, про остальные я не знаю. 
	Поблагодарив тетку и попрощавшись с ней, ты идешь дальше. Иди на (63).

8

	Ты поворачиваешь направо и идешь по еле заметной дорожке вдоль деревьев. Что – то подсказывает тебе, что дворец уже близко, по этому ты весело идешь вперед…
	…Как вдруг прямо перед тобой, словно из – под земли, появляется мужик в кожаной куртке и спортивных штанах. Он молчит, крутит в руках какие – то четки и пристально глядит на тебя. Что будешь делать?
	Скажешь «Здарово, мужик!»				Иди на (38),
	Скажешь «Че – то ты браток тут 
	Не по – понятиям!»						Иди на (81),
	Нападешь на него						Иди на (49),
 	Проигнорируешь мужика и пойдешь
 дальше своей дорогой                                                        Иди на (62)

9

Через несколько минут ты выходишь на очередную развилку. Ты видишь раздолбанный сожженный магаз, в нем ничего нет. За него уходит еле заметная тропинка на север, тогда как на восток ведет хорошая ровная дорога. 
На восток                                                                       	           Иди на (22)
На север						                       Иди на (85)

10.

Пуля попадает тебе прямо промеж глаз. Ты ногаешь дрыгами и головаешь мотою, у тебя из крови льется живот…
На этом ты и здох!..

11

Повернув скрипучий руль, ты направляешь катамаран на север, в камыши.
Ты заплываешь в густую ряску, но винты твоего катамарана с легкостью ее рубят. 
Вдруг ты натыкаешься на какой-то плавающий в воде предмет. Раздвинув камыши ты с ужасом понимаешь, что это свежий труп мужика!
Ты можешь забрать найденные у него в кармане деньги (250 рублей), тогда сделай пометку на игровой карте и скорее уматывай от туда!
Иди на (67).

12

Наконец-то ты на берегу! Весь мокрый, ты с четверть часа идешь по густому подлеску и наконец с радостью замечаешь Дворец!
Немного пообсохнув на солнце, ты выбираешься из леса и направляешься на главную площадь парка.
Иди на (14)

13

Решив, что дорога не куда ни денется, ты решаешь сначала покататься на катамаране. Это стоит 50 рублей за час.
Если у тебя их нет, то придется идти на (71)! 
Если есть, читай дальше.
Заплатив в кассу на лодочной станции 50 рублей (вычеркни их на ИГРОВОЙ КАРТЕ), ты получаешь чек и садишься на желтый катамаран «Заря»! Выплыв на середину пруда, ты любуешься окрестностями.
Куда поплывешь? В южную часть пруда, где вода чистая и прозрачная (43), или в северную, где все заросло болотной травой, тиной и камышами (11)?

14

Наконец - то, ты на главной площади перед дворцом! Твоя цель уже почти у тебя в руках. Ты проходишь мимо туристов и рядов мраморных статуй, и вот перед тобой 2 здания:
Если сразу рванешь во дворец - (60), если сначала 
Хочешь зайти в сувенирную лавку, (44).

15

Ты идешь по правой дороге. Лес заканчивается, поэтому вокруг только деревья и кусты.
К тебе подходит Состоятельный Мужик в пиджаке, брюках, галстуке и с короткими волосами и спрашивает, не поможешь ли ты ему в одном деле?
Если хочешь помочь мужику, иди на 68, если откажешься и пойдешь мимо, иди на (9).

16

Ты сжимаешь кулаки и нападаешь на МУЖИКА.

                         СИЛА   ВЫНОСЛИВОСТЬ  УРОН
МУЖИК С         
ТОПОРОМ          3                     2                       1.0

Если тебе удалось убить МУЖИКА С ТОПОРОМ, иди на (23).

17

Все ГОПНИКИ мертвы. Обыскав их, ты находишь 50 рублей, 5 упаковок сэмечек и 5 кэпочек. Можещь все это взять с собой, тогда пометь это на ИГРОВОЙ КАРТЕ. Убедившись, что тебя не заметили, ты оттаскиваешь ГОПНИКОВ в канаву, а сам идешь дальше по дорожке. Иди на (66).  

18

 

19

 - Давай желтую, - говоришь ты и Абраша протягивает тебе желтую колбу. Пахнет она какими – то конфетами, и ты одним глотком выпиваешь содержимое. Вдруг Абраша и вся его комната пропадает, и у тебя темнеет в глазах… 
Иди на (49).    	

20

Тропинка идет на восток, и вскоре выводит тебя к берегу большого пруда. Подойдя ближе, ты трогаешь воду: она теплая, но купаться тут нельзя, потому что все заросло тиной и ряской, хотя южная часть пруда абсолютно чистая.
Пройдя еще немного, ты замечаешь на западной стороне пруда какие – то домики. Вскоре ты понимаешь, что это лодочная станция. Тебя так и тянет покататься на катамаране!
Пойдешь к лодочной станции (иди на (13)), или решишь, что это займет слишком много времени и пойдешь дальше (иди на (71))?

21

Пройдя несколько метров, ты вдруг чувствуешь, что тебе как – то очень легко идется. Сначала ты не можешь понять почему, но потом до тебя вдруг доходит, ты в ужасе хватаешься за карман…
Так и есть! Недавно встреченный тобой мужик оказался ВОРОМ. Он украл ровно половину твоих денег, и к тому же, если у тебя были КЭПОЧКИ ГОПНИКОВ, то и их тоже. Вычеркни эти предметы на ИГРОВОЙ КАРТЕ!
Ты бегом возвращаешься на то место, где впервые увидел вора, но там уже разумеется ни кого нет.
Матерясь проклиная все на свете, особенно депутатов, ты бредешь дальше. Иди на (62).

22

Пройдя метров двадцать, дорожка поворачивает на север и ты видишь на изломе два толчка. Что то тебе очень хочется в один из них…
У женского толчка стоит молодая тетка с сумкой и жрет сэмечки.
Пойдешь в мужской толчок,                                                           Иди на (32)
Подойдешь к тетке,						             Иди на (75)
Или пройдешь мимо?                                                                      Иди на (63)

23

Обыскав МУЖИКА С ТОПОРОМ, ты находишь у него 25 рублей, ну и конечно его топор (урон 1)! Можешь взять это с собой. Скинув МУЖИКА в канаву, чтобы его никто не нашел, ты идешь дальше и вскоре лес заканчивается. Ты вылезаешь из него, иди на (54).

24

 - Здрасти, здрасти, - говорит Абраша, когда ты заходишь к нему в гости. – я таки алхимик, готовлюсс, знаете ли, разные зельеца… Не желаете ли испить?
Ты соглашаешься и Абраша протягивает тебе три пробирки: какую выберешь?
Красную                                                                  Иди на (45)
Синюю                                                                    Иди на (34)
Желтую					           Иди на (19)

25

Дорожка очень долго петляет между деревьев, и ты уже решаешь, что заблудился, но потом слышишь где – то недалеко шум воды  стремглав несешься туда сквозь лес. 
Иди на (28).

26

Ты решаешь подзаработать денег и идешь искать белку с золотой цепочкой на шее. По короткому пути ты идешь к лодочной станции, где она и потерялась. 
Иди на (4).

27

Дорожка сначала уводит тебя от озера на восток, но потом, сильно углубившись в лес, она вдруг поворачивает и ты видишь впереди длинные доски, сваленные в кучу и лежащие прямо между деревьев. Забравшись на них и пройдя до конца, ты оказываешься на большой площадке.
 Ты спрыгиваешь с досок и идешь туда, иди на (30).

28

Ты выходишь к неширокой, но бурной реке, через которую перекинут узкий деревянный мостик. Он почему – то не внушает тебе доверия. На другой стороне реки растет лес.
Пойдешь по этому мостику (иди на (36)), или спрыгнешь в воду и поплывешь вниз по течению (на запад), надеясь найти там хороший берег и вылезти (иди на (79))?

29

Дорожка, которую ты выбрал, хоть и заброшена, но асфальтовая, по этому идти по ней легко.
Вдруг за очередным поворотам ты видишь около канавы 5 мужиков. Они одеты в спортивные штаны, телогрейки и кэпочки. Мужики сидят на корточках, едят сэмечки и о чем – то негромко разговаривают. Тут ты с ужасом понимаешь, что это ни кто иные, как ужасные ГОПНИКИ! 
Ты уже собираешься потихоньку свалить, но тут они замечают тебя.
- О мужик, - говорит тебе один из них, - у нас сэмечки кончаются, дай нам ышо.
- Ну или рублей 50 дай. – говорит другой.
Другого выбора у тебя нет. Если у тебя есть 50 рублей или пакет сэмичек, отдай их ГОПНИКАМ (иди на (87)), если же у тебя этого нет, или ты не хочешь отдавать, то тебе придется драться сразу со всеми пятью (иди на (52))! 

30

От сюда ведут две дороги. Куда направишься?
На север, к мосту через реку,				Иди на (56)
Или на восток, к какому – то строению?		            Иди на (74)
Так же ты можешь выбрать одну 
маленькую тропинку через лес,
ведущую в западном направление. 			Иди на (8)

31

- Моя харошая!!! – орет Состоятельный Мужик, получив свою белку и начинает тискать ее и кормить орехами. Потом он снимает с нее золотой медальен и кладет его себе в карман. 
- Ты спас ее, друг! – говорит он патом. – Как я и обещал, вот твои деньги!
Он отдает тебе 200 рублей (отметь это на ИГРОВОЙ КАРТЕ). Потом он долго прощается, и наконец ты оставляешь его и идешь дальше. 
Иди на (9).

32

Ты заходишь в толчок и хорошенько сотворив там злодеяние великое, радостно расслабляешься. Повысь уровень своей УДАЧИ на 1, даже если он еще не понижался! Кстати, бумагу от туда тоже можешь утащить (тогда отметь ее на ИГРОВОЙ КАРТЕ).
Теперь можешь подойти к тетке (иди на (75)), или пройти мимо (иди на (63)).

33

Ты входишь во дворец и оказываешься в огромном красивом зале из мрамора, уставленного статуями, барельефами и картинами.
Дворец трехэтажный, и ты не знаешь, на каком именно этаже находится Шляпогрыз. Но будь осторожен, этот гад уже подготовился к твоему приходу и напичкал весь дворец всевозможными ловушками и десятками охранников!
Решив, что лучше не стоять долго на одном месте, ты пытаешься решить, куда идти. 
Перед тобой две мраморных лестницы на запад (иди на (64)), и на восток(95). Так же в зале около лестниц есть проходы в смежные комнаты. Ты можешь войти в левую (иди на (99)), или в правую (иди на (78)). 

34

- Дай мне синюю! – говоришь ты и Абраша протягивает тебе ее. Жидкость ни чем не пахнет, и ты набравшись смелости, выпиваешь ее. 
- О, - говорит Абраша, - тебе повезло! Это ЭЛЕКСИР СИЛЫ! Теперь начальное значение твоей СИЛЫ увеличено на 1! (Отметь это на ИГРОВОЙ КАРТЕ).
Поблагодарив этого еврея – алхимика и попрощавшись, ты, довольный своим правильным выбором, выходишь из его дома.
Пойдешь по дорожке на северо – восток (иди на (20)), или углубишься в северный лес (иди на (25))?

35

Ловко зацепившись рукой за самый край моста, ты подтягиваешься и вылезаешь через перила. Немного пообсохнув на мосту, ты решаешь перейти его и идти дальше, иди на (76).

36

Несмотря на то, что мост показался тебе таким хлипким, он тебя с легкостью выдержал!
Ты начинаешь пробираться через густой подлесок в северном направление, и уже через несколько минут замечаешь сквозь ветки хорошую асфальтовую дорогу.
Иди на (58).

37

Не доверяя лесу, ты идешь дальше по прямой дороге. 
Вдруг из – за одного из деревьев слева от тебя вылазят два бомжа.
Один из них кричит:
- Смари, Петрович, какойто петух!
- Вижу, - орет другой, - Михалыч, а давай его замочим и бабло хапнем!
- Внатуре, давай!
Крича и корча пьяные рожи, бомжи медленно надвигаются на тебя, чтобы «замачить», но ты совсем иного мнения! 
Иди на (86) и вломи им хорошенько.

38

- Здарово, мужик! – говоришь ты.
- Здарово, - говорит мужик.
Вы минут десять с ним говорите, а патом жмете друг другу руки и прощаетесь. Тебе очень понравился этот мужик, жаль, так мало удалось поговорить… Пообещав себе, что когда ты убьешь Шляпогрыза, найдешь этого мужика и поговоришь с ним еще, ты идешь дальше.
Иди на (21).

39

Миновав деревню, ты идешь на север вдоль больших штабелей досок. Потом они кончаются и тебе приходится углубиться в лес…
Иди на (66).

40

Следуя совету ВОРА, ты находишь пятое окно справа от угла и влезаешь внутрь. Он тебе не врал, сигнализация не сработала!
Ты осматриваешься: перед тобой большая комната из мрамора и янтаря, на стенах висят картины. В южной стене есть одна дверь, за ней слышится какой – то шум.
Поскольку других дверей нет, ты входишь туда. 
Иди на (99).

41

Ты вбегаешь в самую левую дверь и зацепляешь какую – то веревку. Сверху что – то натягивается, а патом прямо на тебя валится огромная бетонная плита. Это была одна из ловушек Шляпогрыза. Ты, совсем чуть – чуть не дошел до цели…
На этом ты и помер!...

42

Ты подходишь к закрытой двери и несколько раз дергаешь ее, она не открывается. За дверью раздается какое – то тихое рычание. Если ты посильнее ударишь дверь плечем (иди на (83)), она все же откроется, но стоит ли это делать? Если хочешь вернуться к лестнице и пойти дальше по коридору, иди на (69).

43

Ты поворачиваешь катамаран на юг, и некоторое время плывешь спокойно, но насладиться красотой природы тебе не дают. Ты замечаешь еще один катамаран, на котором сидят Платоныч и его сын. Завидев тебя, они что – то орут и прыгают на твой катамаран! Отвертеться не удастся, придется драться!
                         
                       СИЛА  ВЫНОСЛИВОСТЬ  УРОН
ПЛАТОНЫЧ       2                    3                       0,2
ЕГО СЫН            1                    1                       0,5
Если ты убил их обоих, иди на (55).

44

Сначала ты решаешь зайти в сувенирную лавку. Цены в ней очень высокие, потому что они рассчитаны на богатых туристов. Тут работает продавец дядя Слава. Он предлагает тебе такие товары:

Товар                              цена    действие
Тарелка супа                   150    Ее надо съесть прямо тут, она 
                                                   восстановит твою ВЫНОСЛИВОСТЬ
                                                   до начального значения.
Пирожок с капустой       50     Ты можешь съесть его в любое время,
                                                   кроме битвы, это не займет много 
                                                   времени. Один пирожок восстановит
                                                   одну ВЫНОСЛИВОСТЬ. Всего их
                                                   тут не больше трех.
Бетонно – стеклянный   250    Ты можешь использовать его только
кастет                                        один раз. Он одним ударом убьет 
                                                    врага, чья СИЛА не более 3, и после
                                                    этого ломается.
Большой нож                  350     УРОН – 1.5 
 для мяса

Другое тебя не интересует, но дядя Слава говорит тебе, что пока никто не видит, он может купить у тебя некоторые товары по следующим ценам:

Товар                                          цена в рублях
Пакет сэмечек                                    10
Кэпочка гопника                                20
Туалетная бумага                               30
Пиво «Степан Разин»                        40
Тапор УРОН 1                                    50

Еще немного посмотрев на товары, ты благодаришь дядю славу и идешь к Дворцу.
Иди на (60).

45

- Давай ка мне красную, - просишь ты и Абраша протягивает тебе красную колбу. Жидкость пахнет дихлорэтиленгидроглюколемтри, ты выпиваешь ее и тут же чувствуешь себя очень злым. Отними 1 от своей УДАЧИ! (Отметь это на ИГРОВОЙ КАРТЕ).
- Да, таки тебе не повезло, это было зелье Плохого Настроения. Эффект сильный, но короткий. Через десять минут все пройдет.
Но ты просто в ярости! Ты швыряешь эту колбу в Абрашу, орешь, материшься, и напоследок, пнув его хорошенько по пузу, да так, что он аж падает со стула, ты выходишь из этого гребаного дома и попадаешь на чертову улицу. Ты пинаешь какие – то пни и проклинаешь всех подряд. 
Лишь через пол часа, немного успокоившись, ты решаешь, куда дальше идти.
Пойдешь по дорожке на северо – восток (иди на (20)), или углубишься в северный лес (иди на (25))?

46

Ты выбираешь западное направление и вскоре проходишь мимо указателя с надписью «Село Бухая Выпь». Насколько ты помнишь, тут стали вырубать лес, поэтому почти все переехали, осталось только несколько человек. 
И правда, село состоит теперь всего из нескольких домов, обложенных со всех сторон досками. Тебя привлекает один дом: он единственный двухэтажный, с черепичной красной крышей.
Зайдешь в него,							Иди на (94)
Или в како – нибудь другой?					Иди на (2)
Если не будешь задерживаться 
И пойдешь на север,  						Иди на (39).

47

Каким – то чудом ты уклоняешься от летящей прямо в тебя пули, и она разбивает вазу за твоей спиной. Матюгнувшись раза два, Шляпогрыз бросает свой пистолет и, достав огромный самурайский меч, с яростным криком бросается на тебя!
Готовься к решающей схватке, иди на (80).

48

Когда оба бомжа падают на землю, ты пытаешься их обыскать, но они такие вонючие, даже для тебя, что ты лишь спихиваешь их ногой в канаву и поскорей идешь дальше.
Дорожка поворачивает сначала на восток, а потом снова на запад. Иди на (63).

49

Какое то время ты ничего не видишь и не слышишь, а потом вдруг зависаешь в двух метрах в воздухе над каким – то прудом и в следующую секунду падаешь туда, поднимая тучи брызг. 
Когда ты, проклиная Абрашу, выкарабкиваешься из воды, то начинаешь подозревать, что это было, очевидно, какое – не будь зелье телепортации.
Немного обсохнув, ты осматриваешься: на дальнем берегу пруда видишь какую - то маленькую деревню, а вокруг нее несколько лесопилок. Тебе эта деревня вовсе не по пути, поэтому ты, прыгая через кучами наваленные доски, обходишь пруд с запада и вскоре проходишь деревню. Иди на (39).

50

Вода тут очень теплая, по этому ты раздеваешься и окунаешься в озеро. Покупавшись в нем пол часика, ты вылезаешь на берег и обсыхаешь. Это озеро придает тебе сил – восстанови уровень своей ВЫНОСЛИВОСТИ до начального значения и прибавь 1 к своей УДАЧЕ.
Высохнув, ты одеваешься и с новыми силами идешь в лес. Переходи на (27).

51

Ты поднимаешься по мраморной лестнице и понимаешь, что ты на последнем третьем этаже. На лестнице никого нет, и ты поднимаешься в большой зал с шестью дверями в юго – западной стене. Других выходов тут нет, поэтому решай, куда идти:
Дверь с надписью «Администрация»			Иди на (98)
Дверь с надписью «Комната охраны» 			Иди на (61)
Дверь с надписью «Служебный туалет»			Иди на (81)
Дверь с надписью «Отдел реставрации»  			Иди на (41)
Дверь с надписью «Вторая каминная»			Иди на (83)
Дверь с надписью «Овальная комната»			Иди на (92)

52

Не давая ГОПНИКАМ опомниться, ты бросаешься в битву:

                                СИЛА  ВЫНОСЛИВОСТЬ  УРОН
ГОПНИК САНЯ         1                      2                    0.1
ГОПНИК ГОША        1                      2                    0.2
ГОПНИК СЭМЭН      2                      1                    0.1
ГОПНИК МИША       1                      2                    0.3
ГОПНИК ПАША        2                      1                    0.2

Если ты убил всех ГОПНИКОВ, скорей иди на (17).

53

Ты подплываешь к бомжу и вдруг белка сама прыгает тебе на плече. Бомж достает топор мясника и говорит: «Мужик, лучше вали по – хорошему!»
Ты решаешь спасти свою жизнь, иди на (96).

54

Пройдя еще пару метров ты выходишь на небольшую площадку, окруженную лесом. На ней стоит одноэтажный деревянный домик с красной черепичной крышей. На двери написано: «Абраша Перельман. Химик.» 
Если хочешь зайти к Абраше в гости, иди на (24). Если не станешь задерживаться и пойдешь по асфальтовой дорожке на северо – восток, иди на (20).
Так же ты можешь пойти на север и углубиться в лес, тогда иди на (25).

55

Обыскав семейку, ты находишь у сына АРМЕЙСКИЙ НОЖ (урон 0.5), а у Платоныча 30 рублей. Можешь взять все это с собой, в таком случае отметь эти предметы на ИГРОВОЙ КАРТЕ и иди на (67).

56

Ты идешь по северной дороге через лес, и вскоре до тебя доносится шум воды. Как ты и предполагал, скоро ты выходишь к бурной реке. Через нее перекинут широкий мост с высокими перилами. Тебе ничего не остается, как перейти его, для этого иди на (76).

57

- А я сейчас тебя замочу! – говоришь ты.
Тетка размахивает сумкой и с боевым криком «Ай, люлю – люлю», нападает на тебя!

              СИЛА  ВЫНОСЛИВОСТЬ  УРОН
ТЕТКА       4                   3                        0.1

У нее ты находишь 50 рублей и НОЖНИЦЫ. (Сделай пометки на ИГРОВОЙ КАРТЕ). Ты закидываешь тетку за толчки в канаву, чтоб ее там никто не нашел, а сам скорее уходишь по северной дороге, иди на (63).

58

 Эта дорога ведет тебя вдоль берега реки. На юга от дороги растут редкие деревья и течет река, а на севере ты несколько раз замечаешь высокую стальную ограду. Это значит, что ты достиг северной границы парка! 
Пройдя еще сто метров, ты выходишь ко Дворцу!!!
Иди на (14).

59

Все охранники мертвы, ты можешь взять их ДУБИНКИ (урон 0.5, ПОМЕТЬ ИХ НА игровой карте). Ты прячешь их тела в зале за статуей, и выходишь в западную дверь. 
Ты в большом зале, в нем есть две лестницы наверх (на запад (иди на (64)), и на восток (95)) и дверь в восточной стене (иди на (78)).

60

Ты решаешь больше не задерживаться и идешь к дворцу. Перед входом стоят ряды статуй, трава подстрижена. Когда охранники перед воротами останавливают тебя и спрашивают, куда ты идешь, ты отвечаешь что к Шляпогрызу и тебя сразу же пропускают.
Итак, ты наконец во дворце! Иди на (33).

61

Ты заходишь в комнату охраны. Как ты и ожидал, внутри полно охранников, а именно четыре штуки. Увидев тебя они орут «Не положено!» и бросаются в бой:

                                            СИЛА  ВЫНОСЛИВОСТЬ  УРОН
ПЕРВЫЙ ОХРАННИК         3                   3                         0.5
ВТОРОЙ ОХРАННИК         4                    2                         0.5
ТРЕТИЙ ОХРАННИК          3                    3                         0.5
НАЧАЛЬНИК ОХРАНЫ      5                    5                          1

Если вся охрана мертва, иди на (77).

62

От того места, где ты встретил ВОРА, ты идешь через лес на север и вскоре выходишь к реке. Через нее перекинут хлипкий деревянный мостик, по которому ты ее и переходишь. Кажется, ты уже почти достиг дворца, и вскоре ты выходишь на широкую асфальтовую дорогу, иди на (58). 

63

Ты решаешь больше не задерживаться и идешь по дороге на северо - запад. Она петляет между елок и кустов, и наконец принимает северное направление, иди на (54).

64

Ты поднимаешься по левой лестницы. На ней никакой охраны нет, поэтому вскоре ты оказываешься на втором этаже. Шляпогрыз, скорее всего, как раз тут. 
Итак, перед тобой короткий коридор всего с одной массивной дверью Зайдешь в нее (иди на (42)), или пойдешь по коридору (иди на (69))?

65

Теперь оба охранника мертвы. Ничего интересного ты у них не находишь. Теперь тебе ничего не остается, как пройти до конца коридора и подняться по лестнице, иди на (51).

66  

Ты идешь по хорошей, хоть и не асфальтированной дороге, вокруг которой растет густой хвойный лес. В этом лесу ты то и дело замечаешь разных зверей, например дятлов и белок. Но тебе не долго удается на них полюбоваться, так как вскоре ты подходишь к указателю. Он указывает на север, на нем написано «На север: скульптурная аллея, 100 м.» 
Хочешь отправиться туда (иди на (30)), или свернешь в лес и пойдешь на восток (иди на (5))?
 
67

Поплавав еще немного, ты не замечаешь больше ничего интересного. Вскоре выделенный час проходит. Ты причаливаешь к берегу и вылезаешь из катамарана. Чек ты решаешь оставить себе на память.
Отойдя от лодочной станции на десять метров, ты снова попадаешь на старую дорожку, иди на (71).

68

- Здарова мужик! Мне надо помочь!
Он долго здоровается, и вот наконец он начал рассказывать…
Мужик потерял здесь свою ручную белку. Она укусила его за палец и убежала, примерно около проката катамаранов. У этой белке есть особая примета: у нее на шее висит золотая цепочка.
Мужик говорит, что если ты поможешь ему, он заплатит тебе 200 рублей!
Что ты будешь делать? 
Поможешь мужику и выполнишь его миссию? 			Иди на (26)
Если ты передумал,							Иди на (9).

69

Коридор вскоре делится на две части: слева лестница наверх, а справа – еще один такой же коридор. Странно, что ты так и не встретил Шляпогрыза…
Пойдешь на лестницу,						Иди на (51)
Или по коридору?							Иди на (72)

70

Ты вбегаешь в эту единственную дверь и понимаешь, что нашел то, что искал! Это кабинет Шляпогрыза! Сам он сейчас одет в халат и домашние тапочки. Когда ты входишь, он говорит что бы ты принес ему чаю, но потом понимает, что ты не охранник и орет «Что ты здесь делаешь?!!!» 
Поняв, что ты не собираешься уходить, этот гад достает от куда – то из складок халата револьвер и стреляет прямо тебе в голову…
Испытай удачу. Если тебе повезло, иди на (47), если нет – на (10).

71

Минут десять дорога ведет тебя на северо – запад, и наконец выходит к неширокой, но бурной реке. Через нее перекинут хлипкий мостик. Другого пути нет, придется переходить по нему эту реку…
Иди на (36).

72

Выбранный тобой коридор вскоре поворачивает налево и ты видишь двух охранников, идущих прямо на тебя.
Ты прячешься обратно за угол.
Тебе очень не хочется с ними встречаться, но ты так и не понимаешь, заметили они тебя или нет.
Испытай удачу: если повезло, иди на (93), если нет – на (84).

73

- Сильный гад! – говоришь ты, когда ТЕЛОХРАНИТЕЛЬ падает на пол. 
Теперь ты можешь обыскать его и забрать его ПИЛО – МЕЧ (урон 2). Потом ты выходишь из этой пустой комнаты. 
Коридор вскоре кончается, и упирается в массивную дверь. Других дверей тут нет. Чтож, тебе ничего не остается, как скорей идти туда… Иди на (70).

74

Замеченное тобой строение оказывается магазином и ты сразу туда заходишь.
Продовщица тетя Люба предлагает тебе следующие товары:

Товар		             цена  	действие
ПИРОЖОК С                  15       Один раз за игру он восстановит
КАРТОШКОЙ                           одну 1 единицу ВЫНОСЛИВОСТИ.
                                                     Можешь съесть его в любое время,  
                                                     кроме битвы.
ЗЕЛЕНАЯ КОЛБА         150     Эту колбу с зельем тетя Люба
АБРАШИ                                   очень давно купила у еврея - 
                                                    Алхимика Абраши. Один раз
                                                    за игру она восстановит тебе 
                                                    одну единицу УДАЧИ.

Так же тетя Люба может купить у тебя некоторые товары по следующим ценам:

Товар                                            цена в рублях
ПАКЭТ СЭМЕЧЕК                             15
КЭПОЧКА ГОПНИКА                       10
ПИВО «СТЕПАН РАЗИН»                35
ГРЕЦКИЕ ОРЕХИ                              35

Если хочешь что – то купить, вычеркни требуемую сумму на ИГРОВОЙ КАРТЕ и впиши купленный предмет.
Ты прощаешься с тетей Любой и, выйдя из магазина, идешь дальше по дорожке на северо – восток. Иди на (91).

75

Ты подходишь к тетке.
Она долго смотрит на тебя, а патом говорит:
- Ну и чего тебе надо?
И действительно, чего тебе надо?
Хочешь напасть на нее, иди на (57). Если хочешь с ней поговорить – на (7). Если ничего не будешь делать, иди на (63).

76

Ты быстро переходишь мост и идешь по дорожке на север, иди на (58).


77

Вся охрана убита, теперь ты можешь ее обыскать. У охранников ничего интересного нет, а вот у начальника ты находишь ЭЛЕКТРОШОКЕР (урон 1). Можешь взять его с собой, сделай пометку на ИГРОВОЙ КАРТЕ. 
Потом ты выходишь из этой комнаты. 
Коридор вскоре кончается, и упирается в массивную дверь. Других дверей тут нет. Чтож, тебе ничего не остается, как скорей идти туда… Иди на (70).

78

Как только ты открываешь эту дверь, срабатывает какой – то механизм и подвешенное сбоку ружье выстреливает в тебя…
Это была одна из ловушек Шляпогрыза. Ты, совсем чуть – чуть не дошел до цели…
На этом ты и помер!...

79

Ты слезаешь с берега и прыгаешь в реку. Хорошо, хоть вода теплая!
Около получаса ты плывешь по течению, и вот наконец впереди появляется хороший деревянный мост! Тебе бы только за него ухватиться…
ИСПЫТАЙ УДАЧУ. Если тебе повезло, иди на (35), если нет – на (89).

80

 Ты сумел выжить, и теперь ты можешь приняться и за нервно визжащего Шляпогрыза!

                         СИЛА  ВЫНОСЛИВОСТЬ  УРОН
ШЛЯПОГРЫЗ    1                     2                        5

Если ты погубил этого козла, иди на (100).

81

- А, - говорит мужик, - Да я вижу, ты наш чел. А я, чего греха таить, ВОР. Ну раз уж ты тут по – понятиям, то говори, что тебе надо?
- Я хочу пробраться во дворец Екатерины второй и убить Шляпогрыза, - говоришь ты.
- Хм, Шляпогрыза, говоришь… В этом я тебе могу помочь. Конечно, я не буду помогать тебе его убивать, но я покажу тебе, как можно быстро попасть во дворец. Сначала иди через лес на север и переходи реку по мосту. Потом, когда увидишь дворец, обходи его с севера и залезай в пятое окно от угла. Там сейчас ремонт, поэтому оно открыто, а сигнализация не работает. А уж дальше как не будь сам. Да, и старайся не заходить ни в какие двери, а ходи только по коридорам и лестницам.
Ты благодаришь ВОРА, прощаешься с ним решаешь, что тебе делать? Если последуешь его совету, иди на (88), если нет – на (62). В любом случае прибавь 1 к уровню своей УДАЧИ!

82

Когда псина наконец сдохла, ты смог осмотреть дом. Ты находишь в ящике стола 100 рублей, а в холодильнике две бутылки пива «СТЕПАН РАЗИН» (отметь эти находки на ИГРОВОЙ КАРТЕ). Ты можешь выпить это пиво сейчас, или в любое время, кроме битвы. Одна бутылка восстановит одну единицу УДАЧИ. Хотя возможно, не стоит его пить, вдруг ты сможешь его потом выгодно продать…
В любом случае ты решаешь не дожидаться прихода хозяев и скорее выбегаешь из дома и идешь по дороге на север, иди на (39).

83

Ты разбегаешься и со всей силы ударяешь дверь плечем. Она вылетает внутрь, а ты по энэрции летишь следом и влетаешь башкой прям в камин…  
Это была одна из ловушек Шляпогрыза. Ты, совсем чуть – чуть не дошел до цели…
На этом ты и помер!...

84

Они все таки замечают тебя и с криком «Неположено!» бросаются в битву!

                                         СИЛА  ВЫНОСЛИВОСТЬ  УРОН
ПЕРВЫЙ ОХРАННИК      3                     2                      0.5 
ВТОРОЙ ОХРАННИК       2                     3                     0.5

Если оба они мертвы, иди на (65).

85

Ты сворачиваешь за магазин и идешь по лесу. Какое – то время все тихо, только вокруг поют птички, а патом вдруг раздается крик «ААААА!!!» и из кустов на тебя выбегает МУЖИК С ТОПОРОМ из фильма «Поворот не туда»! 
Тебе придется сразиться с ним, иди на (16).

86

Все, им конец!

                      СИЛА  ВЫНОСЛИВОСТЬ  УРОН
ПЕТРОВИЧ      2                     1                    0.1
МИХАЛЫЧ      2                     2                    0.2

Если оба БОМЖА мертвы, иди на (48).

87

Ты отдаешь ГОПНИКАМ то, что они хотели. Вычеркни деньги или сэмечки на ИГРОВОЙ КАРТЕ. Гопники гладят тебя по головки и ты скорей уходишь от туда и идешь дальше, иди на (66). 

88

Ты решаешь последовать совету ВОРА. Пройдя, как он сказал, по лесу и перейдя реку по мрсту, ты вскоре замечаешь дворец. Ты обходишь его с севера.
Иди на (40).

89

Ты хватаешься рукой за край моста, но она соскальзывает и тебя сносит дальше по течению. Ты уже порядком замерз, отними 1 от своей ВЫНОСЛИВОСТИ! 
Вскоре течение прибивает тебя к берегу, иди на (12).

90

Ты заходишь в служебный туалет. Там ничего интересного нет, поэтому ты решаешь насладиться его прелестями.
Прибавь 1 к уровню своей УДАЧИ и ВЫНОСЛИВОСТИ и иди в дальнюю дверь. Иди на (70).

91

Ты отходишь от магазина и дорожка ведет тебя между деревьев. Ты идешь почти час, но за это время ничего особенного не происходит и вскоре ты благополучно добираешься до реки, иди на (28).

92

Ты заходишь в овальную комнату, как вдруг срабатывает ловушка и на тебя с потолка падает пустое аллюминевое ведро! Отними 1 от своей ВЫНОСЛИВОСТИ! 
Ты пинаешь ведро ногой и с матюгами идешь дальше. Коридор заканчивается у очередной двери…
Иди на (70).

93

Охранники о чем – то увлеченно спорят, поэтому им не до тебя. Когда они скрываются за очередным поворотом, ты наконец можешь расслабиться!
Теперь тебе ничего не остается, как пройти до конца коридора и подняться по лестнице, иди на (51).

94

Ты подходишь к этому дому. Хозяев нет, а дверь почему – то открыта и ты входишь. 
Но не успеваешь ты переступить порог, как на тебя с лаем бросается какая – то огромная лохматая псина! Если не хочешь быть съеденным, тебе придется быстро усмирить ее!
                                      СИЛА  ВЫНОСЛИВОСТЬ  УРОН 
ЛОХМАТАЯ ПСИНА     1                     1                     0.5

Если усмирил, иди на (82).

95

Ты поднимаешься по правой мраморной лестнице. Вопреки твоим ожиданиям, на тебя никто не нападает, и ты спокойно поднимаешься на второй этаж. Перед тобой небольшой коридор без дверей и окон, иди на (72).

96

Ты быстро убегаешь от того места, где нашел белку и идешь к Мужику.
Вдруг к тебе подходят два скина и говорят, что ты сраный хач. Ты не понимаешь, почему это они так подумали, но тем не менее они уже достают кастеты. Ты тоже готовишься к бою:

                               СИЛА  ВЫНОСЛИВОСТЬ  УРОН
ПЕРВЫЙ СКИН      2                   3                        0.3
ВТОРОЙ СКИН       1                   3                        0.3

Если ты замочил скинов, то скорее беги к Мужику, пока еще кто  не будь к тебе не пристал. Иди на (31).

97

Ничего не говоря, ты набрасываешься на этого мужика:

          СИЛА  ВЫНОСЛИВОСТЬ  УРОН
ВОР       3                    1                       0.5

Если ворюга мертв, скорее беги от туда на север, иди на (62).

98

Ты входишь в Администрацию и видишь здорового мужика. У него на груди висит табличка: «ТЕЛОХРАНИТЕЛЬ». Он смотрит на тебя тупыми глазами, и, сказав «Неположено!» нападает на тебя!

                                   СИЛА  ВЫНОСЛИВОСТЬ  УРОН
ТЕЛОХРАНИТЕЛЬ     3                    3                         2

Если ты убил шкафа, иди на (73).

99

Ты заходишь в комнату и видишь трех о чем – то беседующих охранников. Завидев тебя они вскакивают с мест и с криками «Неположено!» устремляются в атаку.

                                         СИЛА  ВЫНОСЛИВОСТЬ  УРОН
ПЕРВЫЙ ОХРАННИК      3                 1                          0.5
ВТОРОЙ ОХРАННИК       2                 2                          0.5
ТРЕТИЙ ОХРАННИК        3                 3                          0.5

Если они все мертвы, иди на (59).

100

Наконец, ШЛЯПОГРЫЗ мертв! Ты сумел выполнить свою миссию! Вывалив на пол все свои веши, что ты нашел в парке, чтобы не было улик, ты выходишь из дворца, затем пересекаешь парк и вновь садишься на пригородную электричку до поселка, где ты живешь. Там тебя обязательно наградят, к тому же ты наконец то сможешь хорошенько поспать…
НА ЭТОМ ТВОЕ ПРИКЛЮЧЕНИЕ ОКОНЧЕНО!
"""


class GameCharacter:
    def __init__(self, strength=None, stamina=None, luck=None):
        """
        СИЛА: кинь один кубик, чтобы узнать начальное значение, и запиши его в поле «СИЛА» на ИГРОВОЙ КАРТЕ.
        ВЫНОСЛИВОСТЬ: кинь один кубик, чтобы узнать начальное значение, и запиши его в поле «ВЫНОСЛИВОСТЬ» на ИГРОВОЙ
                      КАРТЕ.
        УДАЧА: кинь один кубик, чтобы узнать начальное значение, и запиши его в поле «УДАЧА» на ИГРОВОЙ КАРТЕ.

        УРОН: сначала твой УРОН – 0,1.  Если ты найдешь какое нибудь оружие, то он может увеличиться. Если во время
              битвы ты наносишь удар противнику, то отними количество своего УРОНА от его ВЫНОСЛИВОСТИ, и наоборот.

        """
        self.strength = strength or d(1, 6)
        self.stamina = stamina or d(1, 6)
        self.luck = luck or d(1, 6)
        self.damage = .1

    def test_luck(self):
        """
        ПРОВЕРКА УДАЧИ: в некоторых местах тебе будет предложено ИСПЫТАТЬ УДАЧУ. Кинь один кубик: если полученное число
                        будет меньше твоей или равно УДАЧЕ, значит тебе повезло, если больше – не повезло. После каждой
                        проверки удача уменьшается на 1.

        :return:
        """
        result = d(1, 6) <= self.luck
        self.luck -= 1
        return result

    def fight(self, enemy):
        """
        БИТВЫ:

        1. Во время битвы кинь один кубик и прибавь полученное число к своей СИЛЕ. Это твоя СИЛА УДАРА.
        2. Кинь кубик, и выпавшее число прибавь к СИЛЕ противника. Это его СИЛА УДАРА.
        3. Сравнит значения. Если твоя сила удара больше, ты отнимаешь от ВЫНОСЛИВОСТИ противника число, равное твоему
           УРОНУ.
        4. Повторяй пункты 1 – 3 до полной победы или поражения.

        :param enemy:
        :return:
        """
        while self.stamina > 0 and enemy.stamina > 0:
            player_attack = d(1, 6) + self.strength
            enemy_attack = d(1, 6) + enemy.strength
            if player_attack > enemy_attack:
                enemy.get_wound(self.damage)
            elif enemy_attack > player_attack:
                self.get_wound(enemy.damage)

    def get_wound(self, damage):
        self.stamina -= damage
        if self.stamina < 0:
            self.stamina = 0
