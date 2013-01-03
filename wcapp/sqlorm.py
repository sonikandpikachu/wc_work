'''
Created on Sep 18, 2012

@author: Pavel

This modul realise our database as orm.
'''
from wcconfig import db


class wc_Computer(db.Model):
    __tablename__ = "wc_Computer"

    id = db.Column(db.Integer, primary_key=True)

    chipset = db.Column(db.String(30))
    color = db.Column(db.String(50))
    cpu_frequency = db.Column(db.Float)
    cpu_kernel_count = db.Column(db.Integer)
    cpu_model = db.Column(db.String(30))
    cpu_name = db.Column(db.String(50))
    display_brightness = db.Column(db.Integer)
    display_diagonal = db.Column(db.Integer)
    display_led_backlight = db.Column(db.Boolean)
    display_sensor = db.Column(db.Boolean)
    display_resolution = db.Column(db.String(20))
    hdd_capacity = db.Column(db.String(100))
    hdd_cell = db.Column(db.Integer)
    hdd_speed = db.Column(db.Integer)
    hdd_type = db.Column(db.String(30))
    height = db.Column(db.Float)
    jacks = db.Column(db.String(150))
    length = db.Column(db.Float)
    material = db.Column(db.String(150))
    media_builtin_dinamics = db.Column(db.Boolean)
    media_jacks3 = db.Column(db.Integer)
    media_microphone = db.Column(db.Boolean)
    media_remote = db.Column(db.Boolean)
    media_sound = db.Column(db.String(10))
    media_tv_tunner = db.Column(db.Boolean)
    media_web_camera = db.Column(db.Boolean)
    model = db.Column(db.String(200))
    name = db.Column(db.String(300))
    network = db.Column(db.String(150))
    os = db.Column(db.String(50))
    panel_audio = db.Column(db.Boolean)
    panel_cardreader = db.Column(db.Boolean)
    panel_cell3 = db.Column(db.Integer)
    panel_cell5 = db.Column(db.Integer)
    panel_digital_display = db.Column(db.Boolean)
    panel_drive = db.Column(db.String(50))
    panel_usb2 = db.Column(db.Integer)
    panel_usb3 = db.Column(db.Integer)
    pb_power = db.Column(db.Integer)
    ps2 = db.Column(db.String(10))
    ram_amount = db.Column(db.Integer)
    ram_frequency = db.Column(db.Integer)
    ram_jacks = db.Column(db.Integer)
    ram_type = db.Column(db.String(30))
    thunderbolt = db.Column(db.Integer)
    type = db.Column(db.String(100))
    url = db.Column(db.String(300))
    vga_amount = db.Column(db.Integer)
    vga_model = db.Column(db.String(100))
    vga_type = db.Column(db.String(150))
    weight = db.Column(db.Float)
    width = db.Column(db.Float)
    price = db.Column(db.Float)
    testcpu_passmark = db.Column(db.Float)
    testvga_3dmark06 = db.Column(db.Float)
    in_view = db.Column(db.Boolean)

    def __init__(self, id=None, chipset=None, color=None, cpu_frequency=None, cpu_kernel_count=None, cpu_model=None,
        cpu_name=None, display_brightness=None, display_diagonal=None, display_led_backlight=None, display_sensor=None,
        display_resolution=None, hdd_capacity=None, hdd_cell=None, hdd_speed=None, hdd_type=None, height=None,
        jacks=None, length=None, material=None, media_builtin_dinamics=None, media_jacks3=None, media_microphone=None,
        media_remote=None, media_sound=None, media_tv_tunner=None, media_web_camera=None, model=None, name=None, network=None,
        os=None, panel_audio=None, panel_cardreader=None, panel_cell3=None, panel_cell5=None, panel_digital_display=None,
        panel_drive=None, panel_usb2=None, panel_usb3=None, pb_power=None, ps2=None,
        ram_amount=None, ram_frequency=None, ram_jacks=None, ram_type=None, thunderbolt=None, type=None, url=None,
        vga_amount=None, vga_model=None, vga_type=None, weight=None, width=None, price=None,
        testcpu_passmark=None, testvga_3dmark06=None, in_view=None):
        self.chipset = chipset
        self.color = color
        self.cpu_frequency = cpu_frequency
        self.cpu_kernel_count = cpu_kernel_count
        self.cpu_model = cpu_model
        self.cpu_name = cpu_name
        self.display_brightness = display_brightness
        self.display_diagonal = display_diagonal
        self.display_led_backlight = display_led_backlight
        self.display_sensor = display_sensor
        self.display_resolution = display_resolution
        self.hdd_capacity = hdd_capacity
        self.hdd_cell = hdd_cell
        self.hdd_speed = hdd_speed
        self.hdd_type = hdd_type
        self.height = height
        self.jacks = jacks
        self.length = length
        self.material = material
        self.media_builtin_dinamics = media_builtin_dinamics
        self.media_jacks3 = media_jacks3
        self.media_microphone = media_microphone
        self.media_remote = media_remote
        self.media_sound = media_sound
        self.media_tv_tunner = media_tv_tunner
        self.media_web_camera = media_web_camera
        self.model = model
        self.name = name
        self.network = network
        self.os = os
        self.panel_audio = panel_audio
        self.panel_cardreader = panel_cardreader
        self.panel_cell3 = panel_cell3
        self.panel_cell5 = panel_cell5
        self.panel_digital_display = panel_digital_display
        self.panel_drive = panel_drive
        self.panel_usb2 = panel_usb2
        self.panel_usb3 = panel_usb3
        self.pb_power = pb_power
        self.ps2 = ps2
        self.ram_amount = ram_amount
        self.ram_frequency = ram_frequency
        self.ram_jacks = ram_jacks
        self.ram_type = ram_type
        self.thunderbolt = thunderbolt
        self.type = type
        self.url = url
        self.vga_amount = vga_amount
        self.vga_model = vga_model
        self.vga_type = vga_type
        self.weight = weight
        self.width = width
        self.price = price
        self.testcpu_passmark = testcpu_passmark
        self.testvga_3dmark06 = testvga_3dmark06
        self.in_view = in_view
        if id:
            self.id = id


class wc_ConcComputer(db.Model):
    __tablename__ = "wc_ConcComputer"

    id = db.Column(db.Integer, primary_key=True)
    price_grn = db.Column(db.Integer)
    price_usd = db.Column(db.Integer)

    wc_Computer_id = db.Column(db.Integer, db.ForeignKey('wc_Computer.id'))
    device = db.relationship('wc_Computer',
        backref=db.backref('concretes', lazy='dynamic'))

    wc_Shop_id = db.Column(db.Integer, db.ForeignKey('wc_Shop.id'))
    shop = db.relationship('wc_Shop',
        backref=db.backref('conccomputers', lazy='dynamic'))

    def __init__(self, id=None, price_usd=None, price_grn=None, device=None, shop=None):
        self.price_grn = price_grn
        self.price_usd = price_usd
        self.shop = shop
        self.device = device
        if id:
            self.id = id


class wc_Shop(db.Model):
    __tablename__ = "wc_Shop"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))

    def __init__(self, id=None, name=None):
        self.name = name
        if id:
            self.id = id


#wc_dss.id == wc_computer.id
class wc_ComputerDSS(db.Model):
    __tablename__ = 'wc_ComputerDSS'

    id = db.Column(db.Integer, primary_key=True)
    hdd = db.Column(db.Float)
    cpu = db.Column(db.Float)
    display = db.Column(db.Float)
    ram = db.Column(db.Float)
    vga = db.Column(db.Float)
    os = db.Column(db.Float)
    price = db.Column(db.Float)
    size = db.Column(db.Float)
    panel = db.Column(db.Float)
    media = db.Column(db.Float)
    thunderbolt = db.Column(db.Float)
    network = db.Column(db.Float)

    def __init__(self, id=None, hdd=None, cpu=None, display=None, ram=None, vga=None,
        os=None, size=None, panel=None, media=None, thunderbolt=None, network=None, price=None):
        self.hdd = hdd
        self.cpu = cpu
        self.vga = vga
        self.ram = ram
        self.display = display
        self.os = os
        self.price = price
        self.size = size
        self.panel = panel
        self.media = media
        self.thunderbolt = thunderbolt
        self.network = network


class wc_Notebook(db.Model):
    __tablename__ = "wc_Notebook"

    id = db.Column(db.Integer, primary_key=True)
    battery_capacity = db.Column(db.Float)
    battery_cells = db.Column(db.Float)
    battery_charging_time = db.Column(db.Float)
    battery_voltage = db.Column(db.Float)
    battery_work_time = db.Column(db.Float)
    cpu_frequency = db.Column(db.Float)
    cpu_kernel_count = db.Column(db.Integer)
    cpu_model = db.Column(db.String(10))
    cpu_name = db.Column(db.String(50))
    com_g3 = db.Column(db.Boolean)
    com_bluetooth = db.Column(db.Boolean)
    com_dialup = db.Column(db.Boolean)
    com_nfs = db.Column(db.Boolean)
    com_slot = db.Column(db.Boolean)
    com_slot_type = db.Column(db.String(100))
    com_widi = db.Column(db.Boolean)
    com_wifi = db.Column(db.String(150))
    com_wimax = db.Column(db.Boolean)
    display_led_backlight = db.Column(db.Boolean)
    display_brightness = db.Column(db.Integer)
    display_contrast = db.Column(db.String(50))
    display_cover = db.Column(db.String(150))
    display_diagonal = db.Column(db.Integer)
    display_gorilla_glass = db.Column(db.Boolean)
    display_light_sensor = db.Column(db.Boolean)
    display_matrix = db.Column(db.String(50))
    display_multitouch = db.Column(db.Boolean)
    display_rotation = db.Column(db.Boolean)
    display_sensor = db.Column(db.Boolean)
    disply_resolution = db.Column(db.String(20))
    hdd_capacity = db.Column(db.String(100))
    hdd_speed = db.Column(db.Integer)
    hdd_type = db.Column(db.String(100))
    panel_drive = db.Column(db.String(50))
    panel_usb2 = db.Column(db.Integer)
    panel_usb3 = db.Column(db.Integer)
    ram_amount = db.Column(db.Integer)
    ram_jacks = db.Column(db.Integer)
    system_bus = db.Column(db.Float)
    vga_amount = db.Column(db.Integer)
    vga_type = db.Column(db.String(150))
    accoustic_format = db.Column(db.String(150))
    additional_headphones_port = db.Column(db.String(50))
    chipset = db.Column(db.String(30))
    color = db.Column(db.String(50))
    completeness = db.Column(db.String(100))
    connection_ports = db.Column(db.String(150))
    cpu_cash2 = db.Column(db.Integer)
    cpu_cash3 = db.Column(db.Integer)
    doc_station_connection = db.Column(db.Boolean)
    hdd_capacity2 = db.Column(db.String(150))
    hdd_free_fall = db.Column(db.Boolean)
    hdd_raid = db.Column(db.Boolean)
    input_aditional_keys = db.Column(db.String(50))
    input_keyboard_backlight = db.Column(db.String(50))
    input_keyboard_keycolors = db.Column(db.String(50))
    input_keys_constraction = db.Column(db.String(50))
    input_manipulator = db.Column(db.String(150))
    input_multitouch = db.Column(db.String(150))
    input_numblock = db.Column(db.String(150))
    lan = db.Column(db.String(150))
    material = db.Column(db.String(150))
    multimedia = db.Column(db.String(150))
    name = db.Column(db.String(300))
    model = db.Column(db.String(300))
    os = db.Column(db.String(150))
    panel_bluraydrive = db.Column(db.Boolean)
    ram_max = db.Column(db.Integer)
    ram_standart = db.Column(db.String(150))
    ram_type = db.Column(db.String(10))
    shell = db.Column(db.String(150))
    shockproof = db.Column(db.String(150))
    testcpu_3dmark06 = db.Column(db.Integer)
    testcpu_passmark = db.Column(db.Integer)
    testcpu_super = db.Column(db.Float)
    testvga_3dmark = db.Column(db.Integer)
    testvga_3dmark06 = db.Column(db.Integer)
    thunderbolt = db.Column(db.Integer)
    type = db.Column(db.String(100))
    url = db.Column(db.String(300))
    vga_memory_type = db.Column(db.String(50))
    vga_model = db.Column(db.String(100))
    vga_number = db.Column(db.String(150))
    waterproof = db.Column(db.String(150))
    web_camera = db.Column(db.String(100))
    weight = db.Column(db.Float)
    width = db.Column(db.Float)
    length = db.Column(db.Float)
    height = db.Column(db.Float)
    price = db.Column(db.Float)
    in_view = db.Column(db.Boolean)

    def __init__(self, id=None, battery_capacity=None, battery_cells=None, battery_charging_time=None,
            battery_voltage=None, battery_work_time=None,
            cpu_frequency=None, cpu_kernel_count=None, cpu_model=None, cpu_name=None,
            com_g3=None, com_bluetooth=None, com_dialup=None, com_nfs=None, com_slot=None,
            com_slot_type=None, com_widi=None, com_wifi=None, com_wimax=None, display_led_backlight=None,
            display_brightness=None, display_contrast=None, display_cover=None,
            display_diagonal=None, display_gorilla_glass=None, display_light_sensor=None,
            display_matrix=None, display_multitouch=None, display_rotation=None,
            display_sensor=None, disply_resolution=None, hdd_capacity=None,
            hdd_speed=None, hdd_type=None, panel_drive=None, panel_usb2=None,
            panel_usb3=None, ram_amount=None, ram_jacks=None, system_bus=None,
            vga_amount=None, vga_type=None, accoustic_format=None,
            additional_headphones_port=None, chipset=None, color=None,
            completeness=None, connection_ports=None, cpu_cash2=None,
            cpu_cash3=None, doc_station_connection=None, hdd_capacity2=None,
            hdd_free_fall=None, hdd_raid=None, input_aditional_keys=None,
            input_keyboard_backlight=None, input_keyboard_keycolors=None,
            input_keys_constraction=None, input_manipulator=None,
            input_multitouch=None, input_numblock=None, lan=None, material=None,
            multimedia=None, name=None, model=None, os=None, panel_bluraydrive=None, ram_max=None,
            ram_standart=None, ram_type=None, shell=None, shockproof=None,
            testcpu_3dmark06=None, testcpu_passmark=None, testcpu_super=None, testvga_3dmark=None,
            testvga_3dmark06=None, thunderbolt=None, type=None, url=None, vga_memory_type=None,
            vga_model=None, vga_number=None, waterproof=None, web_camera=None, weight=None,
            width=None, length=None, height=None, price=None, in_view=None):
        self.battery_capacity = battery_capacity
        self.battery_cells = battery_cells
        self.battery_charging_time = battery_charging_time
        self.battery_voltage = battery_voltage
        self.battery_work_time = battery_work_time
        self.cpu_frequency = cpu_frequency
        self.cpu_kernel_count = cpu_kernel_count
        self.cpu_model = cpu_model
        self.cpu_name = cpu_name
        self.com_g3 = com_g3
        self.com_bluetooth = com_bluetooth
        self.com_dialup = com_dialup
        self.com_nfs = com_nfs
        self.com_slot = com_slot
        self.com_slot_type = com_slot_type
        self.com_widi = com_widi
        self.com_wifi = com_wifi
        self.com_wimax = com_wimax
        self.display_led_backlight = display_led_backlight
        self.display_brightness = display_brightness
        self.display_contrast = display_contrast
        self.display_cover = display_cover
        self.display_diagonal = display_diagonal
        self.display_gorilla_glass = display_gorilla_glass
        self.display_light_sensor = display_light_sensor
        self.display_matrix = display_matrix
        self.display_multitouch = display_multitouch
        self.display_rotation = display_rotation
        self.display_sensor = display_sensor
        self.disply_resolution = disply_resolution
        self.hdd_capacity = hdd_capacity
        self.hdd_speed = hdd_speed
        self.hdd_type = hdd_type
        self.panel_drive = panel_drive
        self.panel_usb2 = panel_usb2
        self.panel_usb3 = panel_usb3
        self.ram_amount = ram_amount
        self.ram_jacks = ram_jacks
        self.system_bus = system_bus
        self.vga_amount = vga_amount
        self.vga_type = vga_type
        self.accoustic_format = accoustic_format
        self.additional_headphones_port = additional_headphones_port
        self.chipset = chipset
        self.color = color
        self.completeness = completeness
        self.connection_ports = connection_ports
        self.cpu_cash2 = cpu_cash2
        self.cpu_cash3 = cpu_cash3
        self.doc_station_connection = doc_station_connection
        self.hdd_capacity2 = hdd_capacity2
        self.hdd_free_fall = hdd_free_fall
        self.hdd_raid = hdd_raid
        self.input_aditional_keys = input_aditional_keys
        self.input_keyboard_backlight = input_keyboard_backlight
        self.input_keyboard_keycolors = input_keyboard_keycolors
        self.input_keys_constraction = input_keys_constraction
        self.input_manipulator = input_manipulator
        self.input_multitouch = input_multitouch
        self.input_numblock = input_numblock
        self.lan = lan
        self.material = material
        self.multimedia = multimedia
        self.name = name
        self.model = model
        self.os = os
        self.panel_bluraydrive = panel_bluraydrive
        self.ram_max = ram_max
        self.ram_standart = ram_standart
        self.ram_type = ram_type
        self.shell = shell
        self.shockproof = shockproof
        self.testcpu_3dmark06 = testcpu_3dmark06
        self.testcpu_passmark = testcpu_passmark
        self.testcpu_super = testcpu_super
        self.testvga_3dmark = testvga_3dmark
        self.testvga_3dmark06 = testvga_3dmark06
        self.thunderbolt = thunderbolt
        self.type = type
        self.url = url
        self.vga_memory_type = vga_memory_type
        self.vga_model = vga_model
        self.vga_number = vga_number
        self.waterproof = waterproof
        self.web_camera = web_camera
        self.weight = weight
        self.width = width
        self.length = length
        self.height = height
        self.price = price
        self.in_view = in_view
        if id:
            self.id = id


class wc_ConcNotebook(db.Model):
    __tablename__ = "wc_ConcNotebook"

    id = db.Column(db.Integer, primary_key=True)
    price_grn = db.Column(db.Integer)
    price_usd = db.Column(db.Integer)

    wc_Notebook_id = db.Column(db.Integer, db.ForeignKey('wc_Notebook.id'))
    device = db.relationship('wc_Notebook',
        backref=db.backref('concretes', lazy='dynamic'))

    wc_Shop_id = db.Column(db.Integer, db.ForeignKey('wc_Shop.id'))
    shop = db.relationship('wc_Shop',
        backref=db.backref('concnotebooks', lazy='dynamic'))

    def __init__(self, id=None, price_usd=None, price_grn=None, device=None, shop=None):
        self.price_grn = price_grn
        self.price_usd = price_usd
        self.shop = shop
        self.device = device
        if id:
            self.id = id


class wc_NotebookDSS(db.Model):
    __tablename__ = 'wc_NotebookDSS'

    id = db.Column(db.Integer, primary_key=True)
    hdd = db.Column(db.Float)
    cpu = db.Column(db.Float)
    display = db.Column(db.Float)
    ram = db.Column(db.Float)
    vga = db.Column(db.Float)
    os = db.Column(db.Float)
    price = db.Column(db.Float)
    size = db.Column(db.Float)
    common = db.Column(db.Float)
    web_camera = db.Column(db.Float)
    accoustic = db.Column(db.Float)
    input = db.Column(db.Float)
    com = db.Column(db.Float)
    battery = db.Column(db.Float)
    panel = db.Column(db.Float)
    weight = db.Column(db.Float)

    def __init__(self, id=None, hdd=None, cpu=None, display=None, ram=None, vga=None,
        os=None, size=None, common=None, price=None, web_camera=None, accoustic=None,
        input=None, com=None, battery=None, panel=None, weight=None):
        self.hdd = hdd
        self.cpu = cpu
        self.vga = vga
        self.ram = ram
        self.display = display
        self.os = os
        self.price = price
        self.size = size
        self.common = common
        self.web_camera = web_camera
        self.accoustic = accoustic
        self.input = input
        self.com = com
        self.battery = battery
        self.panel = panel
        self.weight = weight
        if id:
            self.id = id


class wc_User(db.Model):
    __tablename__ = 'wc_User'
    id = db.Column(db.Integer, primary_key=True)
    devices_id = db.Column(db.PickleType)
    devices_dss = db.Column(db.PickleType)

    def __init__(self, id=None, devices_id=None, devices_dss=None):
        self.devices_dss = devices_dss
        self.devices_id = devices_id
        if id:
            self.id = id


def add_computers(computers):
    for c in computers:
        comp = wc_Computer(**c)
        db.session.add(comp)
    db.session.commit()


def add_conccomputers(pairs):
    #pair: url + shop + price_grn + price_usd
    for pair in pairs:
        computer = wc_Computer.query.filter_by(url=pair['url']).first()
        shop = wc_Shop.query.filter_by(name=pair['shop']).first()
        conc = wc_ConcComputer(price_grn=pair['price_grn'], price_usd=pair['price_usd'], shop=shop,
            computer=computer)
        db.session.add(conc)
    db.session.commit()


if __name__ == '__main__':
    print db
    # db.drop_all()
    db.create_all()
