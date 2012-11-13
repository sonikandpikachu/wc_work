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
    cpu_model = db.Column(db.String(10))
    cpu_name = db.Column(db.String(50))
    display_brightness = db.Column(db.Integer)
    display_diagonal = db.Column(db.Integer)
    display_led_backlight = db.Column(db.Boolean)
    display_sensor = db.Column(db.Boolean)
    disply_resolution = db.Column(db.String(20))
    hdd_capacity = db.Column(db.Integer)
    hdd_cell = db.Column(db.Integer)
    hdd_speed = db.Column(db.Integer)
    hdd_type = db.Column(db.String(10))
    height = db.Column(db.Integer)
    jacks = db.Column(db.String(150))
    length = db.Column(db.Integer)
    material = db.Column(db.String(50))
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
    ram_type = db.Column(db.String(10))
    thunderbolt = db.Column(db.Integer)
    type = db.Column(db.String(100))
    url = db.Column(db.String(300))
    vga_amount = db.Column(db.Integer)
    vga_model = db.Column(db.String(100))
    vga_type = db.Column(db.String(50))
    weight = db.Column(db.Float)
    width = db.Column(db.Integer)

    def __init__(self, id =None, chipset=None, color=None, cpu_frequency=None, cpu_kernel_count=None, cpu_model=None,
        cpu_name=None, display_brightness=None, display_diagonal=None, display_led_backlight=None, display_sensor=None,
        disply_resolution=None, hdd_capacity=None, hdd_cell=None, hdd_speed=None, hdd_type=None, height=None,
        jacks=None, length=None, material=None, media_builtin_dinamics=None, media_jacks3=None, media_microphone=None, 
        media_remote=None, media_sound=None, media_tv_tunner=None, media_web_camera=None, name=None, network=None, 
        os=None, panel_audio=None, panel_cardreader=None, panel_cell3=None, panel_cell5=None, panel_digital_display=None, 
        panel_drive=None, panel_usb2=None, panel_usb3=None, pb_power=None, ps2=None, 
        ram_amount=None, ram_frequency=None, ram_jacks=None, ram_type=None, thunderbolt=None, type=None, url=None, 
        vga_amount=None, vga_model=None, vga_type=None, weight=None, width=None):
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
        self.disply_resolution=disply_resolution
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
        self.panel_usb2=panel_usb2
        self.panel_usb3=panel_usb3
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
        if id: self.id = id


def add_computers(computers):
    for c in computers:
        comp = wc_Computer(**c)
        db.session.add(comp)
    db.session.commit()



if __name__ == '__main__':
    print db
    db.drop_all()
    db.create_all()