#coding: utf-8

import os

import utf8_converter
import save_load as sl

def _russian_sql_attributes(devices):
    '''
    Returns russian attributes from all given devices
    '''
    names = set() # all posible names(attribute and table)
    examples = {} # computers urls, where key apears at first time
    for device in devices:
        for key in set([key for key in device.iterkeys()]) - names: 
            examples[key] = device['Устройство.url']  
        names = names | set([key for key in device.iterkeys()])
    return names


def save_sqlconf_file(devices_folders, output):
    device_files = []
    for devices_folder in devices_folders:
        device_files += [os.path.join(devices_folder,file) for file in os.listdir(devices_folder) 
                                                    if os.path.isfile(os.path.join(devices_folder,file))]
    devices = [sl.pickle_load(file) for file in device_files]
    key = 'Передняя панель.Разъемов USB 3 '
    for dev in devices:
        if key in dev:
            print 'is'
            break
    type = set([device[key] for device in devices if key in device])
    for t in type:
        print t
    names = _russian_sql_attributes(devices)
    s = []
    for key in names:
        if not key.split('.')[1] in ('магазины', 'цены_длр', 'цены_грн', 'url'):
            s.append(key +  ', '.join(set([device[key] for device in devices if key in device])))
    s.sort()
    print '\n'.join(s)


def table_code(columns, table_name):
    code = 'class wc_' + table_name + '(Base):'
    code += '\n\t__tablename__ = "wc_' + table_name + '"'  
    code += '\n\tid = db.Column(db.Integer, primary_key=True)\n'
    str_columns = []
    for column in columns:
        for name, type in zip(column['names'], column['types']):
            str_columns.append('\t' + name.strip().lower() + ' = al.Column(al.' + type + ')')
    str_columns.sort()
    # writing columns deffinition
    code += '\n'.join(str_columns)
    # writing __init__ method:
    code += '\n\tdef __init__(self' + ', '.join([col.split('=')[0].strip() + '=None' for col in str_columns]) \
             + '):'
    code += '\n\t\tself.'.join([col.split('=')[0].strip() + '=' + col.split('=')[0].strip() for col in str_columns])
    code += '\n\t\tif id: self.id = id'
    return code


def table_columns(config):
    '''
    Returns columns: their russion name, columns names in database, types and parsers methods(for package re)
    '''
    f = open(config)
    columns = []
    for line in f.xreadlines():
        keys = ['russian_name', 'names', 'parsers', 'types']
        column = {}
        for i, key in enumerate(keys):
            # print key, line
            column[key] = line.split('|')[i].strip().split(';')
        column['russian_name'] = column['russian_name'][0].replace('_', '.')
        assert len(column['names']) == len(column['parsers']) == len(column['types']), \
                'different length for names, parsers, types' 
        columns.append(column)
    return columns


if __name__ == '__main__':
    # rename_usb('../data/computers')
    # save_sqlconf_file(('../data/computers',), 'config/sqltables.config')
    columns = table_columns('config/computers.config')
    print table_code(columns, 'Computer')
    



