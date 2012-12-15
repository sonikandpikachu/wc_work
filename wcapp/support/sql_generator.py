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
    for device in devices:
        print ', '.join([key for key in device.keys() if '3' in key])
    # key = 'Передняя панель.Разъемов USB 3 '
    # for dev in devices:
    #     if key in dev:
    #         print 'is'
    #         break
    # type = set([device[key] for device in devices if key in device])
    # for t in type:
    #     print t
    # names = _russian_sql_attributes(devices)
    # s = []
    # for key in names:
    #     if not key.split('.')[1] in ('магазины', 'цены_длр', 'цены_грн', 'url'):
    #         s.append(key +  ', '.join(set([device[key] for device in devices if key in device])))
    # s.sort()
    # print '\n'.join(s)


def table_code(columns, table_name):
    code = 'class wc_' + table_name + '(Base):'
    code += '\n\t__tablename__ = "wc_' + table_name + '"'  
    code += '\n\tid = db.Column(db.Integer, primary_key=True)\n'
    str_columns = []
    for column in columns:
        for name, type in zip(column['names'], column['types']):
            str_columns.append('\t' + name.strip().lower() + ' = al.Column(al.' + type + ')')
    # str_columns.sort()
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
        if len(line.split('|')) < 4: continue
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
# ALTER TABLE `wc`.`wc_computer` ADD COLUMN `battery_charging_time` FLOAT NULL  AFTER `price` , ADD COLUMN `battery_work_time` FLOAT NULL  AFTER `battery_charging_time` ;

def alter_query (config):
    query = 'ALTER TABLE `wc`.`wc_computer`'
    for column in table_columns(config):
        query += ',\n ADD COLUMN `' + column['names'][0] + '` ' +  column['types'][0].upper() + ' NULL '
    return query.replace('STRING', 'VARCHAR').replace('BOOLEAN', 'TINYINT(1)').replace('INTEGER', 'INT(11)')

def create_notebooks_config ():
    all_notebook_parameters = set()
    for notebook_file in [nbf for nbf in os.listdir('../../data/notebooks') if nbf.endswith('.pkl')]:
        notebook = sl.pickle_load('../../data/notebooks/' + notebook_file)
        for key in notebook.keys():
            all_notebook_parameters.add(key.decode('utf-8'))
    import codecs
    notebookconf = codecs.open('values', 'wb')
    computerconf = codecs.open('config/computers.config', 'rb', encoding = 'utf-8')
    sorted_notebook_parameters = []
    for line in computerconf.readlines():
        print line.split('|')[0].replace('_', '.').strip() in all_notebook_parameters
        if line.split('|')[0].replace('_', '.').strip() in all_notebook_parameters:
            sorted_notebook_parameters.append(line)
    # print list(all_notebook_parameters)[0].decode('utf-8')
    sorted_notebook_parameters.sort()
    print sorted_notebook_parameters
    notebookconf.write(''.join(sorted_notebook_parameters))
    notebookconf.close()
    computerconf.close()


if __name__ == '__main__':
    # create_notebooks_config()
    # rename_usb('../data/computers')
    # save_sqlconf_file(('../../data/',), 'config/notebooks2.config')
    columns = table_columns('config/notebooks.config')
    columns.sort()
    print table_code(columns, 'Notebook')
    # print alter_query('config/notebooks.config')



