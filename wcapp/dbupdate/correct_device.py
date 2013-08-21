#coding: utf-8
import os
import re
import tablib
import xlrd


def _correct_devices_ram(device):
    if device.ram_amount:
        device.ram_amount = int(device.ram_amount)
        if device.ram_amount > 40 and device.ram_amount != 3096:
            device.ram_amount = device.ram_amount / 1024
        if device.ram_amount == 3096:
            device.ram_amount = 4
    return device


def _correct_computers_hdd(computer):
    if computer.hdd_capacity and u'Гб' in computer.hdd_capacity:
        new_capacity = re.findall(ur"(\d+) Гб", computer.hdd_capacity)[0]
        computer.hdd_capacity = new_capacity
    return computer


def _correct_notebooks_hdd(notebook):
    new_capacity = 0
    if notebook.hdd_capacity and u'Гб' in notebook.hdd_capacity:
        new_capacity += int(re.findall(r"(\d+) Гб", notebook.hdd_capacity)[0])
    if notebook.hdd_capacity2 and u'Гб' in notebook.hdd_capacity2:
        new_capacity += int(re.findall(r"(\d+) Гб", notebook.hdd_capacity2)[0])
    notebook.hdd_clear_capacity = new_capacity
    return notebook


def correct_device(device_type, device):
    device = _correct_devices_ram(device)
    device = _correct_notebooks_hdd(device) if device_type == 'notebook' else _correct_computers_hdd(device)
    return device



# all functions below aern`t in use
def _xls_as_datasets(path):
    wbk = xlrd.open_workbook(path)

    def sheet_to_dataset(sheet_name):
        sheet = wbk.sheet_by_name(sheet_name)
        headers = sheet.row_values(0)
        data = [map(str, sheet.row_values(i)) for i in range(1, sheet.nrows)]
        return tablib.Dataset(*data, headers=headers)

    return dict((sn, sheet_to_dataset(sn)) for sn in wbk.sheet_names())


def _device_column_values(device, columns):
    return tuple(getattr(device, c) for c in columns)


def _set_mark(device, meaning_columns, mark_columns, dataset):
    data_columns = zip(*[dataset[cn] for cn in meaning_columns])
    # print 'data_columns', data_columns
    # print 'ind', _device_column_values(device, meaning_columns)
    ind = data_columns.index(_device_column_values(device, meaning_columns))
    for mc in mark_columns:
        setattr(device, mc, dataset[mc][ind])


# not in use
def set_marks(device_type, path_to_xls, devices):
    '''
    Adds cpu marks to given device.
    If there isn`t any row for given device - adds new row to it.
    Rewrites dss file if there is new values.
    '''
    
    def meaning_columns(part):
        if part == 'cpu':
            meaning_columns = 'cpu_frequency', 'cpu_kernel_count', 'cpu_model', 'cpu_name'
            if device_type == 'notebook':
                meaning_columns += ('cpu_cash2', 'cpu_cash3')
            return meaning_columns
        if part == 'vga':
            meaning_columns = ('vga_amount', 'vga_type', 'vga_model')
            if device_type == 'notebook':
                meaning_columns += ('vga_memory_type', 'vga_number')
            return meaning_columns

    def mark_columns(part):
        if part == 'cpu':
            if device_type == 'notebook':
                return 'testcpu_3dmark06', 'testcpu_passmark', 'testcpu_super'
            else:
                return ('testcpu_passmark', )
        if part == 'vga':
            if device_type == 'notebook':
                return 'testvga_3dmark', 'testvga_3dmark06'
            else:
                return ('testvga_3dmark06', )

    datasets = _xls_as_datasets(path_to_xls)
    for part in 'cpu', 'vga':
        dataset = datasets[part]
        dataset.title = part
        is_new_values = False
        for device in devices:
            try:
                _set_mark(device, meaning_columns(part), mark_columns(part), dataset)
            except ValueError:
                print 'Warning: value', _device_column_values(device, meaning_columns(part)), 
                print 'isn`t in xls file, please add it and restart update'
                l = lambda header: getattr(device, header) if header in meaning_columns(part) else None
                dataset_row = map(l, dataset.headers)
                dataset.append(dataset_row)
                is_new_values = True

    if is_new_values:
        for dataset in datasets.values():
            open(os.path.join('tmp', device_type, str(dataset.title) + '.xls'), 'wb').write(dataset.xls)
        # with open('students.xls', 'wb') as f:
        #     f.write(book.xls)
