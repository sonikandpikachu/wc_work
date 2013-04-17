# coding: utf-8
'''
this module converts database data to data witch is going to be showm to user
'''
from collections import OrderedDict
import math
import os


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

        dir = os.path.join(os.path.dirname(__file__), 'static/img/' + computer.__class__.__name__[3:].lower() + 's/' + str(computer.id) + "_img")
        names = os.listdir(dir)
        if len (names) != 1: names.remove('main.jpg')
        for name in names:
            if name.split(".")[1] == "db": names.remove(name)

        if computer.__class__.__name__[3:].lower() == 'computer':
            pretty_computer = {
                'type': 'computer',
                'id': str(computer.id),
                'name': computer.name,
                'model': computer.model,
                'comp_dss': int(round(computers_dss[index])),
                'cpu_name': computer.cpu_name,
                'cpu_model': computer.cpu_model,
                'cpu_frequency': computer.cpu_frequency,
                'cpu_dss': dss.cpu,
                'ram_amount': computer.ram_amount,
                'ram_dss': dss.ram,
                'hdd_capacity': computer.hdd_clear_capacity,
                'hdd_type': computer.hdd_type,
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
                'display': computer.display_diagonal,
                'resolution': computer.display_resolution,
                'display_dss': dss.display,
                'other_dss': (dss.network + dss.panel + dss.media + 0.5*dss.thunderbolt + 30)/3.5, # 30 - chtob ludi ne dumali chto vubiraut govno nu i thunderbolt toge ne ochen vagen
                'gallery': names
                # 'dss': dss.__dict__,
            }
        else:
            pretty_computer = {
                'type': 'notebook',
                'id': str(computer.id),
                'name': computer.name,
                'model': computer.model,
                'comp_dss': int(round(computers_dss[index])),
                'cpu_name': computer.cpu_name,
                'cpu_model': computer.cpu_model,
                'cpu_frequency': computer.cpu_frequency,
                'cpu_dss': dss.cpu,
                'ram_amount': computer.ram_amount,
                'ram_dss': dss.ram,
                'hdd_capacity': computer.hdd_clear_capacity,
                'hdd_type': computer.hdd_type,
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
                'display': computer.display_diagonal,
                'resolution': computer.disply_resolution,
                'display_dss': dss.display,
                'other_dss': (dss.web_camera + dss.com + dss.panel + 0.5*dss.input + 0.5*dss.accoustic + 30)/4,
                'gallery': names
                # 'dss': dss.__dict__,
            }
        pretty_devices.append(pretty_computer)
    return pretty_devices


def big_computer(id, dbwrapper):
    comp = dbwrapper.parameters_by_id([id], device=u'computer')[0]
    pretty_computer = OrderedDict()
    pretty_computer[u"Компьютер"] = OrderedDict([
        (u"Имя", comp.name),
        (u"Модель", comp.model),
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
        (u"Объем ОЗУ", comp.ram_amount),
        (u"Тип памяти", comp.ram_type),
        (u"Тактовая частота", comp.ram_frequency),
        (u"Кол-во слотов", comp.ram_jacks)        
    ])

    pretty_computer[u"Дисплей"] = OrderedDict([
        (u"Диагональ экрана", comp.display_diagonal),
        (u"Разрешение", comp.display_resolution),
        (u"Яркость", comp.display_brightness),
        (u"LED подсветка", comp.display_led_backlight),        
        (u"Сенсорный экран", comp.display_sensor),        
    ])

    pretty_computer[u"Накопитель"] = OrderedDict([        
        (u"Емкость накопителя", comp.hdd_capacity),
        (u"Тип накопителя", comp.hdd_type),
        (u"Обороты шпинделя", comp.hdd_speed),
        (u"Внутренних отсеков 3.5", comp.hdd_cell),
    ])

    pretty_computer[u"Мультимедиа"] = OrderedDict([
        (u"Встроенные динамики", comp.media_builtin_dinamics),
        (u"Встроенная Вэб-камера", comp.media_web_camera),
        (u"Пульт ДУ", comp.media_remote),
        (u"ТВ-тюнер", comp.media_tv_tunner),
        (u"Звук", comp.media_sound),
        (u"Разъемов 3.5 мм", comp.media_jacks3),
        (u"Встроенный микрофон", comp.media_microphone),
    ])

    pretty_computer[u"Аппаратная часть"] = OrderedDict([
        (u"Чипсет", comp.chipset)
    ])

    pretty_computer[u"Устройство"] = OrderedDict([
        (u"Сеть", comp.network),
        (u"PS2", comp.ps2),
        (u"Thunderbolt", comp.thunderbolt),
        (u"Разъемы", comp.jacks)
    ])

    pretty_computer[u"Панель"] = OrderedDict([
        (u"Привод", comp.panel_drive),
        (u"Разъемов USB 3.0", comp.panel_usb3),
        (u"Разъемов USB 2.0", comp.panel_usb2),
        (u"Кардридер", comp.panel_cardreader),        
        (u"Цифровой дисплей", comp.panel_digital_display),
        (u"Аудио (микрофон/наушники)", comp.panel_audio),
        (u"Отсеков 5.25", comp.panel_cell5),
        (u"Отсеков 3.5", comp.panel_cell3),
    ])

    pretty_computer[u"Общее"] = OrderedDict([
        (u"Вес", comp.weight),
        (u"Мощность БП", comp.pb_power),
        (u"Материал корпуса", comp.material),
        (u"Габариты  (ВхШхГ)", str(comp.height) + "x" + str(comp.width)+ "x" + str(comp.length)),
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
    pretty_notebook[u"Ноутбук"] = OrderedDict([
        (u"Имя", notebook.name),
        (u"Модель", notebook.model),
        (u"Тип", notebook.type),
        (u"Предустановленная ОС", notebook.os),
    ])
    pretty_notebook[u"Процессор"] = OrderedDict([
        (u"Серия процессора", notebook.cpu_name),
        (u"Модель", notebook.cpu_model),
        (u"Частота процессора", notebook.cpu_frequency),
        (u"Кол-во ядер процессора", notebook.cpu_kernel_count),
        (u"Объем кэш памяти 3-го уровня", str(notebook.cpu_cash3) + u" КБ"),        
        (u"Объем кэш памяти 2-го уровня", str(notebook.cpu_cash2) + u" КБ"),
    ])
    pretty_notebook[u"Видеокарта"] = OrderedDict([
        (u"Серия", notebook.vga_model),
        (u"Модель", notebook.vga_number),
        (u"Объем видеопамяти", notebook.vga_amount),
        (u"Тип видеокарты", notebook.vga_type),
        (u"Тип памяти", notebook.vga_memory_type)
    ])

    pretty_notebook[u"Оперативная память"] = OrderedDict([
        (u"Объем оперативной памяти", notebook.ram_amount),
        (u"Тип", notebook.ram_type),
        (u"Стандарт памяти", notebook.ram_standart),
        (u"Максимально устанавливаемый объем", notebook.ram_max),
        (u"Кол-во слотов", notebook.ram_jacks)        
    ])

    pretty_notebook[u"Дисплей"] = OrderedDict([        
        (u"Диагональ экрана", str(notebook.display_diagonal) + " \""),        
        (u"Разрешение дисплея", notebook.disply_resolution),        
        (u"Сенсорный", notebook.display_sensor),
        (u"Поворотный экран", notebook.display_rotation),
        (u"Поддержка мультитач", notebook.display_multitouch), 
        (u"Тип матрицы", notebook.display_matrix),       
        (u"Контрастность", notebook.display_contrast),
        (u"Яркость", notebook.display_brightness),
        (u"Стекло Gorilla Glass", notebook.display_gorilla_glass),
        (u"Покрытие экрана", notebook.display_cover),
        (u"Датчик освещения", notebook.display_light_sensor),
        (u"LED подсветка", notebook.display_led_backlight),
    ])

    pretty_notebook[u"Накопитель"] = OrderedDict([
        (u"Емкость накопителя", notebook.hdd_capacity),
        (u"Тип накопителя", notebook.hdd_type),
        (u"Обороты шпинделя", notebook.hdd_speed),
        (u"RAID массив", notebook.hdd_raid),
        (u"Емкость 2-го накопителя", notebook.hdd_capacity2),
        (u"Датчик свободного падения", notebook.hdd_free_fall),
    ])   

    pretty_notebook[u"Привод оптических дисков"] = OrderedDict([
        (u"Тип", notebook.panel_drive),
        (u"Поддержка BluRay", notebook.panel_bluraydrive)
    ]) 

    pretty_notebook[u"Коммуникации"] = OrderedDict([        
        (u"Wi-Fi", notebook.com_wifi),        
        (u"Bluetooth", notebook.com_bluetooth),
        (u"Wi-Di (беспроводной)", notebook.com_widi),
        (u"WiMAX-модуль", notebook.com_wimax),
        (u"DialUp модем", notebook.com_dialup),
        (u"3G модем", notebook.com_g3),        
        (u"Слот расширения", notebook.com_slot),
        (u"Тип слота расширения", notebook.com_slot_type),
        (u"NFC-чип", notebook.com_nfs),
    ])
    pretty_notebook[u"Аппаратная часть"] = OrderedDict([
        (u"Частота системной шины", notebook.system_bus),
        (u"Чипсет", notebook.chipset),
    ])
    pretty_notebook[u"Устройство"] = OrderedDict([
        (u"USB 2.0", notebook.panel_usb2),
        (u"USB 3.0", notebook.panel_usb3),
        (u"LAN (RJ-45)", notebook.lan),
        (u"Thunderbolt", notebook.thunderbolt),
        (u"Вэб-камера", notebook.web_camera),
        (u"Порты подключения", notebook.connection_ports),
        (u"Мультимедиа", notebook.multimedia),
        (u"Формат акустики", notebook.accoustic_format),        
        (u"Дополнительный выход на наушники", notebook.additional_headphones_port),
    ])

    pretty_notebook[u"Устройства ввода"] = OrderedDict([
        (u"Конструкция клавиш", notebook.input_keys_constraction),
        (u"Манипулятор", notebook.input_manipulator),
        (u"Поддержка мультитач", notebook.input_multitouch),
        (u"Подсветка клавиатуры", notebook.input_keyboard_backlight),
        (u"Разная расцветка букв клавиатуры", notebook.input_keyboard_keycolors),
        (u"Num блок", notebook.input_numblock),
        (u"Кол-во дополнительных клавиш", notebook.input_aditional_keys),
    ])  

    pretty_notebook[u"Аккумулятор"] = OrderedDict([
        (u"Время работы (при макс_ нагрузке)", notebook.battery_work_time),
        (u"Емкость батареи", notebook.battery_capacity),
        (u"Напряжение батареи", notebook.battery_voltage),
        (u"Время зарядки", notebook.battery_charging_time),
        (u"Кол-во ячеек батареи", notebook.battery_cells),        
    ])    

    pretty_notebook[u"Общее"] = OrderedDict([
        (u"Комплектность", notebook.completeness),
        (u"Ударопрочный корпус", notebook.shockproof),
        (u"Влагозащищенный корпус", notebook.waterproof),
        (u"Подключение док-станции", notebook.doc_station_connection),                
        (u"Вес", notebook.weight),
        (u"Материал корпуса", notebook.material),
        (u"Габариты (ШхГхТ)", str(notebook.height) + "x" + str(notebook.width) + "x" + str(notebook.length)),        
        (u"Цвет", notebook.color),
    ])

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
def pagination_pages(last_page):
    current_page = 1
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
