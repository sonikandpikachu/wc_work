# coding: utf-8
'''
this module converts database data to data witch is going to be showm to user
'''
from collections import OrderedDict


def small_devices(computers_id, computers_dss, dbwrapper):
    '''
    prepare computer for QandA page
    '''
    if not computers_id:
        return []
    dsses = dbwrapper.dss_by_id(computers_id)
    computers = dbwrapper.parameters_by_id(computers_id)
    pretty_devices = []
    for index, dss, computer in zip(range(len(dsses)), dsses, computers):
        max_price, min_price = dbwrapper.max_and_min_price(computer)
        pretty_computer = {
            'type': computer.__class__.__name__[3:].lower(),  # type without 'wc_' prefix
            'id': str(computer.id),
            'name': computer.name,
            'model': computer.model,
            'comp_dss': computers_dss[index],
            'cpu_name': computer.cpu_name,
            'cpu_model': computer.cpu_model,
            'cpu_frequency': computer.cpu_frequency,
            'cpu_dss': dss.cpu,
            'ram_amount': computer.ram_amount,
            'ram_dss': dss.ram,
            'hdd_capacity': computer.hdd_capacity,
            'hdd_dss': dss.hdd,
            'os': computer.os,
            'os_dss': dss.os,
            'price': computer.price,
            'vga': computer.vga_model,
            'vga_amount': computer.vga_amount,
            'vga_dss': dss.vga,
            'price_dss': dss.price,
            'min_price': min_price,
            'max_price': max_price,
            'dss': dss
        }
        pretty_devices.append(pretty_computer)
    return pretty_devices


def big_computer(id, dbwrapper):
    comp = dbwrapper.parameters_by_id([id], device=u'computer')[0]
    pretty_computer = OrderedDict()
    pretty_computer[u"Компьютер"] = OrderedDict([
        (u"Имя", comp.name),
        (u"Тип", comp.type),
        (u"Предустановленная ОС", comp.os),
    ])
    pretty_computer[u"Процессор"] = OrderedDict([
        (u"Процессор", comp.cpu_name),
        (u"Модель", comp.cpu_model),
        (u"Частота процессора", comp.cpu_frequency),
        (u"Кол-во ядер", comp.cpu_kernel_count),
    ])

    pretty_computer[u"Видеокарта"] = OrderedDict([
        (u"Модель видеокарты", comp.vga_model),
        (u"Объем видеопамяти", comp.vga_amount),
        (u"Тип видеокарты", comp.vga_type),
    ])

    pretty_computer[u"Оперативная память"] = OrderedDict([
        (u"Тип памяти", comp.ram_type),
        (u"Тактовая частота", comp.ram_frequency),
        (u"Кол-во слотов", comp.ram_jacks),
        (u"Объем ОЗУ", comp.ram_amount),
    ])

    pretty_computer[u"Дисплей"] = OrderedDict([
        (u"Разрешение", comp.display_resolution),
        (u"LED подсветка", comp.display_led_backlight),
        (u"Диагональ экрана", comp.display_diagonal),
        (u"Сенсорный экран", comp.display_sensor),
        (u"Яркость", comp.display_brightness),
    ])

    pretty_computer[u"Накопитель"] = OrderedDict([
        (u"Внутренних отсеков 3", comp.hdd_cell),
        (u"Емкость накопителя", comp.hdd_capacity),
        (u"Тип накопителя", comp.hdd_type),
        (u"Обороты шпинделя", comp.hdd_speed),
    ])

    pretty_computer[u"Мультимедиа"] = OrderedDict([
        (u"Встроенные динамики", comp.media_builtin_dinamics),
        (u"Встроенная Вэб-камера", comp.media_web_camera),
        (u"Пульт ДУ", comp.media_remote),
        (u"ТВ-тюнер", comp.media_tv_tunner),
        (u"Звук", comp.media_sound),
        (u"Разъемов 3", comp.media_jacks3),
        (u"Встроенный микрофон", comp.media_microphone),
    ])

    pretty_computer[u"Аппаратная часть"] = OrderedDict([
        (u"Чипсет", comp.chipset)
    ])

    pretty_computer[u"Устройство"] = OrderedDict([
        (u"Сеть", comp.network),
        (u"PS/2", comp.ps2),
        (u"Thunderbolt", comp.thunderbolt),
        (u"Разъемы", comp.jacks),
        (u"USB 3", comp.panel_usb3),
        (u"USB 2", comp.panel_usb2),
    ])

    pretty_computer[u"Передняя панель"] = OrderedDict([
        (u"Отсеков 5", comp.panel_cell5),
        (u"Кардридер", comp.panel_cardreader),
        (u"Отсеков 3", comp.panel_cell3),
        (u"Цифровой дисплей", comp.panel_digital_display),
        (u"Аудио (микрофон/наушники)", comp.panel_audio),
        (u"Разъемов USB 3", comp.panel_usb3),
        (u"Разъемов USB 2", comp.panel_usb2),
        (u"Привод", comp.panel_drive),
    ])

    pretty_computer[u"Общее"] = OrderedDict([
        (u"Вес", comp.weight),
        (u"Мощность БП", comp.pb_power),
        (u"Материал корпуса", comp.material),
        (u"Габариты  (ВхШхГ)", u'%dx%dx%d (мм)' % (comp.height, comp.width, comp.length)),
        (u"Цвет", comp.color),
    ])

    for part in pretty_computer.iterkeys():
        for key in pretty_computer[part].iterkeys():
            if isinstance(pretty_computer[part][key], bool):
                pretty_computer[part][key] = '+' if pretty_computer[part][key] else '-'
            if not pretty_computer[part][key]:
                del pretty_computer[part][key]

    for part in pretty_computer.iterkeys():
        if not pretty_computer[part]:
            del pretty_computer[part]

    return pretty_computer


def big_notebook(id, dbwrapper):
    notebook = dbwrapper.parameters_by_id([id], device=u'notebook')[0]
    pretty_notebook = OrderedDict()
    pretty_notebook[u"Устройства ввода"] = OrderedDict({
        u"Конструкция клавиш": notebook.input_keys_constraction,
        u"Разная расцветка букв клавиатуры": notebook.input_keyboard_keycolors,
        u"Num блок": notebook.input_numblock,
        u"Манипулятор": notebook.input_manipulator,
        u"Поддержка мультитач": notebook.input_multitouch,
        u"Подсветка клавиатуры": notebook.input_keyboard_backlight,
        u"Кол-во дополнительных клавиш": notebook.input_aditional_keys,
    })
    pretty_notebook[u"Коммуникации"] = OrderedDict({
        u"Wi-Di (беспроводной)": notebook.com_widi,
        u"WiMAX-модуль": notebook.com_wimax,
        u"Слот расширения": notebook.com_slot,
        u"DialUp модем": notebook.com_dialup,
        u"3G модем": notebook.com_g3,
        u"Bluetooth": notebook.com_bluetooth,
        u"Тип слота расширения": notebook.com_slot_type,
        u"NFC-чип": notebook.com_nfs,
        u"Wi-Fi": notebook.com_wifi,
    })
    pretty_notebook[u"Аппаратная часть"] = OrderedDict({
        u"Частота системной шины": notebook.system_bus,
        u"Чипсет": notebook.chipset,
    })
    pretty_notebook[u"Устройство"] = OrderedDict({
        u"Дополнительный выход на наушники": notebook.additional_headphones_port,
        u"LAN (RJ-45)": notebook.lan,
        u"Thunderbolt": notebook.thunderbolt,
        u"имя": notebook.name,
        u"Вэб-камера": notebook.web_camera,
        u"Порты подключения": notebook.connection_ports,
        u"USB 2": notebook.panel_usb2,
        u"страница_картинок": notebook.media_url,
        u"USB 3": notebook.panel_usb3,
        u"Тип": notebook.type,
        u"url": notebook.url,
        u"модель": notebook.model,
        u"Мультимедиа": notebook.multimedia,
        u"Формат акустики": notebook.accoustic_format,
    })
    pretty_notebook[u"Накопитель"] = OrderedDict({
        u"Емкость накопителя": notebook.hdd_capacity,
        u"Обороты шпинделя": notebook.hdd_speed,
        u"RAID массив": notebook.hdd_raid,
        u"Емкость 2-го накопителя": notebook.hdd_capacity2,
        u"Тип накопителя": notebook.hdd_type,
        u"Датчик свободного падения": notebook.hdd_free_fall,
    })
    pretty_notebook[u"Процессор"] = OrderedDict({
        u"Процессор (SuperPI 1M)": notebook.testcpu_super,
        u"Процессор (Passmark CPU Mark)": notebook.testcpu_passmark,
        u"Модель": notebook.cpu_model,
        u"Частота процессора": notebook.cpu_frequency,
        u"Кол-во ядер процессора": notebook.cpu_kernel_count,
        u"Объем кэш памяти 3-го уровня": notebook.cpu_cash3,
        u"Серия процессора": notebook.cpu_name,
        u"Объем кэш памяти 2-го уровня": notebook.cpu_cash2,
        u"Процессор (3DMark06)": notebook.testcpu_3dmark06,
    })
    pretty_notebook[u"Видеокарта"] = OrderedDict({
        u"Серия": notebook.vga_model,
        u"Видеокарта (3DMark Vantage)": notebook.testvga_3dmark,
        u"Тип видеокарты": notebook.vga_type,
        u"Тип памяти": notebook.vga_memory_type,
        u"Объем видеопамяти": notebook.vga_amount,
        u"Видеокарта (3DMark06)": notebook.testvga_3dmark06,
        u"Модель": notebook.vga_number,
    })
    pretty_notebook[u"Привод оптических дисков"] = OrderedDict({
        u"Поддержка BluRay": notebook.panel_bluraydrive,
        u"Тип": notebook.panel_drive,
    })
    pretty_notebook[u"Общее"] = OrderedDict({
        u"Комплектность": notebook.completeness,
        u"Ударопрочный корпус": notebook.shockproof,
        u"Предустановленная ОС": notebook.os,
        u"Габариты (ШхГхТ)": '%dx%dx%d' % (notebook.height,notebook.width,notebook.length),
        u"Вес": notebook.weight,
        u"Влагозащищенный корпус": notebook.waterproof,
        u"Цвет": notebook.color,
        u"Подключение док-станции": notebook.doc_station_connection,
        u"Материал корпуса": notebook.material,
    })
    pretty_notebook[u"Результаты тестов"] = OrderedDict({
        u"Процессор (SuperPI 1M)": notebook.testcpu_super,
        u"Процессор (Passmark CPU Mark)": notebook.testcpu_passmark,
        u"Видеокарта (3DMark Vantage)": notebook.testvga_3dmark,
        u"Видеокарта (3DMark06)": notebook.testvga_3dmark06,
        u"Процессор (3DMark06)": notebook.testcpu_3dmark06,
    })
    pretty_notebook[u"Аккумулятор"] = OrderedDict({
        u"Напряжение батареи": notebook.battery_voltage,
        u"Макс": notebook.battery_work_time,
        u"Время зарядки": notebook.battery_charging_time,
        u"Кол-во ячеек батареи": notebook.battery_cells,
        u"Время работы (при макс_ нагрузке)": notebook.battery_work_time,
        u"Емкость батареи": notebook.battery_capacity,
    })
    pretty_notebook[u"Дисплей"] = OrderedDict({
        u"Датчик освещения": notebook.display_light_sensor,
        u"Тип матрицы": notebook.display_matrix,
        u"Поддержка мультитач": notebook.display_multitouch,
        u"Стекло Gorilla Glass": notebook.display_gorilla_glass,
        u"Покрытие экрана": notebook.display_cover,
        u"Контрастность": notebook.display_contrast,
        u"Разрешение дисплея": notebook.disply_resolution,
        u"Сенсорный": notebook.display_sensor,
        u"Яркость": notebook.display_brightness,
        u"Поворотный экран": notebook.display_rotation,
        u"Диагональ экрана": notebook.display_diagonal,
        u"LED подсветка": notebook.display_led_backlight,
    })
    pretty_notebook[u"Оперативная память"] = OrderedDict({
        u"Стандарт памяти": notebook.ram_standart,
        u"Максимально устанавливаемый объем": notebook.ram_max,
        u"Объем оперативной памяти": notebook.ram_amount,
        u"Кол-во слотов": notebook.ram_jacks,
        u"Тип": notebook.ram_type,
    })

    for part in pretty_notebook.iterkeys():
        for key in pretty_notebook[part].iterkeys():
            if isinstance(pretty_notebook[part][key], bool):
                pretty_notebook[part][key] = '+' if pretty_notebook[part][key] else '-'
            if not pretty_notebook[part][key]:
                del pretty_notebook[part][key]

    for part in pretty_notebook.iterkeys():
        if not pretty_notebook[part]:
            del pretty_notebook[part]

    return pretty_notebook

#I think this function code is bad, but no ideas how to make it better :(
def pagination_pages(current_page, last_page):
    if last_page == 0:
        return ['1']
    pages = set((1, 2, current_page - 1, current_page, current_page + 1, last_page - 1, last_page))
    if 0 in pages:
        pages.remove(0)
    if last_page + 1 in pages:
        pages.remove(last_page + 1)
    pages = list(pages)
    pages.sort()
    pagination_pages = []
    for i in range(len(pages) - 1):
        pagination_pages.append(pages[i])
        if pages[i] + 1 != pages[i + 1]:
            pagination_pages.append('...')
    pagination_pages.append(pages[-1])
    return pagination_pages
