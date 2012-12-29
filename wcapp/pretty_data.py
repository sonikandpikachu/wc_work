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
    comp = dbwrapper.parameters_by_id([id])[0]
    pretty_computer = OrderedDict()
    pretty_computer[u"Мультимедиа"] = OrderedDict({
       u"Встроенные динамики": comp.media_builtin_dinamics,
       u"Встроенная Вэб-камера": comp.media_web_camera,
       u"Пульт ДУ": comp.media_remote,
       u"ТВ-тюнер": comp.media_tv_tunner,
       u"Звук": comp.media_sound,
       u"Разъемов 3": comp.media_jacks3,
       u"Встроенный микрофон": comp.media_microphone,
    })
    pretty_computer[u"Аппаратная часть"] = OrderedDict({
       u"Чипсет": comp.chipset,
    })
    pretty_computer[u"Устройство"] = OrderedDict({
       u"Сеть": comp.network,
       u"PS/2": comp.ps2,
       u"имя": comp.name,
       u"url": comp.url,
       u"Тип": comp.type,
       u"Thunderbolt": comp.thunderbolt,
       u"Разъемы": comp.jacks,
       u"USB 3": comp.panel_usb3,
       u"USB 2": comp.panel_usb2,
    })
    pretty_computer[u"Накопитель"] = OrderedDict({
       u"Внутренних отсеков 3": comp.hdd_cell,
       u"Емкость накопителя": comp.hdd_capacity,
       u"Тип накопителя": comp.hdd_type,
       u"Обороты шпинделя": comp.hdd_speed,
    })
    pretty_computer[u"Процессор"] = OrderedDict({
       u"Кол-во ядер": comp.cpu_kernel_count,
       u"Модель": comp.cpu_model,
       u"Частота процессора": comp.cpu_frequency,
       u"Процессор": comp.cpu_name,
    })
    pretty_computer[u"Видеокарта"] = OrderedDict({
       u"Модель видеокарты": comp.vga_model,
       u"Объем видеопамяти": comp.vga_amount,
       u"Тип видеокарты": comp.vga_type,
    })
    pretty_computer[u"Общее"] = OrderedDict({
       u"Вес": comp.weight,
       u"Мощность БП": comp.pb_power,
       u"Материал корпуса": comp.material,
       u"Габариты  (ВхШхГ)": str(comp.height) + str(comp.width) + str(comp.length),
       u"Предустановленная ОС": comp.os,
       u"Цвет": comp.color,
    })
    pretty_computer[u"Дисплей"] = OrderedDict({
       u"Разрешение": comp.display_resolution,
       u"LED подсветка": comp.display_led_backlight,
       u"Диагональ экрана": comp.display_diagonal,
       u"Сенсорный экран": comp.display_sensor,
       u"Яркость": comp.display_brightness,
    })
    pretty_computer[u"Передняя панель"] = OrderedDict({
       u"Отсеков 5": comp.panel_cell5,
       u"Кардридер": comp.panel_cardreader,
       u"Отсеков 3": comp.panel_cell3,
       u"Цифровой дисплей": comp.panel_digital_display,
       u"Аудио (микрофон/наушники)": comp.panel_audio,
       u"Разъемов USB 3": comp.panel_usb3,
       u"Разъемов USB 2": comp.panel_usb2,
       u"Привод": comp.panel_drive,
    })
    pretty_computer[u"Оперативная память"] = OrderedDict({
       u"Тип памяти": comp.ram_type,
       u"Тактовая частота": comp.ram_frequency,
       u"Кол-во слотов": comp.ram_jacks,
       u"Объем ОЗУ": comp.ram_amount,
    })

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
