﻿TOOLTIPS_DICT = {}
TOOLTIPS_DICT['price'] = u"<img style = 'float:left;' src=\"{{ url_for('static', filename='img/tooltip.png') }}\" alt=\"Далее\"/>\
<div class = 'tooltip-text'> <p>Значение определяет на сколько увеличится важность <b>цены</b> \
в подбираемой модели в ущерб остальным параметрам. </p> </br> <p> В точке 0 &mdash; &Prime;разумная цена&Prime;.</p>"

TOOLTIPS_DICT['performance'] = u"<img style = 'float:left;' src=\"{{ url_for('static', filename='img/tooltip.png') }}\" alt=\"Далее\"/>\
<div class = 'tooltip-text'> <p>Значение определяет на сколько увеличится важность параметра <b>производительности</b> \
в подбираемой модели в ущерб остальным параметрам. </p> </br> <p> В точке 0 &mdash; стандартные требование к производительности.</p>"

TOOLTIPS_DICT['video'] = u"<img style = 'float:left;' src=\"{{ url_for('static', filename='img/tooltip.png') }}\" alt=\"Далее\"/>\
<div class = 'tooltip-text'> <p>Значение определяет на сколько увеличится важность <b>видеокарты</b> \
в подбираемой модели в ущерб остальным параметрам. </p> </br> <p> В точке 0 &mdash; стандартные требование к видеокарте.</p>"

TOOLTIPS_DICT['battery'] = u"<img style = 'float:left;' src=\"{{ url_for('static', filename='img/tooltip.png') }}\" alt=\"Далее\"/>\
<div class = 'tooltip-text'> <p>Значение определяет на сколько увеличится важность длительности работы <b>батареи</b> \
в подбираемой модели в ущерб остальным параметрам. </p> </br> <p> В точке 0 &mdash; стандартные требование к батарее.</p>"

TOOLTIPS_DICT['weight'] = u"<img style = 'float:left;' src=\"{{ url_for('static', filename='img/tooltip.png') }}\" alt=\"Далее\"/>\
<div class = 'tooltip-text'> <p>Значение определяет на сколько увеличится важность минимизации <b>веса</b> \
в подбираемой модели в ущерб остальным параметрам. </p> </br> <p> Чем больше значение, тем больший приоритет будут иметь более легкие модели.</p>"

TOOLTIPS_DICT['size'] = u"<img style = 'float:left;' src=\"{{ url_for('static', filename='img/tooltip.png') }}\" alt=\"Далее\"/>\
<div class = 'tooltip-text'> <p>Значение определяет на сколько увеличится важность <b>компактности</b> модели \
в подбираемой модели в ущерб остальным параметрам. </p> </br> <p> Чем больше значение, тем больший приоритет будут иметь более компактные модели.</p>"

#--------------------------------------------------------------------------------------

TOOLTIPS_DICT[u'bluray'] = u"<p>MY test</p>"

#--------------------------------------------------------------------------------------

TOOLTIPS_DICT[u'Тип памяти'] = u"<p>В современных ПК используется оперативная память типа <b>SDRAM</b> (<i>Synchronous\
Dynamic Random Access Memory</i>). Этот тип памяти получил развитие в виде\
модулей памяти <b>DDR</b> (<i>Double Data Rate</i>), DDR2, DDR3, DDR4. Каждая из них\
вдвое увеличивает частоту передачи данных от предыдущей версии.\
</p></br><p>Модуль <b>SO-DIMM</b> (<i>Small Outline Dual In-line Memory Module</i>) является\
уменьшенным аналогом к SDRAM и не отличается по производительности.\
 Данный тип памяти обычно встраивают в ноутбуки, нетбуки и т.д.</p>"

TOOLTIPS_DICT[u'Тактовая частота'] = u"<p>Тактовая частота оперативной памяти определяет ее пропускную способность, \
	что напрямую влияет на ее производительность. Но необходимо помнить, что эта частота должна соответствовать частоте материнской платы.</p>"    

TOOLTIPS_DICT[u'Кол-во слотов'] = u"<p>Количество слотов в материнской плате для установки плат оперативной памяти.</p>"   

TOOLTIPS_DICT[u'Объем ОЗУ'] = u"<p>Объем оперативной памяти определяет количество задач, которые одновременно может \
	выполнять ПК. Вместе с частотой процессора определяет быстродействие компьютера. Чем больше оперативной \
	памяти, тем более сложные приложения он сможет выполнить. При этом чипсет должен поддерживать такой \
	объем.</p><p>Также для объема в 4ГБ или более должна быть обязательно установлена как минимум 64-битная \
	операционная система.</p>"   

TOOLTIPS_DICT[u'Частота процессора'] = u"<p>Тактовая частота процессора показывает количество выполняемых \
	операций на единицу времени, т.е. чем она выше, тем больше операций может выполнить процессор. \
	От ее величины зависит часть производительности ПК.</p>"

TOOLTIPS_DICT[u'Кол-во ядер'] = u"<p>Многоядерность разделяет простые процессы (как то работа с аудио, видео, \
	а также изображениями) на составляющие и обрабатывает их параллельно, что позволяет закончить процесс \
	быстрее. Многоядерные процессоры используются, как правило, для мультимедийных, а также игровых ПК. Более \
	дешевые одноядерные процессоры устанавливаются для офисных приложений, не требующих мощных ПК.</p>"

TOOLTIPS_DICT[u'Объем видеопамяти'] = u"<p>Объем видеопамяти отвечает за производительность самой \
	видеокарты. Чем больше собственной памяти она имеет, тем более качественно будут \
	отображаться сложная графика и текстуры.</p>"

TOOLTIPS_DICT[u'Тип видеокарты'] = u"<p><b>Встроенная</b> (или <i>интегрированная</i>) видеокарта – видеопроцессор, \
	который встраивается в чипсет материнской платы или в центральный процессор. Зачастую она \
	не обладает собственной памятью и мощным видеочипом, поэтому подходит лишь для простого воспроизведения графики.</p></br><p>Для \
	<b>дискретной</b> видеокарты предназначен специальный слот в материнской плате. Она отличается более \
	значительной производительностью, вследствие чего, и большим тепловыделением. Потребляет намного больше \
	энергии, а также существенно повышает цену ПК.</p></br><p><b>Гибридная</b> видеокарта состоит как из <i>встроенного</i> \
	адаптера, так и <i>дискретного</i>. Это позволяет использовать <i>интегрированную</i> видеокарту при воспроизведении несложной графики, и \
	автоматически переключать на более мощную – <i>дискретную</i> – при усложненной графике. Благодаря \
	этому значительно снижается энергопотребление, что существенно для переносных устройств: ноутбуков, нетбуков и т.д.</p>"

TOOLTIPS_DICT[u'Внутренних отсеков 3.5'] = u"<p>Количество отсеков в системном блоке для установки винчестеров</p>"

TOOLTIPS_DICT[u'Емкость накопителя'] = u"<p>Объем долговременной памяти для хранения данных (установленная \
	ОС, программы и приложения, игры; рабочие файлы, фильмы, музыка, книги и т.д.).</p>"

TOOLTIPS_DICT[u'Тип накопителя'] = u"<p>Основное преимущество <b>SSD</b>-накопителей – это высокая скорость чтения/записи. \
	Такие процессы как архивирование, перемещение файлов, а также загрузка ОС или вход/выход из состояния \
	гибернации происходят в разы быстрее. Также у них ниже энергопотребление, отсутствует шум. Устойчивы к \
	падениям. Цена прямо пропорциональна размеру, что делает SSD-носители более дорогими.</p></br><p><b>HDD</b>-накопитель \
	меньше изнашивается: ячейки памяти служат дольше, хотя он сильно подвержен механическим и магнитным \
	воздействиям. Небольшая цена при больших объемах.</p>"
	
TOOLTIPS_DICT[u'Обороты шпинделя'] = u"<p>От скорости вращения шпинделя зависит время доступа к информации \
	хранимой на винчестере, а также скорость записи/считывания данных. Сегодня средней скоростью \
	работы шпинделя считается 7200 об/мин, но для серверов и высокопроизводительных рабочих \
	станций необходимо 10 000 – 15 000 об/мин. </p>"
	
TOOLTIPS_DICT[u'Мощность БП'] = u"<p>От мощности блока питания (БП) зависит работа всего ПК. Этот \
	параметр должен рассчитываться в зависимости от потребляемой мощности всех компонентов \
	системы: процессора, видеокарты и др. К полученному значению добавляется еще 10-25% для \
	того, чтобы блок питания не работал все время на полную мощность.</p>"	
	
TOOLTIPS_DICT[u'Чипсет'] = u"<p>Чипсет – один из важнейших элементов материнской платы, который \
	обеспечивает взаимодействие между памятью, процессором, видеадаптером, устройствами \
	ввода/вывода и другими компонентами ПК. Наиболее популярными производителями чипсетов \
	являются AMD, Intel, ATI, NVIDIA. </p>"		
	
TOOLTIPS_DICT[u'Сеть'] = u"<p><b>Wi-Fi</b> адаптер – устройство, позволяющее подключить ПК (или \
	другие устройства: мышь, принтер и др.) к локальной беспроводной компьютерной сети. На \
	сегодняшний день зачастую используется стандарт 802.11g, обеспечивающий максимальную скорость \
	до 54 Мбит/с. Кроме этого  набирает популярность 802.11n, дающий скорость передачи данных \
	до 320 Мбит/с.</p></br><p><b>Bluetooth</b> - беспроводная технология обмена данными на \
	коротких дистанциях (до 10-100 метров в зависимости от класса устройства). Используется \
	для подключения и обмена информацией в ряде устройств: компьютеры (как персональные, так \
	и ноутбуки), КПК, мобильные телефоны, мышки, принтеры, фотоаппараты, джойстики и др.</p></br><p>\
	Разъем <b>LAN</b> (<i>Local Area Network</i>) предназначен для подключения сетевого \
	кабеля к ПК, таким образом делая ПК частью локальной компьютерной сети.</p>"

TOOLTIPS_DICT[u'USB 2.0'] = u"<p><b>USB 2.0</b> - универсальный интерфейс обмена данными, позволяющий \
	подключить к ПК множество устройств: клавиатура, мишь, принтер, сканер, \
	флешки и др. Передача информации между внешними устройствами и ПК осуществляется \
	на скорости до 480 Мбит/с.</p>"
	
TOOLTIPS_DICT[u'USB 3.0'] = u"<p><b>USB 3.0</b> - новый улучшеный стандарт USB. Отличается \
	существенно большей скоростью обмена данными - до 5 Гбит/с, при чем обмен осуществляется \
	одновременно в оба направления: на прием и на передачу данных. Разъемы и кабели остаются \
	функционально совместимыми со стандартом USB 2.0. Также новая версия обладает большей \
	силой тока, что может избавить некоторые внешние устройства от дополнительных блоков питания.</p>"		

TOOLTIPS_DICT[u'Отсеков 5.25"'] = u"<p>Количество отсеков размера 5.25\", которые \
	используются для установки оптических приводов CD/DVD.</p>"		
	
TOOLTIPS_DICT[u'Отсеков 3.5"'] = u"<p>Количество отсеков размера 3.5\", которые \
	используются для установки кардридера или Floppy-дисковода.</p>"		
	
TOOLTIPS_DICT[u'Разъемов USB 2.0'] = u"<p>Количество разъемов стандарта USB 2.0.</p>"

TOOLTIPS_DICT[u'Разъемов USB 3.0'] = u"<p>Количество разъемов стандарта USB 3.0.</p>"	

TOOLTIPS_DICT[u'Звук'] = u"<p>Параметр характеризует объемность звука. На сегодняшний день \
	варьируется от 1 (моно) до 11 (наиболее объемный), обозначая количество полнодиапазонных \
	каналов (громкоговорителей).\
	<a href = 'http://ru.wikipedia.org/wiki/%D0%9E%D0%B1%D1%8A%D1%91%D0%BC%D0%BD%D1%8B%D0%B9_%D0%B7%D0%B2%D1%83%D0%BA#.D0.9A.D0.BE.D0.BD.D1.84.D0.B8.D0.B3.D1.83.D1.80.D0.B0.D1.86.D0.B8.D0.B8_.D0.B3.D1.80.D0.BE.D0.BC.D0.BA.D0.BE.D0.B3.D0.BE.D0.B2.D0.BE.D1.80.D0.B8.D1.82.D0.B5.D0.BB.D0.B5.D0.B9'>\
	Подробнее об объемном звуке</a> </p>\
	<p>В системе 7.1 воспроизводится полное (360 градусов вокруг слушателя) звуковое поле.</p><p>\".1\" обозначает \
	воспроизведение низкочастотных звуковых эффектов (сабвуфер)</p>"	
	
TOOLTIPS_DICT[u'Кардридер'] = u"<p>Кардридер - устройство для считывания и записи \
	информации на карты памяти (SD, miniSD, microSD), которые сейчас часто \
	используются в фотоаппаратах, электронных книгах, мобильных телефонах и др.</p>"	
	
TOOLTIPS_DICT[u'Привод'] = u"<p>Оптический лазерный привод – устройство, использующееся для \
	чтения, возможно, и записи информации на компакт-диски.</p></br><p><b>CD-ROM</b> – возможность \
	только чтения, <b>CD-RW</b> – возможность чтения и записи CD-дисков (700 МБ). Теряет \
	свою популярность.</p></br><p><b>DVD-ROM</b> – возможность только чтения, <b>DVD-RW</b> – \
	возможность, как чтения, так и записи на DVD-диск (однослойный 4.5ГБ, двухслойный – 8ГБ).</p></br>\
	<p><b>BD-ROM</b> – возможность чтения BD-дисков (<i>Blu-ray Disk</i>), которые обычно \
	служат в качестве носителя фильма высокого разрешения. Приводы <b>BD-RE</b> –имеют возможность \
	чтения/записи BD-дисков. Такие диски имеют объем по 25ГБ или 50ГБ.</p></br><p><b>HD-DVD-ROM</b> – \
	приводы позволяющие считывать информацию с HD-DVD-дисков – главного конкурента BD. Они также \
	хранят видео высокого разрешения (HDTV). Приставка <b>RW</b> означает, что информацию можно как \
	читать, так и записывать. Размер вмещаемой информации на HD-DVD может составлять 15ГБ (однослойные), \
	30ГБ (двухслойные) и по 45ГБ (трехслойные).</p></br><p>Обычно более дорогие BD и HD приводы могут \
	считывать (записывать) информацию и на обычные CD, DVD диски.</p>"

TOOLTIPS_DICT[u'Разрешение'] = u"<p>Разрешение - размер экрана по горизонтали-вертикали в пикселях. Чем \
	больше разрешение экрана, тем четче воспроизводится на экране картинка. Этот показатель \
	особенно важен для больших экранов, чем больше разрешение, тем меньше заметна зернистость \
	пикселей, но тем больше ресурсов видеокарты требуется.</p>"	
	
TOOLTIPS_DICT[u'LED подсветка'] = u"<p>Жидко-кристаллические экраны, чья матрица освещается светодиодами \
	(<b>LED</b> - <i>Light Emitting Diode</i>) имеет ряд преимуществ, в сравнении, с \
	подсветкой люминесцентными лампами: улучшенные контрастность и передача цвета, уменьшенное \
	энергопотребление, малая толщина монитора.</p>"	
	
TOOLTIPS_DICT[u'Диагональ экрана'] = u"<p>Диагональ экрана - размер экрана по диагонали в дюймах.</p>"	

TOOLTIPS_DICT[u'Сенсорный экран'] = u"<p>Сенсорный экран - экран, чувствителен к прикосновениям, при нажатии \
	пальцем производит действия эквивалентны нажатию мышкой.</p>"	

TOOLTIPS_DICT[u'Пульт ДУ'] = u"<p>Пульт дистанционного управления (ДУ) - позволяет управлять компьютером, в основном, его мультимедийной частью: \
	управление громкостью, запуск следующей/предыдущей дорожки и т.д.</p>"	

TOOLTIPS_DICT[u'ТВ-тюнер'] = u"<p>Встроенный в компьютер ТВ-тюнер позволяет принимать телевизионные \
	сигналы и использовать ПК в качестве телевизора.</p>"	
	
TOOLTIPS_DICT[u'Разъемов 3.5 мм'] = u"<img style = 'float:left; margin: 5px;' src=\"{{ url_for('static', filename='img/miniJack.jpg') }}\" alt=\"miniJack\"/>\
	<p>Количество разъемов <b>mini-Jack</b>, которые используются для подключения \
	наушников, микрофона, колонок или другой акустической системы.</p>"	
	
TOOLTIPS_DICT[u'PS2'] = u"<img style = 'float:left; margin: 5px;' src=\"{{ url_for('static', filename='img/ps-2.jpeg') }}\" alt=\"img ps-2\"/>\
	<p><b>PS/2</b> - порт, предназначен для подключению к ПК клавиатуры и мыши с соответствующими кабелями. На сегодня \
	практически полностью утратил свою популярность.</p>"		

TOOLTIPS_DICT[u'Thunderbolt'] = u"<img style = 'float:left;' src=\"{{ url_for('static', filename='img/Thunderbolt.jpeg') }}\" alt=\"img Thunderbolt\"/>\
	<p><b>Thunderbolt</b> (или <i>Light Peak</i>) - новый интерфейс высокоскоростного подключения для различных периферийных \
	устройтсв, начавший выпускаться лишь в 2011 году. Объединяет в себе возможности нескольких стандартов, предполагается как \
	замена некоторым из них. Геометрически разъем схож с разъемом MDP (<i>Mini DisplayPort</i>). Устройства, для которых \
	подходит разъем MDP, могут использоваться и с разъемами <i>Thunderbolt.</i></p>"	
	
TOOLTIPS_DICT[u'Разъемы'] = u"<img style = 'float:left; margin: 5px;' src=\"{{ url_for('static', filename='img/VGA.jpeg') }}\" alt=\"img VGA\"/>\
	<p><b>VGA</b> (<i>Video Graphics Array</i>)- интерфейс, который предназначен для подключения аналоговых мониторов и \
	телевизоров. На сегодняшний день активно вытесняется цифровыми интерфейсами: DVI, HDMI, DisplayPort и другими.</p></br>\
	<img style = 'float:right;margin: 5px;' src=\"{{ url_for('static', filename='img/DVI.jpeg') }}\" alt=\"img DVI\"/></br></br></br>\
	<p><b>DVI</b> (<i>Digital Visual Interface</i>) - интерфейс, который предназначен для подключения цифровых устройств \
	отображения: жидкокристаллические мониторы, телевизоры и проекторы. По DVI идет только передача видеоизображения без \
	звука. Пропускная способностью до 3.4 Гбит/с на каждый из трех каналов.</p></br>\
	<img style = 'float:left;margin: 5px;' src=\"{{ url_for('static', filename='img/HDMI.jpeg') }}\" alt=\"img HDMI\"/>\
	<p><b>HDMI</b> (<i>High-Definition Multimedia Interface</i>) - интерфейс для передачи мультимедийного \
	контента (видео и звук) с большой пропускной способностью от 4.9 до 10.2 Гбит/с, что позволяет передавать \
	видеоизображение высокого разрешения (HD). Стандартная длина кабеля - до 10 метров, с помощью усилителей \
	сигнала можно продлить до 20-30 метров.</p></br>\
	<img style = 'float:right;margin: 5px;' src=\"{{ url_for('static', filename='img/DisplayPort.jpeg') }}\" alt=\"img DisplayPort\"/>\
	<p><b>DisplayPort</b> - разъем предназначен для передачи видео и звука хорошего качества (HD) на другие \
	цифровые устройства. Схож с HDMI, отличается большей скоростью передачи информации 10.8 Гбит/с, а также \
	максимальной длиной кабеля без дополнительных усилителей - до 15 метров.</p></br>\
	<img style = 'float:left;margin: 5px;' src=\"{{ url_for('static', filename='img/mini-displayPort.jpg') }}\" alt=\"img mini-displayPort\"/>\
	<p><b>Mini DisplayPort</b> – минимизированная версия DisplayPort, выполняющая те же функции. Является общепринятым \
	разъемом в продуктах Apple.</p></br>\
	<img style = 'float:right;margin: 5px;' src=\"{{ url_for('static', filename='img/IEEE1394.jpeg') }}\" alt=\"img IEEE1394\"/>\
	<p><b>IEEE 1394</b> – высокоскоростной интерфейс, предназначение которого соединять различные устройства \
	(ПК, видеокамеры, принтеры, внешние жесткие диски) между собой, при этом скорость передачи данных от 400 \
	до 3200 Мбит/с в зависимости от спецификации. Более того, устройства, которые потребляют небольшое количество \
	электроэнергии, могут обходиться без дополнительного блока питания.</p></br>\
	<img style = 'float:left;margin: 5px;' src=\"{{ url_for('static', filename='img/eSATA-USB.jpeg') }}\" alt=\"img eSATA-USB\"/>\
	<p><b>eSATA/USB</b> – порт предназначен для подключения внешних жестких носителей или устройства с USB выходом, \
	обеспечивает при этом скорость передачи данных до 3Гбит/с.</p></br>\
	<img style = 'float:right;margin: 5px;' src=\"{{ url_for('static', filename='img/COM-port.jpeg') }}\" alt=\"img COM-port\"/>\
	<p><b>COM-порт</b> ранее был предназначен для подключения терминалов, модемов, кассовых аппаратов. Практически \
	полностью вытеснен USB, используется лишь в узкоспециализированном оборудовании.</p></br>\
	<img style = 'float:left;margin: 5px;' src=\"{{ url_for('static', filename='img/SPDIF.jpeg') }}\" alt=\"img SPDIF\"/></br></br></br>\
	<p><b>S/P-DIF</b> – узкоспециализированный разъем, предназначен для подключения профессиональной \
	акустической аппаратуры. Может быть оптическим или коаксиальным разъемом.</p>"



TOOLTIPS_DICT[u'RAID массив'] = u"<p>Цепочка из двух или более жестких носителей, связанных между собой. Воспринимаются \
	операционной системой, как единственный винчестер.</p>"		

TOOLTIPS_DICT[u'Датчик свободного падения'] = u"<p>Датчик свободного падения определяет в каком состоянии находятся ноутбук: неподвижном, \
	малоподвижном или в процессе падения. В последнем случае датчик успевает подать сигнал на жесткий диск, \
	который, в свою очередь, снимает считывающие головки с дисков, предотвращая тем самым потерю информации, \
	хранящуюся на жестком носителе.</p>"		
	
TOOLTIPS_DICT[u'Конструкция клавиш'] = u"<p><img style = 'float:left;' src=\"{{ url_for('static', filename='img/KeysIlandType.jpg') }}\" alt=\"img KeysIlandType\"/>\
	Наиболее распространенной на сегодняшний день является <b>островная</b> конструкция \
	клавиш. Характеризуется большим расстоянием между клавишами, а также отсутствием  зазоров между \
	ними: клавиши являются \"островками\" в основании клавиатуры, в которой проделаны соответствующие \
	отверстия.</p></br>\
	<p><img style = 'float:right;' src=\"{{ url_for('static', filename='img/KeysClassicType.jpg') }}\" alt=\"img KeysClassicType\"/>\
	<b>Классическая</b> и <b>монолитная</b> конструкция внешним видом практически не \
	отличается. Однако, у монолитных клавиатурах зазор между клавишами немного меньше, чем у классических.<p></br>\
	<p><img style = 'float:left;' src=\"{{ url_for('static', filename='img/KeysSensorType.jpg') }}\" alt=\"img KeysSensorType\"/>\
	Некоторые ноутбуки оснащены <b>сенсорной</b> клавиатурой, которая представляется совершенно \
	плоской и гладкой. Такой клавиатуре не страшны попадание влаги или крошек, но и цена становится значительно \
	дороже.</p>"
		
TOOLTIPS_DICT[u'Num блок'] = u"<p>Num блок - присутствие на клавиатуре панели цифровых клавиш. Oбычно \
	присутствует на ноутбуках с большой диагональю экрана и размещается справа.</p>"
		
TOOLTIPS_DICT[u'Манипулятор'] = u"<p><b>Тouchpad</b> - сенсорная панель, обычно расположена под основной клавиатурой. \
	Перемещение пальца на панели соответствует перемещению курсора на экране.</p></br>\
	<p><b>Trackpoint</b> - неболшой джойстик, располагаемый посреди клавиатуры между клавишами. Управление \
	джойстиком соответствует перемещению курсора на экране.</p>"
		
TOOLTIPS_DICT[u'Поддержка мультитач'] = u"<p>Поддержка мультитач - способность сенсорного устройства распознавать движение сразу \
	нескольких пальцев: используется для изменения масштаба изображения, прокрутки и др.</p>"
			
	
TOOLTIPS_DICT[u'Кол-во дополнительных клавиш'] = u"<p>Дополнительные клавиши на клавиатуре играют роль управления неосновными ее \
	функциями: звук (громкость, след. дорожка), питание (выключение, переход в ждущий режим, в режим гибернации), \
	вызов программ (браузер или электронная почта).</p>"
		
TOOLTIPS_DICT[u'Wi-Di (беспроводной)'] = u"<p>Wi-Di (<i>Wireless Display</i>) - технология беспроводной передачи видеоизображения \
	высокого разрешения (HD) и звука 5.1 от ноутбука или ПК на совместимый дисплей. Основан на стандарте Wi-Fi.</p>"	
	
TOOLTIPS_DICT[u'WiMAX-модуль'] = u"<p>WiMAX-модуль обеспечивает поддержку технологии WiMAX - беспроводная \
	передача данных на большие расстояния до 80 км с гораздо большей скоростью - до 70 Мбит/с, которая \
	уменьшается с увеличением расстояния (на практике: 10 Мбит/с на расстоянии 10 км при прямой видимости).</p>"	
	
TOOLTIPS_DICT[u'Слот расширения'] = u"<p>Слот расширения предназначен для подключения \
	дополнительных плат (звуковых, сетевых, видео) или адаптеров (Wi-Fi, модем, TV-тюнер), не входящих в основную \
	поставку. Обычно присутствует в настольных ПК, в ноутбуках встречается реже, т.к. ноутбуки являются малогабаритными.</p>"	
	
TOOLTIPS_DICT[u'DialUp модем'] = u"<p>DialUp модем позволяет подключиться к сети Интернет через телефонную сеть.</p>"	
	
TOOLTIPS_DICT[u'3G модем'] = u"<p>3G модем позволяет получить доступ к Интернету на основе мобильной сети. Достоинство \
	такого подключения - возможность передвижения, не утрачивая при этом соединение с сетью. Скорость передачи \
	пакетов данных уменьшается с увеличением скорости движения и составляет:</p><p>до 144 Кбит/с при быстром движении \
	объектов (скорость до 120 км/ч);</p><p>до 384 Кбит/с для медленно движущихся объектов (до 3 км/ч);</p><p>до 2048 Кбит/с в \
	состоянии неподвижности.</p>"	
	
TOOLTIPS_DICT[u'Bluetooth'] = u"<p><b>Bluetooth</b> - беспроводная технология обмена данными на \
	коротких дистанциях (до 10-100 метров в зависимости от класса устройства). Используется \
	для подключения и обмена информацией в ряде устройств: компьютеры (как персональные, так \
	и ноутбуки), КПК, мобильные телефоны, мышки, принтеры, фотоаппараты, джойстики и др.</p>"	

TOOLTIPS_DICT[u'Тип слота расширения'] = u"<p><b>PCMCIA</b> или <b>ExpressCard</b> слоты играют одну и ту же роль – для установки дополнительных \
	плат или адаптеров. Они не являются совместимыми и устройства предназначенные для <b>PCMCIA</b> невозможно использовать \
	со слотом типа <b>ExpressCard</b> или наоборот. Оба формата вытесняются новым интерфейсом USB 3.0.</p>"	

TOOLTIPS_DICT[u'NFC-чип'] = u"<p><b>NFC</b> (<i>Near Field Communication</i>) чип представляет собой устройство имеющее характеристики \
	бесконтактных смарткарт и характеристики считывателя в одном лице. Взаимодействует на коротких расстояниях - до 20 см. Пока что, \
	только начинает набирать популярность в виде внедрения в смартфоны, но в целом еще не распространен.</p>\
	<p>Как и смарткарта, позволяет производить быстрое считывание информации с ноутбука за короткое время на \
	близком расстоянии до 20 см.</p>\
	<p>Как считыватель, позволяет получить информацию с других бесконтактных карт и RFID меток (данная технология \
	используется в траспортных проездных документах, в идентификации товаров в супермаркетах, в качестве электронных \
	ключей в номерах гостинниц и др.).</p>\
	<p>Также устройство имеющее NFC-чип может использоваться в связке с другим устройством имеющим его для обмена данными. \
	В будущем планируется использовать в качестве электронных денег, удостоверений личности и др.</p>"	

TOOLTIPS_DICT[u'Wi-Fi'] = u"<p><b>Wi-Fi</b> адаптер – устройство, позволяющее подключить ПК (или \
	другие устройства: мышь, принтер и др.) к локальной беспроводной компьютерной сети. На \
	сегодняшний день зачастую используется стандарт 802.11g, обеспечивающий максимальную скорость \
	до 54 Мбит/с. Кроме этого  набирает популярность 802.11n, дающий скорость передачи данных \
	до 320 Мбит/с.</p>"	

TOOLTIPS_DICT[u'Частота системной шины'] = u"<p>Частота системной шины - является важным показателем производительности, т.к. по \
	системной шине идет передача данных между микропроцессором и чипсетом. Ее величина определяется величиной \
	опорной частоты, которая в свою очередь является кратным от частоты процессора. Т.е. частоты процессора и системной \
	шины являются взаимосвязанными.</p>"	

TOOLTIPS_DICT[u'Вэб-камера'] = u"<p>При наличии вэб-камеры, которая встраивается над дисплеем, становится возможным \
	проведение видео-звонков или конференций посредством сети Интернет. Характеристика вэб-камеры отвечающая \
	за качество и размер видеоизображения измеряется в МПикс (в среднем от 0.3 МПикс до 3.0 МПикс). Чем больше \
	пикселей камера способна зафиксировать, тем лучше просматривается картинка.</p>"	

TOOLTIPS_DICT[u'LAN'] = u"<p>Разъем <b>LAN</b> (<i>Local Area Network</i>) предназначен для подключения сетевого \
	кабеля к ноутбуку или компьютеру, таким образом делая его частью локальной компьютерной сети.</p>"	

TOOLTIPS_DICT[u'Мультимедиа'] = u"<p><b>Кардридер</b> - устройство для считывания и записи информации на разнообразные \
	карты памяти (SD, MS, MMC и др.), которые сейчас часто используются в фотоаппаратах, электронных книгах, \
	мобильных телефонах и т.п.</p></br>\
	<p><b>Kensington замок</b> – специальный замок, который крепится в предназначенное для этого отверстие на \
	боковой панели ноутбука. Имеет стальной трос, которым можно охватить неподвижный или крупный предмет таким \
	образом, что ноутбук оказывается \"прикованным\" к этому предмету (подобие велосипедных замков).</p></br>\
	<p><b>GPS-модуль</b> предназначен для обмена данными со спутниковой системой навигации, таким образом, определяя \
	текущее местоположение с точностью до 1-3 м. Имея в арсенале GPS-модуль и подходящее ПО становится возможным \
	определение расстояния до разных объектов, расчет пути до объекта по оптимальному маршруту и много других полезных функций.</p></br>\
	<p>Вмонтированный в ноутбук <b>сканер отпечатка пальца</b> предназначен для облегчения ввода паролей (вместо набора \
	пароля достаточно провести пальцем по сканеру).</p></br>\
	<p><b>Пульт ДУ</b> - позволяет управлять компьютером в основном мультимедийной его частью: управление \
	громкостью, запуск следующей/предыдущей дорожки и т.д.</p></br>\
	<p>Встроенный в компьютер <b>ТВ-тюнер</b> позволяет принимать телевизионные сигналы и использовать ПК в качестве телевизора.</p>"	

TOOLTIPS_DICT[u'Объем кэш памяти 2-го уровня'] = u"<p><b>Кэш память</b> – память, в которую временно помещается часто используемая \
	информация, с высокой вероятностью запроса. Доступ и считывание данных из кэша происходит быстрее, \
	чем доступ к оперативной памяти.</p>\
	<p><b>L1 кэш память 1-го уровня</b> обладает самой большей скоростью, работает напрямую со своим \
	ядром процессора, расположена на самом кристалле процессора. Имеет очень малый объем.</p>\
	<p><b>L2 кэш память 2-го уровня</b> работает медленнее, чем 1-го уровня, однако имеет объем \
	до 12 МБ. Взаимодействует между кэшом 1-го уровня своего ядра и кэшом 3-го уровня.</p>\
	<p><b>L3 кэш память 3-го уровня</b> работает еще медленнее, но все-таки доступ к ней осуществляется \
	быстрее, чем к оперативной памяти. Объем может достигать 24 МБ. Взаимодействует с кэшом 2-го уровня всех ядер процессора.</p>"	

TOOLTIPS_DICT[u'Тип видеопамяти'] = u"<p>Разные типы видеопамяти различаются между собой в первую очередь  \
	эффективной частотой передачи данных: 1ГГц на <b>GDDR2</b> (устаревает), 2.5ГГц на <b>GDDR3</b> \
	(наиболее популярна сегодня), 3.6ГГц на <b>GDDR5</b> (самая современная  и быстрая видеопамять).</p>"	

TOOLTIPS_DICT[u'Поддержка BluRay'] = u"<p>Способность оптического привода поддерживать BD-диски \
	(<i>Blu-ray Disk</i>), которые обычно служат в качестве носителя фильма высокого разрешения. \
	Такие диски имеют объем по 25ГБ или 50ГБ.</p>"	

TOOLTIPS_DICT[u'Комплектность'] = u"<p>Предметы, входящие в комплект поставки, цена которых уже \
	включена в стоимость ноутбука.</p>"	

TOOLTIPS_DICT[u'Ударопрочный корпус'] = u"<p>При падении ноутбука со стола (или аналогичной высоты) \
	ударопрочный корпус предотвращает выход из строя данного устройства. </p>"	

TOOLTIPS_DICT[u'Влагозащищенный корпус'] = u"<p>Ноутбуки обладающие влагозащищенным корпусом могут \
	кратковременно находится в контакте с водой (дождь, попадание жидкости в корпус или даже падение \
	в воду), не выходя при этом из строя.</p>"	

TOOLTIPS_DICT[u'Подключение док-станции'] = u"<p>Возможность подключить к ноутбуку док-станцию – внешняя \
	подставка, которая крепится к ноутбуку и значительно расширяет его функциональность: в док-станции \
	может быть в наличии привод оптических дисков, дискретная видеокарта, разнообразные порты подключения, \
	вентилятор в качестве дополнительной системы охлаждения.</p>"	

TOOLTIPS_DICT[u'Емкость батареи'] = u"<p>Характеристика указывает на величину заряда, который аккумулятор \
	способен содержать и, соответственно, отдавать этот заряд на потребление ноутбука, т.е. питать его, \
	во время отсутствия питания от электросети. Измеряется в Ач, мАч или Втч (эти величины при сравнении \
	следует привести в единый вид).</p><p>Чем большей емкостью обладает батарея, тем дольше ноутбук сможет \
	работать без подзарядки. Но это не единственный фактор, который влияет на время работы вне электросети. \
	Необходимо также учитывать диагональ экрана (чем она больше, тем больше потребляется энергии), нагрузку \
	на процессор, подключение к локальной или сети Интернет. Все это определяет потребляемую мощность \
	ноутбука. Чем она выше, тем быстрее израсходуется заряд аккумулятора.</p>"	

TOOLTIPS_DICT[u'Кол-во ячеек батареи'] = u"<p>Количество элементов батареи ноутбука, обычно одинаковой \
	емкости, которые складываются в общую емкость аккумулятора. Бывают батареи, состоящие из 4 или 6 ячеек, \
	если ячеек 9 или 12, то они заметно влияют на форму и вес ноутбука.</p>"	

TOOLTIPS_DICT[u'Макс. время работы'] = u"<p>Максимальное время работы ноутбука без подзарядки при минимальном потреблении \
	энергии: уменьшенная яркость экрана, невысокие нагрузки на процессор и, особенно, видеокарту.</p>"	

TOOLTIPS_DICT[u'Датчик освещения'] = u"<p>Датчик освещения определяет насколько хорошо освещено окружение, \
	в котором работает ноутбук, и автоматически определяет: уменьшить (в темных помещениях) или увеличить \
	(в хорошо освещенных помещениях) яркость дисплея для улучшения работы.</p>"	
	
TOOLTIPS_DICT[u'Тип матрицы'] = u"<p>Тип матрицы определяется внутренними особенностями построения \
	изображения – размещение кристаллов, а также направление их поворотов.</p></br>\
	<p><b>TN+film</b> (<i>Twisted Nematic</i> + film) матрица наиболее распространенная. Характерна \
	быстрым откликом (до 5 мс) и является недорогой. Но обладает недостаточно качественной цветопередачей \
	и контрастностью.  Подходит для домашнего использования, в т.ч. и для игр. Но из-за малых углов обзора, \
	делает невозможным совместный просмотр фильмов – в зависимости от угла наблюдения происходит искажение \
	цвета. Не подходит для фотографов, т.к. при печати фотографий (или просмотре их на других мониторах) \
	цветовая гамма изображения может оказаться другой.</p></br>\
	<p><b>IPS</b> (<i>In Plane Switch</i>, также обозначается как <b>SFT</b>, <b>PLS</b>) идеально подходит \
	для профессионального дизайна и графики, но и цена обычно дороже в несколько раз, по сравнению с TN матрицей. \
	Характерна большими углами наблюдения, отлично передает контрастность. Из недостатков – большое время \
	отклика (25 мс).</p></br>\
	<p><b>MVA</b> (<i>Multi-domain Vertical Alignment</i>) или <b>PVA</b> (<i>Patterned Vertical Alignment</i>) \
	является. своего рода, компромиссом между TN и IPS. Передача цвета достаточно хороша и даже сравнима с \
	цветопередачей IPS матриц, но при даже небольшом отклонении может быть замечено искажение в полутонах. \
	Время отклика уступает TN, но лучше, чем у профессиональных IPS. По стоимости является дороже, чем TN матрица.</p>"		
	
TOOLTIPS_DICT[u'Стекло Gorilla Glass'] = u"<p>Стекло Gorilla Glass обладает большей прочностью, в сравнении \
	с обычным стеклом, и устойчивостью к царапинам. При этом, такое стекло легче и тоньше, но стоит дороже. \
	Но это не означает, что стекло непробиваемое и/или ударопрочное; данное стекло лишь в состоянии защитить \
	ваш ноутбук (или телефон) в мини-экстренных ситуациях.</p>"		
	
TOOLTIPS_DICT[u'Покрытие экрана'] = u"<p><b>Глянцевое</b> покрытие достаточно распространено среди \
	производителей, хотя имеет ряд недостатков: на глянце становится невозможно работать на улице \
	при солнечных лучах, а также и в помещении с ярким освещением – на экране появляются блики. Также \
	глянец больше подвержен загрязнению, особенно, часто видны отпечатки пальцев. Что касается, \
	изображения, то такое покрытие качественно влияет на цветопередачу, яркость и контрастность.</p></br><p>А \
	вот спрос на <b>матовое</b> покрытие гораздо больший. И, хотя оно немного уступает по качеству изображения, \
	его выбирают за отсутствие недостатков присущих глянцу. На матовом покрытии экрана практически отсутствуют \
	блики, дисплей меньше пачкается, не так сильно устают глаза при длительной работе.</p></br><p><b>Глянцевое \
	антибликовое</b> покрытие сохраняет качество отображения на экране, как у обычных глянцевых дисплеях, и при \
	этом обладает антибликовым эффектом: при ярком освещении не так сильно отзеркаливает.</p>"		
	
TOOLTIPS_DICT[u'Контрастность'] = u"<p>Контрастность определяется соотношением между уровнем яркости белого цвета \
	и уровнем яркости черного цвета. Чем больше это соотношение, тем более качественные оттенки дисплей может \
	воспроизвести. Оптимальной можно считать контрастность в пределах от 700:1 до 1000:1. Дальнейшее увеличение \
	контрастности в производстве мониторов и дисплеев не имеет практической ценности. Цифры в 8000:1 или 15000:1 \
	достигаются искусственным путем в идеальных условиях.</p>"	

TOOLTIPS_DICT[u'Яркость'] = u"<p>Параметр определяет максимальное количество света, излучаемое дисплеем, и \
	измеряется в кд/м² (канделах на квадратный метр). Идеальной для работы (для зрения) считается яркость \
	120-160 кд/м² (в помещении, на улице в солнечную погоду показатель можно увеличить и до 220 кд/м²). Если \
	монитор в силах обеспечить более высокую яркость, то для оптимальной работы ее необходимо уменьшить на \
	необходимую величину, подходящую для глаз. Ориентироваться на высокое значение этого параметра не стоит, \
	если вы не собираетесь устанавливать экран на улице для прокрутки рекламы.</p>"

TOOLTIPS_DICT[u'Поворотный экран'] = u"<p>Возможность экрана в открытом состоянии поворачиваться вдоль \
	вертикальной оси и укладываться обратно на клавиатуру дисплеем вверх. Обычно, ноутбуки оснащенные \
	таким экраном имеют еще и сенсорный дисплей, что превращает ноутбук в планшет. </p>"

TOOLTIPS_DICT[u'Стандарт памяти'] = u"<p>Стандарт памяти определяется ее типом (для DDR – стандарт \
	памяти <b>PC</b>, для типа DDR2 – стандарт <b>PC2</b>, для DDR3 – <b>PC3</b>) и частотой оперативной \
	памяти (начиная от 266 МГц в стандарт добавляется через дефис приставка 2100, и с увеличением частот до \
	2133 МГц – добавляется 17000; сама по себе, численная приставка означает пропускную способность \
	оперативной памяти в Мб/сек, чем она больше, тем более производительным будет устройство). </p>"


