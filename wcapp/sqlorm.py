'''
Created on Sep 18, 2012

@author: Pavel

This modul realise our database as orm.
'''
from wcconfig import db
import os
import csv
import tablib


class DeviceMixin(object):

    id = db.Column(db.Integer, primary_key=True)

    def __init__(self, **kwargs):
        for column in [c.name for c in self.__table__.columns]:
            if column in kwargs:
                self._setattr(column, kwargs[column])
            else:
                if column != 'id':
                    self._setattr(column, None)

    def columns_by_type(self, ctype):
        return [c.name for c in self.__table__.columns if str(c.type)==ctype]

    def _setattr(self, attrname, attrvalue):
        if attrvalue is not None:
            if attrname in self.columns_by_type('BOOLEAN'):
                attrvalue = 1 if u'+' in attrvalue else 0
            if attrname in self.columns_by_type('INTEGER'):
                attrvalue = int(attrvalue) if attrvalue != '' else 0
            if attrname in self.columns_by_type('FLOAT'):
                attrvalue = float(attrvalue)
        setattr(self, attrname, attrvalue)

    def headers(self):
        return sorted([k for k in self.__dict__.keys() if not k.startswith('_')])

    def to_list(self):
        return [self.__dict__[h] for h in self.headers()]

    @classmethod
    def columns_by_prefix(type, prefix):
        ''' Warning: Returns columns names as strings '''
        return [c.name for c in type.__table__.columns if c.name.startswith(prefix)]

    def values_by_prefix(self, prefix):
        return tuple(
            getattr(self, c) for c in self.__class__.columns_by_prefix(prefix))


class wc_Computer(DeviceMixin, db.Model):
    __tablename__ = "wc_Computer"

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
    hdd_clear_capacity = db.Column(db.Integer)
    last_update = db.Column(db.DateTime)


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

    url = db.Column(db.String(500))

    def __init__(self, id=None, price_usd=None, price_grn=None, device=None, shop=None, url=None):
        self.price_grn = price_grn
        self.price_usd = price_usd
        self.shop = shop
        self.device = device
        self.url = url
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


class wc_Notebook(DeviceMixin, db.Model):
    __tablename__ = "wc_Notebook"

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
    hdd_clear_capacity = db.Column(db.Integer)
    last_update = db.Column(db.DateTime)



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

    url = db.Column(db.String(500))

    def __init__(self, id=None, price_usd=None, price_grn=None, device=None, shop=None, url=None):
        self.price_grn = price_grn
        self.price_usd = price_usd
        self.shop = shop
        self.device = device
        self.url = url
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
