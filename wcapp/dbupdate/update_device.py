# coding: utf-8
from lxml import html, etree
import re
import os
import requests
import copy
import tablib
from datetime import datetime, timedelta

import sqlorm as sql
from wcconfig import db
from correct_device import correct_device, set_marks
from save_load import pickle_save, pickle_load

SITE = 'http://nadavi.com.ua/'

CONF = {
    'computer': {
        'links_url': 'http://nadavi.com.ua/src/170/src-39.php',
        'db_table': sql.wc_Computer,
    },
    'notebook': {
        'links_url': 'http://nadavi.com.ua/src/298/src-39.php',
        'db_table': sql.wc_Notebook,
    }
}


def _text(element):
    return etree.tostring(element, method='text', encoding='utf-8')


def _page(url, params={}):
    ''' return string downloaded from url '''
    return requests.get(url, params=params).text


def _device_documents(device):
    ''' 
    Iterates over pages, which contains list of devices.
    Creates html document from each page
    '''

    def _is_last_page(page_document):
        names = page_document.cssselect(
            'body div table div table div.name-big')
        return len(names) < 10

    url = CONF[device]['links_url']
    i = 0
    while True:
        document = html.document_fromstring(_page(url, params={'page_': i}))
        yield document
        if _is_last_page(document):
            break
        i += 1
        # only for debug:
        # if i > 0:
        #     break


def _picke_path(name):
    return os.path.join('dbupdate', 'values', name)


def cache(name, cache_data):
    data = {'time': datetime.now(), 'data': cache_data}
    pickle_save(_picke_path(name), data)


def get_cached(name):
    path = _picke_path(name)
    if os.path.exists(path):
        data = pickle_load(path)
        if data['time'] > datetime.now() - timedelta(days=30):
            return data['data']


def download_links(device):
    ''' Downloads all currently existed on nadavi links '''
    print 'downloading links, names and models'

    cached_links = get_cached(device+'_links.pkl')
    if cached_links:
        print 'loading links from cache'
        return cached_links

    def _names_models_links(document):
        ''' Takes all names-models-links from given page '''
        name_blocks = document.cssselect('body div table div table tr')
        result = []
        for block in name_blocks:
            # this try-catch ignores tr blocks of table whitch doesn`t have any
            # computers description
            try:
                name = _text(block.cssselect('div.name-big')[0])
            except IndexError:
                continue
            models = [_text(m)
                      for m in block.cssselect('table.conf-table a.conf-name u')]
            links = [SITE + a.get('href')
                     for a in block.cssselect('table.conf-table a.conf-name')]
            if len(models) != len(links):
                print 'length of models != length of links - this is bad. This block willl be ignored.'
                continue
            result += [(name, model, link)
                       for model, link in zip(models, links)]
        return result

    nml = []
    print 'downloading from page #',
    for i, document in enumerate(_device_documents(device)):
        print i,
        nml += _names_models_links(document)
    print '[Done]'

    cache(device + '_links.pkl', nml)

    return nml


def compare_links(device, nml):
    ''' 
    Takes name-model-link(nml) list of models and compares it with db data. 
    If this model exists in db - element will be removed from nml list
    '''
    all_devices = db.session.query(CONF[device]['db_table']).all()
    db_links = [d.url for d in all_devices]
    db_models_and_names = [(d.name, d.model) for d in all_devices]

    def not_in_db(nml_el):
        name, model, link = nml_el
        if link in db_links or (name, model) in db_models_and_names:
            return False
        else:
            return True
    return filter(not_in_db, nml)


def download_nadavi_device(nml_el):
    name, model, link = nml_el
    document = html.document_fromstring(_page(link))
    device = {}
    prefix = 'Устройство'
    tds = iter(document.cssselect('body div table div table table td'))
    for td in tds:
        if td.get('class') == 'llineo':
            td_name = prefix + '.' + _text(td).strip()
            td_value = _text(tds.next())
            device[td_name] = td_value
        if td.get('class') == 'dlineo':
            prefix = _text(td).strip()
            tds.next()
    device['Устройство.url'] = link
    device['Устройство.имя'] = name
    device['Устройство.модель'] = model
    return device


def _config_file(device):
    return open(os.path.join('dbupdate', 'config', device + '.config'))


def is_full_config(device, nadavi_devices):
    nadavi_devices_keys = [nd.keys() for nd in nadavi_devices]
    nadavi_names = set(reduce(lambda a, b: a + b, nadavi_devices_keys))
    config_names = set([l.split('|')[0].strip()
                       for l in _config_file(device).readlines()])
    not_in_config = [nn for nn in nadavi_names if not nn in config_names]
    if not_in_config:
        print 'Warning! Next values aren`t in config file, please add them to it and start update again'
        for n in not_in_config:
            print n
        return False
    return True


def save_devices(device, nadavi_devices):
    config_lines = [l for l in _config_file(
        device).readlines() if len(l.split('|')) > 1]

    def split_config(line):
        return [el.strip() for el in line.split('|')[:3]]

    def to_db_device_dict(nadavi_device):
        db_device_dict = {}
        for line in config_lines:
            nadavi_name, db_name, pattern = split_config(line)
            if nadavi_name in nadavi_device:
                if db_name == 'height ; width ; length':
                    for i, name in enumerate(['height', 'width', 'length']):
                        db_device_dict[name] = re.findall(
                            pattern, nadavi_device[nadavi_name])[i]
                else:
                    try:
                        db_device_dict[db_name.lower()] = re.findall(
                            pattern, nadavi_device[nadavi_name])[0].strip()
                    except IndexError as er:
                        if db_name == 'RAM_amount':
                            db_device_dict[db_name.lower()] = 0
                        if db_name == 'Разъемы и подключения.Thunderbolt':
                            db_device_dict[db_name.lower()] = '-'
                        else:
                            print nadavi_device[nadavi_name]
                            print er, ': pattern -', pattern, 'db_name -',
                            print db_name, 'nadavi_name -', nadavi_name
                            raise IndexError
        return db_device_dict

    db_table = CONF[device]['db_table']
    dataset = tablib.Dataset(headers=db_table().headers())
    for db_device_dict in map(to_db_device_dict, nadavi_devices):
        db_device = correct_device(device, db_table(**db_device_dict))
        dataset.append(db_device.to_list())
        db.session.add(db_device)
    db.session.commit()

    open(os.path.join('dbupdate', 'values', str(device) + '.xls'),
         'wb').write(dataset.xls)
    open(os.path.join('dbupdate', 'values', str(device) + '.json'),
         'wb').write(dataset.json)


def _export_dss(device):
    ''' Export data from db to `device`_dss.xls '''
    import xlwt
    wbk = xlwt.Workbook()
    db_table = CONF[device]['db_table']
    prefixes = 'cpu', 'vga'
    tests = 'testcpu', 'testvga'
    for prefix, test in zip(prefixes, tests):
        all_values = {}
        id_values = {}
        columns =db_table.columns_by_prefix(prefix) + db_table.columns_by_prefix(test)
        print columns
        for d in db_table.query.all():
            values = tuple(getattr(d, column) for column in columns)
            if values in all_values:
                all_values[values].append(d.url)
                id_values[values].append(d.id)
            else:
                all_values[values] = [d.url]
                id_values[values] = [d.id]
        sheet = wbk.add_sheet(prefix)
        for i, column in enumerate(columns + ['id', 'url']):
            sheet.write(0, i, column)
        for i, values in enumerate(all_values):
            for j, value in enumerate(values):
                sheet.write(i + 1, j, value)

            sheet.write(i + 1, len(values) + 1, ', '.join(str(v)
                        for v in all_values[values]))
            sheet.write(i + 1, len(values), ', '.join(
                [str(v) for v in id_values[values]]))
    wbk.save(os.path.join('dbupdate', 'dss', str(device) + '.xls'))


def update_devices(device):
    print 'updating devices: ' + device

    if get_cached(device+'_nadavi.pkl'):
        print 'downloading devices from cache'
        nadavi_devices = get_cached(device+'_nadavi.pkl')
    else:
        nml = download_links(device)
        print 'devices on nadavi:', len(nml)
        nml = compare_links(device, nml)
        print 'not in our base:', len(nml)
        nadavi_devices = map(download_nadavi_device, nml)
        cache(device+'_nadavi.pkl', nadavi_devices)
    if is_full_config(device, nadavi_devices):
        print 'Config is ok. Writing devices into database, .xls and .json ...'

        save_devices(device, nadavi_devices)


def export_dss(device):
    print 'exporting dss for devices:', device
    _export_dss(device)


def set_existed_dss(device):
    ''' Set dss marks to devices, which configurations already exists in our base '''

    db_table = CONF[device]['db_table']

    def existed_dss(prefix, mark_column):
        return dict((d.values_by_prefix(prefix), getattr(d, mark_column))
                    for d in db_table.query.all() if getattr(d, mark_column) is not None)

    def dss_by_prefix(prefix, mark_column):
        edss = existed_dss(prefix, mark_column)
        print 'edss', edss
        for d in db_table.query.all():
            device_values = d.values_by_prefix(prefix)
            if (device_values in edss.keys() and
                    getattr(d, mark_column) is None):
                db_device = db.session.query(db_table).filter_by(id=d.id)
                db_device.update({mark_column: edss[device_values]})
        db.session.commit()


    for prefix in 'cpu', 'vga':
        mark_columns = db_table.columns_by_prefix('test' + prefix)
        print mark_columns
        for mark_column in mark_columns:
            dss_by_prefix(prefix, mark_column)
