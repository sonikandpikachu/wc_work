#coding: utf-8

import os, sys, re

import xlrd

import sqlorm

float_substitutions = {'-' : 0, u'64(флэш-памяти)+128' : 192} 

def get_all_elements(path, config):
	wb = xlrd.open_workbook(path)
	sh = wb.sheet_by_index(0)
	elements = []
	for rownum in range(1, sh.nrows):
		element = {}
		for conf in config:
			try:
				value = sh.cell(rownum, config[conf]).value
				element[conf] = value if unicode(value) else None
			except IndexError as er:
				print 'IndexError:', er, 'in row:', rownum, 'column:', config[conf]
				sys.exit("IndexError")
		elements.append(element)
	del wb
	return elements


def insert_all_elements(tableclass, elements, types):
	controller = sqlorm.SQLController()
	session = controller.create_sql_session()
	for element in elements:
		if element['id'] == element['id_ref']:
			table_element = tableclass()
			del element['id_ref']
			for key in element.iterkeys():
				if isinstance(element[key], basestring): element[key] = unicode(element[key])
				if types[key] == float and element[key] in float_substitutions: 
					element[key] = float_substitutions[element[key]] 
				if element[key]: table_element.__dict__[key] = types[key](element[key]) 
			session.add(table_element)
	session.commit()


def insert_lists():
	configs = {
		'hd' : ({'hdd_amount' : 0, 'ssd_amount' : 1, 'dss' : 4, 'interface' : 5, 'speed' : 6, 'id' : 8, 'id_ref' : 9}, sqlorm.wc_HD),
		'odd' : ({'name' : 0, 'dss' : 2, 'type' : 3, 'id' : 4, 'id_ref' : 5}, sqlorm.wc_ODD),
		'cpu' : ({'cores' : 6, 'frequency' : 1, 'dss' : 4, 'name' : 0, 'threads' : 11, 'id' : 3, 'id_ref' : 5}, sqlorm.wc_CPU),
		'os' : ({'dss' : 3, 'name' : 0, 'type' : 1, 'id' : 4, 'id_ref' : 5}, sqlorm.wc_OS),
		'ram' : ({'dss' : 9, 'amount' : 7, 'name' : 0, 'max_amount' : 8, 'id' : 10, 'id_ref' : 11}, sqlorm.wc_RAM),
		'chipset' : ({'name' : 0, 'id' : 1, 'id_ref' : 2}, sqlorm.wc_Chipset),
		'screen' : ({'size' : 0, 'resolution' : 1, 'cover' : 2, 'id' : 3, 'id_ref' : 4}, sqlorm.wc_Screen),
		'type' : ({'name' : 0, 'id' : 1, 'id_ref' : 2}, sqlorm.wc_Type),
	}

	types = {
		'hd' : {'hdd_amount' : float, 'ssd_amount' : float, 'dss' : float, 'interface' : unicode, 'speed' : unicode, 'id' : int, 'id_ref' : int},
		'odd' : {'name' : unicode, 'dss' : float, 'type' : unicode, 'id' : int, 'id_ref' : int},
		'cpu' : {'cores' : float, 'frequency' : float, 'dss' : float, 'name' : unicode, 'threads' : float, 'id' : int, 'id_ref' : int},
		'os' : {'dss' : float, 'name' : unicode, 'type' : unicode, 'id' : int, 'id_ref' : int},
		'ram' : {'dss' : float, 'amount' : float, 'name' : unicode, 'max_amount' : float, 'id' : int, 'id_ref' : int},
		'chipset' : {'name' : unicode, 'id' : int, 'id_ref' : int},
		'screen' : {'size' : unicode, 'resolution' : unicode, 'cover' : unicode, 'id' : int, 'id_ref' : int},
		'type' : {'name' : unicode, 'id' : int, 'id_ref' : int},
	}
	work_keys = ['ram']
	assert not set(configs.keys()) - set(types.keys()), 'Error: configs and types containes different keys'
	assert not set(work_keys) - set(configs.keys()), 'Error: There is no work_keys in configs' 
	for key in work_keys:
		path = os.path.join('..','Comp elements', key.upper() + 'Final.xls')
		elements = get_all_elements(path, configs[key][0])
		insert_all_elements(configs[key][1], elements, types[key])


def get_xls_computers(sh):
	computers = []
	for rownum in range(2, sh.nrows):
		computers.append(sh.row_values(rownum))
	return computers


def parse_comp_name(sh, column):
	'''creates new computers in database and inits their names'''
	controller = sqlorm.SQLController()
	session = controller.create_sql_session()
	for rownum in range(2, sh.nrows):
		value = unicode(sh.cell(rownum, column).value)
		comp = sqlorm.wc_Computer(name = value)
		session.add(comp)
	session.commit()
	

def show_simple_comp_column(sh, column):
	controller = sqlorm.SQLController()
	session = controller.create_sql_session()
	values = set()
	for rownum in range(2, sh.nrows):
		value = unicode(sh.cell(rownum, column).value)
		values.add(value)
	for v in values:
		print [v]


def insert_simple_column(sh, colname, valuefunction):
	xlscomputers = get_xls_computers(sh)
	controller = sqlorm.SQLController()
	session = controller.create_sql_session()
	for xlscomp in xlscomputers:
		value = valuefunction(xlscomp[xls_columns[colname]])
		computer = session.query(sqlorm.wc_Computer).filter_by(name = xlscomp[xls_columns['name']]).first()
		setattr(computer, colname, value)
		session.flush()
	session.commit()	


def valuefunc(column):
	def Bluetoothfunc (value): 
		return 0 if value in (u'-', u'', u'н.д.') else 1
	def simplefunc(value): return 0 if not value else 1
	def strfunc(value): return value
	def concatestrfunc(value): return value[:100]
	def wimaxfunc(value): return 1 if value == u'+' else 0
	def weightfunc(value): return float(value.replace(u',', u'.')) if not value in (u'', u'н.д.') else -1
	def widthfunc(value):
		value = re.findall('[\d\.]+', value.replace(u',', u'.'))[0]
		return float(value) if value else -1
	def lengthfunc(value):
		value = re.findall('[\d\.]+', value.replace(u',', u'.'))
		if len(value) < 2: return -1
		return float(value[1]) if value[0] and value[1] and value[1] != u'.' else -1
	def heightfunc(value):
		value = re.findall('[\d\.]+', value.replace(u',', u'.'))
		if len(value) < 3: return -1
		value[2] = value[2].replace(u'3.5.6', '3.5')
		return float(value[2]) if value[0] and value[2] and value[2] != u'.' else -1
	def pricefunc(value):
		value = value[1:-1].replace('\'','').replace(',','').replace('-','')
		if value:
			values = [float(v) for v in value.split()]
			return sum(values)/len(values)
		return 0

	all_functions = {
		'Bluetooth' : Bluetoothfunc,
		'webcamera' : simplefunc,
		'wifi' : simplefunc,
		'wimax' : wimaxfunc,
		'slot' : strfunc, 
		'cardreader' : Bluetoothfunc,
		'out_ports' : concatestrfunc,
		'modem56' : wimaxfunc, 
		'network_adapter' : Bluetoothfunc,
		'G3' : Bluetoothfunc,
		'weight' : weightfunc,
		'width' : widthfunc,
		'length' : lengthfunc,
		'height' : heightfunc,
		'maker_url' : strfunc,
		'price' : pricefunc,
		'type' : strfunc
	}
	return all_functions[column]


def insert_complex_column(sh, el_sh, el_id_ref_column, columnname, identical_columns):
	xlscomputers = get_xls_computers(sh)
	xlselements = [el_sh.row_values(rownum) for rownum in range(1, el_sh.nrows)]
	controller = sqlorm.SQLController()
	session = controller.create_sql_session()

	def isavailable(xlselement, xlscomp):
		for key in identical_columns:
			element = unicode(xlselement[identical_columns[key]])
			# print element, [unicode(xlscomp[k]) for k in key], element in [unicode(xlscomp[k]) for k in key]
			if not element in [unicode(xlscomp[k]) for k in key]: return False
			if not element and [xlscomp[k] for k in key if xlscomp[k]]: return False
		return True

	for index, xlselement in enumerate(xlselements):
		# print xlselement
		available_computers = [xlscomp for xlscomp in xlscomputers if isavailable(xlselement, xlscomp)]
		computers = [session.query(sqlorm.wc_Computer).filter_by(name = avcomp[xls_columns['name']]).first() 
																			for avcomp in available_computers]
		for comp in computers:
			setattr(comp, 'id_wc_' + columnname, int(xlselement[el_id_ref_column]))
			# print comp.name
		print index + 1,'/', len(xlselements)
		session.flush()
	session.commit()


xls_columns = {'name' : 37, 'Bluetooth' : 39, 'webcamera' : 27, 'wifi' : 32, 'wimax' : 28, 'slot' : 13, 'cardreader' : 12,
				'out_ports' : 19, 'modem56' : 24, 'network_adapter' : 16, 'G3' : 11, 'weight' : 15, 'width' : 10, 
				'height' : 10, 'length' : 10, 'maker_url' : 43, 'price' : 44}

#first index - column in computers file, second - column in element file
complex_columns = {
	'OS' : {(42, 30) : 0},
	'HD' : {(4,) : 5, (36, 40) : 7},
	'ODD' : {(3, 0) : 0},
	'CPU' : {(8,) : 0},
	'RAM' : {(5, 29) : 5},
	'Screen' : {(14,) : 0, (20,) : 1, (22,) : 2},
	'Chipset' : {(25,) : 0},
	'Type' : {(18,) : 0},
}


def insert_comp_columns():
	wb = xlrd.open_workbook(os.path.join('..','Comp elements', 'all_computers.xls'))
	sh = wb.sheet_by_index(0)

	# inserting simple columns:
	columnname = 'cardreader'
	# show_simple_comp_column(sh, xls_columns[columnname])
	insert_simple_column(sh, columnname, valuefunc(columnname))

	# inserting complex columns
	# # OS
	# columnname, id_ref_column = 'OS', 5
	# el_wb = xlrd.open_workbook(os.path.join('..','Comp elements', columnname.upper() + 'Final.xls'))
	# el_sh = el_wb.sheet_by_index(0)
	# insert_complex_column(sh, el_sh, id_ref_column, columnname, complex_columns[columnname])

	# # HD
	# columnname, id_ref_column = 'HD', 9
	# el_wb = xlrd.open_workbook(os.path.join('..','Comp elements', columnname.upper() + 'Final.xls'))
	# el_sh = el_wb.sheet_by_index(0)
	# insert_complex_column(sh, el_sh, id_ref_column, columnname, complex_columns[columnname])

	# # ODD
	# columnname, id_ref_column = 'ODD', 5
	# el_wb = xlrd.open_workbook(os.path.join('..','Comp elements', columnname.upper() + 'Final.xls'))
	# el_sh = el_wb.sheet_by_index(0)
	# insert_complex_column(sh, el_sh, id_ref_column, columnname, complex_columns[columnname])

	# # CPU
	# columnname, id_ref_column = 'CPU', 5
	# el_wb = xlrd.open_workbook(os.path.join('..','Comp elements', columnname.upper() + 'Final.xls'))
	# el_sh = el_wb.sheet_by_index(0)
	# insert_complex_column(sh, el_sh, id_ref_column, columnname, complex_columns[columnname])

	# RAM
	# columnname, id_ref_column = 'RAM', 9
	# el_wb = xlrd.open_workbook(os.path.join('..','Comp elements', columnname.upper() + 'Final.xls'))
	# el_sh = el_wb.sheet_by_index(0)
	# insert_complex_column(sh, el_sh, id_ref_column, columnname, complex_columns[columnname])

	# # SCREEN
	# columnname, id_ref_column = 'Screen', 4
	# el_wb = xlrd.open_workbook(os.path.join('..','Comp elements', columnname.upper() + 'Final.xls'))
	# el_sh = el_wb.sheet_by_index(0)
	# insert_complex_column(sh, el_sh, id_ref_column, columnname, complex_columns[columnname])

	# # CHIPSET
	# columnname, id_ref_column = 'Chipset', 2
	# el_wb = xlrd.open_workbook(os.path.join('..','Comp elements', columnname.upper() + 'Final.xls'))
	# el_sh = el_wb.sheet_by_index(0)
	# insert_complex_column(sh, el_sh, id_ref_column, columnname, complex_columns[columnname])

	# # TYPE
	# columnname, id_ref_column = 'Type', 2
	# el_wb = xlrd.open_workbook(os.path.join('..','Comp elements', columnname.upper() + 'Final.xls'))
	# el_sh = el_wb.sheet_by_index(0)
	# insert_complex_column(sh, el_sh, id_ref_column, columnname, complex_columns[columnname])

	del wb


if __name__ == '__main__':
	# create not computer tables:
	# insert_lists()
	
	# modify computer table:
	insert_comp_columns()







