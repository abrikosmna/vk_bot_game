correct_cities = ['абаза', 'абакан', 'абдулино', 'абинск', 'агидель', 'агрыз', 'адыгейск', 'азнакаево', 'азов',
                  'ак-довурак', 'аксай', 'алагир', 'алапаевск', 'алатырь', 'алдан', 'алейск', 'александров',
                  'александровск', 'александровск-сахалинский', 'алексеевка', 'алексин', 'алзамай', 'альметьевск',
                  'амурск', 'анадырь', 'анапа', 'ангарск', 'андреаполь', 'анжеро-судженск', 'анива', 'апатиты',
                  'апрелевка', 'апшеронск', 'арамиль', 'аргун', 'ардатов', 'ардон', 'арзамас', 'арзамас', 'аркадак',
                  'армавир', 'арсеньев', 'артём', 'артёмовск', 'артёмовский', 'архангельск', 'асбест', 'асино',
                  'астрахань', 'аткарск', 'ахтубинск', 'ачинск', 'аша', 'бабаево', 'бабушкин', 'бавлы', 'багратионовск',
                  'байкальск', 'баймак', 'бакал', 'баксан', 'балабаново', 'балаково', 'балахна', 'балахна', 'балашиха',
                  'балашов', 'балей', 'балтийск', 'барабинск', 'барнаул', 'барыш', 'батайск', 'бежецк', 'белая калитва',
                  'белая холуница', 'белгород', 'белебей', 'белёв', 'белинский', 'белово', 'белогорск', 'белозерск',
                  'белокуриха', 'беломорск', 'белорецк', 'белореченск', 'белоусово', 'белоярский', 'белый', 'бердск',
                  'березники', 'берёзовский', 'берёзовский', 'беслан', 'бийск', 'бикин', 'билибино', 'биробиджан',
                  'бирск', 'бирюсинск', 'бирюч', 'благовещенск', 'благовещенск', 'благодарный', 'бобров', 'богданович',
                  'богородицк', 'богородск', 'богородск', 'боготол', 'богучар', 'бодайбо', 'бокситогорск', 'болгар',
                  'бологое', 'болотное', 'болохово', 'болхов', 'большой камень', 'бор', 'бор', 'борзя', 'борисоглебск',
                  'боровичи', 'боровск', 'бородино', 'братск', 'бронницы', 'брянск', 'бугульма', 'бугуруслан',
                  'будённовск', 'бузулук', 'буинск', 'буй', 'буйнакск', 'бутурлиновка', 'валдай', 'валуйки', 'велиж',
                  'великие луки', 'великий новгород', 'великий устюг', 'вельск', 'венёв', 'верещагино', 'верея',
                  'верхнеуральск', 'верхний тагил', 'верхний уфалей', 'верхняя пышма', 'верхняя салда', 'верхняя тура',
                  'верхотурье', 'верхоянск', 'весьегонск', 'ветлуга', 'ветлуга', 'видное', 'вилюйск', 'вилючинск',
                  'вихоревка', 'вичуга', 'владивосток', 'владикавказ', 'владимир', 'волгоград', 'волгодонск',
                  'волгореченск', 'волжск', 'волжский', 'вологда', 'володарск', 'володарск', 'волоколамск', 'волосово',
                  'волхов', 'волчанск', 'вольск', 'воркута', 'воронеж', 'ворсма', 'ворсма', 'воскресенск', 'воткинск',
                  'всеволожск', 'вуктыл', 'выборг', 'выкса', 'выкса', 'высоковск', 'высоцк', 'вытегра',
                  'вышний волочёк', 'вяземский', 'вязники', 'вязьма', 'вятские поляны', 'гаврилов посад', 'гаврилов-ям',
                  'гагарин', 'гаджиево', 'гай', 'галич', 'гатчина', 'гвардейск', 'гдов', 'геленджик', 'георгиевск',
                  'глазов', 'горбатов', 'горбатов', 'горно-алтайск', 'горнозаводск', 'горнозаводск', 'горняк',
                  'городец', 'городец', 'городище', 'городовиковск', 'гороховец', 'горячий ключ', 'грайворон',
                  'гремячинск', 'грозный', 'грязи', 'грязовец', 'губаха', 'губкин', 'губкинский', 'гудермес', 'гуково',
                  'гулькевичи', 'гурьевск', 'гурьевск', 'гусев', 'гусиноозёрск', 'гусь-хрустальный', 'давлеканово',
                  'дагестанские огни', 'далматово', 'дальнегорск', 'дальнереченск', 'данилов', 'данков', 'дегтярск',
                  'дедовск', 'демидов', 'дербент', 'десногорск', 'дзержинск', 'дзержинск', 'дзержинский', 'дивногорск',
                  'дигора', 'димитровград', 'дмитриев-льговский', 'дмитров', 'дмитровск', 'дно', 'добрянка',
                  'долгопрудный', 'долинск', 'домодедово', 'донецк', 'донской', 'дорогобуж', 'дрезна', 'дубна',
                  'дубовка', 'дудинка', 'духовщина', 'дюртюли', 'дятьково', 'егорьевск', 'ейск', 'екатеринбург',
                  'елабуга', 'елец', 'елизово', 'ельня', 'еманжелинск', 'емва', 'енисейск', 'ермолино', 'ершов',
                  'ессентуки', 'ефремов', 'железноводск', 'железногорск', 'железногорск', 'железногорск-илимский',
                  'железнодорожный', 'жердевка', 'жигулёвск', 'жиздра', 'жирновск', 'жуков', 'жуковка', 'жуковский',
                  'завитинск', 'заводоуковск', 'заволжск', 'заволжье', 'заволжье', 'задонск', 'заинск', 'закаменск',
                  'заозёрный', 'заозёрск', 'западная двина', 'заполярный', 'зарайск', 'заречный', 'заречный', 'заринск',
                  'звенигово', 'звенигород', 'зверево', 'зеленогорск', 'зеленоградск', 'зеленодольск', 'зеленокумск',
                  'зерноград', 'зея', 'зима', 'златоуст', 'злынка', 'змеиногорск', 'знаменск', 'зубцов', 'зуевка',
                  'ивангород', 'иваново', 'ивантеевка', 'ивдель', 'игарка', 'ижевск', 'избербаш', 'изобильный',
                  'иланский', 'инза', 'инсар', 'инта', 'ипатово', 'ирбит', 'иркутск', 'исилькуль', 'искитим', 'истра',
                  'ишим', 'ишимбай', 'йошкар-ола', 'кадников', 'казань', 'калач', 'калачинск', 'калач-на-дону',
                  'калининград', 'калининск', 'калтан', 'калуга', 'калязин', 'камбарка', 'каменка', 'каменногорск',
                  'каменск-уральский', 'каменск-шахтинский', 'камень-на-оби', 'камешково', 'камызяк', 'камышин',
                  'камышлов', 'канаш', 'кандалакша', 'канск', 'карабаново', 'карабаш', 'карабулак', 'карасук',
                  'карачаевск', 'карачев', 'каргат', 'каргополь', 'карпинск', 'карталы', 'касимов', 'касли', 'каспийск',
                  'катав-ивановск', 'катайск', 'качканар', 'кашин', 'кашира', 'кедровый', 'кемерово', 'кемь', 'кизел',
                  'кизилюрт', 'кизляр', 'кимовск', 'кимры', 'кингисепп', 'кинель', 'кинешма', 'киреевск', 'киренск',
                  'киржач', 'кириллов', 'кириши', 'киров', 'киров', 'кировград', 'кирово-чепецк', 'кировск', 'кировск',
                  'кирс', 'кирсанов', 'киселёвск', 'кисловодск', 'климовск', 'клин', 'клинцы', 'княгинино', 'ковдор',
                  'ковров', 'ковылкино', 'когалым', 'кодинск', 'козельск', 'козловка', 'козьмодемьянск', 'кола',
                  'кологрив', 'коломна', 'колпашево', 'кольчугино', 'коммунар', 'комсомольск', 'комсомольск-на-амуре',
                  'конаково', 'кондопога', 'кондрово', 'константиновск', 'копейск', 'кораблино', 'кореновск', 'коркино',
                  'королёв', 'короча', 'корсаков', 'коряжма', 'костерево', 'костомукша', 'кострома', 'котельниково',
                  'котельнич', 'котлас', 'котово', 'котовск', 'кохма', 'красавино', 'красноармейск', 'красноармейск',
                  'красновишерск', 'красногорск', 'краснодар', 'краснозаводск', 'краснознаменск', 'краснознаменск',
                  'краснокаменск', 'краснокамск', 'краснослободск', 'краснослободск', 'краснотурьинск', 'красноуральск',
                  'красноуфимск', 'красноярск', 'красный кут', 'красный сулин', 'красный холм', 'кремёнки', 'кропоткин',
                  'крымск', 'кстово', 'кстово', 'кувандык', 'кувшиново', 'кудымкар', 'кузнецк', 'куйбышев', 'кулебаки',
                  'кулебаки', 'кумертау', 'кунгур', 'купино', 'курган', 'курганинск', 'курильск', 'курлово',
                  'куровское', 'курск', 'куртамыш', 'курчатов', 'куса', 'кушва', 'кызыл', 'кыштым', 'кяхта', 'лабинск',
                  'лабытнанги', 'лагань', 'ладушкин', 'лакинск', 'лангепас', 'лахденпохья', 'лебедянь', 'лениногорск',
                  'ленинск', 'ленинск-кузнецкий', 'ленск', 'лермонтов', 'лесной', 'лесозаводск', 'лесосибирск', 'ливны',
                  'ликино-дулёво', 'липецк', 'липки', 'лиски', 'лихославль', 'лобня', 'лодейное поле',
                  'лосино-петровский', 'луга', 'луза', 'лукоянов', 'лукоянов', 'луховицы', 'лысково', 'лысково',
                  'лысьва', 'лыткарино', 'льгов', 'любань', 'люберцы', 'любим', 'людиново', 'лянтор', 'магадан',
                  'магас', 'магнитогорск', 'майкоп', 'майский', 'макаров', 'макарьев', 'макушино', 'малая вишера',
                  'малгобек', 'малмыж', 'малоархангельск', 'малоярославец', 'мамадыш', 'мамоново', 'мантурово',
                  'мариинск', 'мариинский посад', 'маркс', 'махачкала', 'мглин', 'мегион', 'медвежьегорск',
                  'медногорск', 'медынь', 'межгорье', 'междуреченск', 'мезень', 'меленки', 'мелеуз', 'менделеевск',
                  'мензелинск', 'мещовск', 'миасс', 'микунь', 'миллерово', 'минеральные воды', 'минусинск', 'миньяр',
                  'мирный', 'мирный', 'михайлов', 'михайловка', 'михайловск', 'михайловск', 'мичуринск', 'могоча',
                  'можайск', 'можга', 'моздок', 'мончегорск', 'морозовск', 'моршанск', 'мосальск', 'москва',
                  'муравленко', 'мураши', 'мурманск', 'муром', 'мценск', 'мыски', 'мытищи', 'мышкин',
                  'набережные челны', 'навашино', 'навашино', 'наволоки', 'надым', 'назарово', 'назрань', 'называевск',
                  'нальчик', 'нариманов', 'наро-фоминск', 'нарткала', 'нарьян-мар', 'находка', 'невель', 'невельск',
                  'невинномысск', 'невьянск', 'нелидово', 'неман', 'нерехта', 'нерчинск', 'нерюнгри', 'нестеров',
                  'нефтегорск', 'нефтекамск', 'нефтекумск', 'нефтеюганск', 'нея', 'нижневартовск', 'нижнекамск',
                  'нижнеудинск', 'нижние серги', 'нижний ломов', 'нижний новгород', 'нижний новгород', 'нижний тагил',
                  'нижняя салда', 'нижняя тура', 'николаевск', 'николаевск-на-амуре', 'никольск', 'никольск',
                  'никольское', 'новая ладога', 'новая ляля', 'новоалександровск', 'новоалтайск', 'новоаннинский',
                  'нововоронеж', 'новодвинск', 'новозыбков', 'новокубанск', 'новокузнецк', 'новокуйбышевск',
                  'новомичуринск', 'новомосковск', 'новопавловск', 'новоржев', 'новороссийск', 'новосибирск',
                  'новосиль', 'новосокольники', 'новотроицк', 'новоузенск', 'новоульяновск', 'новоуральск',
                  'новохоперск', 'новочебоксарск', 'новочеркасск', 'новошахтинск', 'новый оскол', 'новый уренгой',
                  'ногинск', 'нолинск', 'норильск', 'ноябрьск', 'нурлат', 'нытва', 'нюрба', 'нягань', 'нязепетровск',
                  'няндома', 'облучье', 'обнинск', 'обоянь', 'обь', 'одинцово', 'ожерелье', 'озёрск', 'озёрск', 'озёры',
                  'октябрьск', 'октябрьский', 'окуловка', 'олёкминск', 'оленегорск', 'олонец', 'омск', 'омутнинск',
                  'онега', 'опочка', 'орёл', 'оренбург', 'орехово-зуево', 'орлов', 'орск', 'оса', 'осинники',
                  'осташков', 'остров', 'островной', 'острогожск', 'отрадное', 'отрадный', 'оха', 'оханск', 'очёр',
                  'павлово', 'павлово', 'павловск', 'павловский посад', 'палласовка', 'партизанск', 'певек', 'пенза',
                  'первомайск', 'первомайск', 'первоуральск', 'перевоз', 'перевоз', 'пересвет', 'переславль-залесский',
                  'пермь', 'пестово', 'петров вал', 'петровск', 'петровск-забайкальский', 'петрозаводск',
                  'петропавловск-камчатский', 'петухово', 'петушки', 'печора', 'печоры', 'пикалёво', 'пионерский',
                  'питкяранта', 'плавск', 'пласт', 'плёс', 'поворино', 'подольск', 'подпорожье', 'покачи', 'покров',
                  'покровск', 'полевской', 'полесск', 'полысаево', 'полярные зори', 'полярный', 'поронайск', 'порхов',
                  'похвистнево', 'почеп', 'починок', 'пошехонье', 'правдинск', 'приволжск', 'приморск',
                  'приморско-ахтарск', 'приозерск', 'прокопьевск', 'пролетарск', 'протвино', 'прохладный', 'псков',
                  'пугачёв', 'пудож', 'пустошка', 'пучеж', 'пушкино', 'пущино', 'пыталово', 'пыть-ях', 'пятигорск',
                  'радужный', 'радужный', 'райчихинск', 'раменское', 'рассказово', 'ревда', 'реж', 'реутов', 'ржев',
                  'родники', 'рославль', 'россошь', 'ростов великий', 'ростов-на-дону', 'рошаль', 'ртищево', 'рубцовск',
                  'рудня', 'руза', 'рузаевка', 'рыбинск', 'рыбное', 'рыльск', 'ряжск', 'рязань', 'салават', 'салаир',
                  'салехард', 'сальск', 'самара', 'санкт-петербург', 'саранск', 'сарапул', 'саратов', 'саров', 'саров',
                  'сасово', 'сатка', 'сафоново', 'саяногорск', 'саянск', 'светлогорск', 'светлоград', 'светлый',
                  'светогорск', 'свирск', 'свободный', 'себеж', 'северобайкальск', 'северодвинск', 'северо-курильск',
                  'североморск', 'североуральск', 'северск', 'севск', 'сегежа', 'сельцо', 'семёнов', 'семёнов',
                  'семикаракорск', 'семилуки', 'сенгилей', 'серафимович', 'сергач', 'сергач', 'сергиев посад',
                  'сердобск', 'серов', 'серпухов', 'сертолово', 'сибай', 'сим', 'сковородино', 'скопин', 'славгород',
                  'славск', 'славянск-на-кубани', 'сланцы', 'слободской', 'слюдянка', 'смоленск', 'снежинск',
                  'снежногорск', 'собинка', 'советск', 'советск', 'советск', 'советская гавань', 'советский', 'сокол',
                  'солигалич', 'соликамск', 'солнечногорск', 'сольвычегодск', 'соль-илецк', 'сольцы', 'сорочинск',
                  'сорск', 'сортавала', 'сосенский', 'сосновка', 'сосновоборск', 'сосновый бор', 'сосногорск', 'сочи',
                  'спас-деменск', 'спас-клепики', 'спасск', 'спасск-дальний', 'спасск-рязанский', 'среднеколымск',
                  'среднеуральск', 'сретенск', 'ставрополь', 'старая русса', 'старица', 'стародуб', 'старый оскол',
                  'стерлитамак', 'стрежевой', 'строитель', 'струнино', 'ступино', 'суворов', 'суджа', 'судогда',
                  'суздаль', 'суоярви', 'сураж', 'сургут', 'суровикино', 'сурск', 'сусуман', 'сухиничи', 'сухой лог',
                  'сходня', 'сызрань', 'сыктывкар', 'сысерть', 'сычевка', 'сясьстрой', 'тавда', 'таганрог', 'тайга',
                  'тайшет', 'талдом', 'талица', 'тамбов', 'тара', 'таруса', 'татарск', 'таштагол', 'тверь', 'теберда',
                  'тейково', 'темников', 'темрюк', 'терек', 'тетюши', 'тимашевск', 'тихвин', 'тихорецк', 'тобольск',
                  'тогучин', 'тольятти', 'томари', 'томмот', 'томск', 'топки', 'торжок', 'торопец', 'тосно', 'тотьма',
                  'трехгорный', 'троицк', 'троицк', 'трубчевск', 'туапсе', 'туймазы', 'тула', 'тулун', 'туран',
                  'туринск', 'тутаев', 'тында', 'тырныауз', 'тюкалинск', 'тюмень', 'уварово', 'углегорск', 'углич',
                  'удачный', 'удомля', 'ужур', 'узловая', 'улан-удэ', 'ульяновск', 'унеча', 'урай', 'урень', 'урень',
                  'уржум', 'урус-мартан', 'урюпинск', 'усинск', 'усмань', 'усолье', 'усолье-сибирское', 'уссурийск',
                  'усть-джегута', 'усть-илимск', 'усть-катав', 'усть-кут', 'усть-лабинск', 'устюжна', 'уфа', 'ухта',
                  'учалы', 'уяр', 'фатеж', 'фокино', 'фокино', 'фролово', 'фрязино', 'фурманов', 'хабаровск',
                  'хадыженск', 'ханты-мансийск', 'харабали', 'харовск', 'хасавюрт', 'хвалынск', 'хилок', 'химки',
                  'холм', 'холмск', 'хотьково', 'цивильск', 'цимлянск', 'чадан', 'чайковский', 'чапаевск', 'чаплыгин',
                  'чебаркуль', 'чебоксары', 'чегем', 'чекалин', 'челябинск', 'чердынь', 'черемхово', 'черепаново',
                  'череповец', 'черкесск', 'чёрмоз', 'черноголовка', 'черногорск', 'чернушка', 'черняховск', 'чехов',
                  'чистополь', 'чита', 'чкаловск', 'чкаловск', 'чудово', 'чулым', 'чусовой', 'чухлома', 'шагонар',
                  'шадринск', 'шали', 'шарыпово', 'шарья', 'шатура', 'шахтёрск', 'шахты', 'шахунья', 'шахунья', 'шацк',
                  'шебекино', 'шелехов', 'шенкурск', 'шилка', 'шимановск', 'шиханы', 'шлиссельбург', 'шумерля',
                  'шумиха', 'шуя', 'щёкино', 'щёлково', 'щербинка', 'щигры', 'щучье', 'электрогорск', 'электросталь',
                  'электроугли', 'элиста', 'энгельс', 'эртиль', 'юбилейный', 'югорск', 'южа', 'южно-сахалинск',
                  'южно-сухокумск', 'южноуральск', 'юрга', 'юрьевец', 'юрьев-польский', 'юрюзань', 'юхнов', 'ядрин',
                  'якутск', 'ялуторовск', 'янаул', 'яранск', 'яровое', 'ярославль', 'ярцево', 'ясногорск', 'ясный',
                  'яхрома']
