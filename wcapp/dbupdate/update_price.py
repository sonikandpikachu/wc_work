# coding: utf-8
import re
import os
import datetime

import requests
from lxml import html, etree
from fn import F, _
from fn.uniform import map

import sqlorm as sql
from wcconfig import db


SITE = 'http://nadavi.com.ua/'

_dn = os.path.dirname

ROOT_FOLDER = os.path.realpath(_dn(_dn(_dn(__file__))))


def _create_folder_in_root(name):
    path = os.path.join(ROOT_FOLDER, name)
    if not os.path.exists(path):
        os.makedirs(path)
    return path

_create_folder_in_root('media')

NOTEBOOK_MEDIA = _create_folder_in_root(os.path.join('media', 'notebooks'))
COMPUTER_MEDIA = _create_folder_in_root(os.path.join('media', 'computers'))


def _text(element):
    return etree.tostring(element, method='text', encoding='utf-8')


def db_devices(device_table):
    return db.session.query(device_table).all()


def device_page(db_device):
    return requests.get(db_device.url).text


def device_description_urls(device_page):
    document = html.document_fromstring(device_page)
    links = document.cssselect('body div table table.dbl a')
    return [SITE + link.get('href') for link in links]


def _first_ends(end, lst):
    return filter(lambda u: u.endswith(end) or u.endswith(end + '-39.php'), lst)[0]


def device_shops_url(device_page):
    return _first_ends('prc', device_description_urls(device_page))


def device_media_url(device_page):
    return _first_ends('med', device_description_urls(device_page))


def device_images_urls(media_url):
    media_page = requests.get(media_url).text
    document = html.document_fromstring(media_page)
    links = document.cssselect('body div table div table div.img-gallery a.gitem')
    return [SITE + l.get('href') for l in links]


def device_image_src(url):
    page = requests.get(url).text
    document = html.document_fromstring(page)
    images = document.cssselect('body div table div table div.img-preview img')
    return images[0].get('src') if len(images) else None


def main_image_src(url):
    page = requests.get(url).text
    document = html.document_fromstring(page)
    images = document.cssselect('body div table div table.slide-table img#img_slide')
    return SITE+images[0].get('src')


def _images_folder(db_device, folder):
    images_folder = os.path.join(folder, str(db_device.id)+'_img')
    if not os.path.exists(images_folder):
        os.makedirs(images_folder)
    return images_folder


def _save_image(images_folder, index, src):
    f = open(os.path.join(images_folder, str(index) + '.' + src.split('.')[-1]), 'wb')
    f.write(requests.get(src).content)
    f.close()


def save_images(db_device, folder, images):
    images_folder = _images_folder(db_device, folder)
    for i, image in enumerate(images):
        _save_image(images_folder, i, image)


def device_shops_blocks(shop_url):
    shop_page = requests.get(shop_url).text
    document = html.document_fromstring(shop_page)
    blocks = document.cssselect('body div table div table '
                                'table.shop-price-position td.lline div.text a')
    return blocks


def _int_from_str(s):
    return ''.join(re.findall(r'\d+', "".join(s.split())))


def shop_dict(shop_block):
    sd = {
        'name': _text(shop_block.cssselect('u')[0]),
        'price': _int_from_str(_text(shop_block.cssselect('span.ac span.price-in-list')[0])),
        'url': requests.get(shop_block.get('onmouseover').split('"')[1]).url
    }
    return sd


def get_or_create_shop(name):
    shop = db.session.query(sql.wc_Shop).filter_by(name=name).first()
    if shop:
        return shop
    else:
        shop = sql.wc_Shop(name=name)
        db.session.add(shop)
        db.session.commit()
        return shop


def create_concdevice(concdevice_table, device, shop_d):
    shop = get_or_create_shop(shop_d['name'])
    concdevice = concdevice_table(
        price_grn=shop_d['price'], device=device, shop=shop, url=shop_d['url'])
    db.session.add(concdevice)
    db.session.commit()
    return concdevice


def update_prices(table, conctable, media_folder):
    devices = db_devices(table)
    shop_dicts = F() >> device_page >> device_shops_url >> device_shops_blocks\
        >> F(map, shop_dict)
    media_images = F() >> device_page >> device_media_url >> device_images_urls\
        >> F(map, device_image_src) >> F(filter, bool)
    for device in devices:
        days_ago = datetime.datetime.now() - datetime.timedelta(days=45)
        if not device.last_update or device.last_update < days_ago:
            print 'updating device #%s: url %s' % (device.id, device.url)
            print 'creating concdevices...'
            concdevices = [create_concdevice(conctable, device, shop_d)
                           for shop_d in shop_dicts(device)]
            prices = [cd.price_grn for cd in concdevices]
            price = sum(prices) / float(len(prices)) if concdevices else -1
            if price > 0:
                print 'downloading and saving media...'
                sources = [main_image_src(device.url)] + media_images(device)
                save_images(device, media_folder, sources)
            else:
                print '...no concdevices for this model'
            db.session.query(table).filter_by(id=device.id).update(
                {"last_update": datetime.datetime.now(), 'price': price})
            db.session.commit()
            print ''
        else:
            print 'already-up-todate'
