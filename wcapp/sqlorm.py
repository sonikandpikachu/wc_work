'''
Created on Sep 18, 2012

@author: Pavel

This modul realise our database as orm.
'''
from wcconfig import app, db

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


    def __init__(self, id =None, chipset=None, color=None, cpu_frequency=None, cpu_kernel_count=None, cpu_model=None,
        cpu_name=None, display_brightness=None, display_diagonal=None, display_led_backlight=None, display_sensor=None,
        display_resolution=None, hdd_capacity=None, hdd_cell=None, hdd_speed=None, hdd_type=None, height=None,
        jacks=None, length=None, material=None, media_builtin_dinamics=None, media_jacks3=None, media_microphone=None, 
        media_remote=None, media_sound=None, media_tv_tunner=None, media_web_camera=None, name=None, network=None, 
        os=None, panel_audio=None, panel_cardreader=None, panel_cell3=None, panel_cell5=None, panel_digital_display=None, 
        panel_drive=None, panel_usb2=None, panel_usb3=None, pb_power=None, ps2=None, 
        ram_amount=None, ram_frequency=None, ram_jacks=None, ram_type=None, thunderbolt=None, type=None, url=None, 
        vga_amount=None, vga_model=None, vga_type=None, weight=None, width=None, price = None,
        testcpu_passmark = None, testvga_3dmark06=None):
        self.chipset=chipset
        self.color=color
        self.cpu_frequency=cpu_frequency
        self.cpu_kernel_count=cpu_kernel_count
        self.cpu_model=cpu_model
        self.cpu_name=cpu_name
        self.display_brightness=display_brightness
        self.display_diagonal=display_diagonal
        self.display_led_backlight=display_led_backlight
        self.display_sensor=display_sensor
        self.display_resolution=display_resolution
        self.hdd_capacity=hdd_capacity
        self.hdd_cell=hdd_cell
        self.hdd_speed=hdd_speed
        self.hdd_type=hdd_type
        self.height=height
        self.jacks=jacks
        self.length=length
        self.material=material
        self.media_builtin_dinamics=media_builtin_dinamics
        self.media_jacks3=media_jacks3
        self.media_microphone=media_microphone
        self.media_remote=media_remote
        self.media_sound=media_sound
        self.media_tv_tunner=media_tv_tunner
        self.media_web_camera=media_web_camera
        self.name=name
        self.network=network
        self.os=os
        self.panel_audio=panel_audio
        self.panel_cardreader=panel_cardreader
        self.panel_cell3=panel_cell3
        self.panel_cell5=panel_cell5
        self.panel_digital_display=panel_digital_display
        self.panel_drive=panel_drive
        self.panel_usb2=panel_usb2
        self.panel_usb3=panel_usb3
        self.pb_power=pb_power
        self.ps2=ps2
        self.ram_amount=ram_amount
        self.ram_frequency=ram_frequency
        self.ram_jacks=ram_jacks
        self.ram_type=ram_type
        self.thunderbolt=thunderbolt
        self.type=type
        self.url=url
        self.vga_amount=vga_amount
        self.vga_model=vga_model
        self.vga_type=vga_type
        self.weight=weight
        self.width=width
        self.price = price
        self.testcpu_passmark = testcpu_passmark
        self.testvga_3dmark06 = testvga_3dmark06
        if id: self.id = id


class wc_ConcComputer(db.Model):
    __tablename__ = "wc_ConcComputer"

    id = db.Column(db.Integer, primary_key=True)
    price_grn = db.Column(db.Integer)
    price_usd = db.Column(db.Integer)

    wc_Computer_id = db.Column(db.Integer, db.ForeignKey('wc_Computer.id'))
    computer = db.relationship('wc_Computer',
        backref=db.backref('concretes', lazy='dynamic'))

    wc_Shop_id = db.Column(db.Integer, db.ForeignKey('wc_Shop.id'))
    shop = db.relationship('wc_Shop',
        backref=db.backref('concretes', lazy='dynamic'))

    def __init__(self, id = None, price_usd = None, price_grn = None, computer = None, shop = None):
        self.price_grn = price_grn
        self.price_usd = price_usd
        self.shop = shop
        self.computer = computer
        if id: self.id = id


class wc_Shop(db.Model):
    __tablename__ = "wc_Shop"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))

    def __init__(self, id = None, name = None):
        self.name=name
        if id: self.id = id

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

    def __init__(self, id = None, hdd = None, cpu = None, display = None, ram = None, vga = None,
        os = None, size = None, panel = None, media= None, thunderbolt = None, network = None, price = None):
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

        

class wc_User(db.Model):
    __tablename__ = 'wc_User'
    id = db.Column(db.Integer, primary_key=True)
    computers_id = db.Column(db.PickleType)
    computers_dss = db.Column(db.PickleType)

    def __init__(self, id = None, computers_id = None, computers_dss = None):
        self.computers_dss = computers_dss
        self.computers_id = computers_id
        if id: self.id = id


def add_computers(computers):
    for c in computers:
        comp = wc_Computer(**c)
        db.session.add(comp)
    db.session.commit()


def add_conccomputers(pairs):
    #pair: url + shop + price_grn + price_usd
    for pair in pairs:
        computer = wc_Computer.query.filter_by(url = pair['url']).first()
        shop = wc_Shop.query.filter_by(name = pair['shop']).first()
        conc = wc_ConcComputer(price_grn = pair['price_grn'], price_usd = pair['price_usd'], shop = shop, 
            computer = computer)
        db.session.add(conc)
    db.session.commit()


if __name__ == '__main__':
    print db
    # db.drop_all()
    db.create_all()