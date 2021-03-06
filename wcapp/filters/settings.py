#coding: utf-8
'''
Created on Sep 30, 2012

@author: Pavel

This class describes all filters for answers. Every filter has to realise class filters.Filter or its implementation.
For more details look filters.py
'''
from sqlorm import wc_Computer
#from sqlorm import wc_Notebook
from wcconfig import db
from dss import DSS_WEIGHTS
import filters


#----------------------------------------------------------------------------------------------------------------------------------------------------------
#Price:

def priceC_cut_function(selected_values):
	return 'price > ' + selected_values[0].split(';')[0]  + ' AND ' + 'price < ' + selected_values[0].split(';')[1]
priceCFilter = filters.SliderDoubleFilter('priceC', u'Цена:',1000, 50000, [4000, 10000], style = "width: 80%",
											cut_function = priceC_cut_function, heterogeneity = [10000, 20000], 
											dimension = u' грн', step = 50)

def priceN_dss_function(selected_values):
	if int(selected_values[0]) > 0:
		return {'price' : -int(selected_values[0])*7}
	else:
		return {'price' : -int(selected_values[0])*5}

priceDescription = 'price'
priceNFilter = filters.SliderSingleFilter('priceN', u'Важность цены:', -3, 3, 0, scale = '[-3,-2,-1, 0, 1, 2, 3]',
									labels = [u'Не имеет значения', u'Максимальная економия'], description = priceDescription, 
									dss_function = priceN_dss_function)

priceFilter = filters.TwoPartFilter('price', cPart =  priceCFilter, nPart =  priceNFilter)

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#Performance:
def performanceN_dss_function(selected_values):
	return {'cpu' : int(selected_values[0])*1.5,'ram' : int(selected_values[0])}


descriptionPerformanceN = 'performance'
performanceNFilter = filters.SliderSingleFilter('perfN', u'Производительность:', 0, 5, 0,
									labels = [u'Нормальная', u'Очень высокая'], description = descriptionPerformanceN, dss_function = performanceN_dss_function)


def cpu_cut_function(selected_values):
	if '1lvl' in selected_values: return 'testcpu_passmark <= 2000'
	if '2lvl' in selected_values: return 'testcpu_passmark <= 3500 AND testcpu_passmark > 2000'
	if '3lvl' in selected_values: return 'testcpu_passmark <= 6000 AND testcpu_passmark > 3500'
	if '4lvl' in selected_values: return 'testcpu_passmark > 6000'
	return ""	

texts = u'все', u"первый уровень (<2 Ггц, 1,2 ядра)", u'второй уровень (2-3 Ггц, 2,4 ядра)',\
u'третий уровень (2.5-3.5 Ггц, 2,4 ядра)', u'четвертый уровень (>3 Ггц, 4,6 ядер)'
values =  'all','1lvl', '2lvl', '3lvl', '4lvl'
performanceCpuFilter = filters.RadioFilter('perfCpu', u'Производительность процессора:', 
									texts, values, cut_function = cpu_cut_function)

def ram_cut_function(selected_values):
	#return 'ram_amount >= ' + selected_values[0].split(';')[0]  + ' AND ' + 'ram_amount <= ' + selected_values[0].split(';')[1]
	return '(ram_amount >= ' + selected_values[0].split(';')[0]  + ' AND ' + 'ram_amount <= ' + selected_values[0].split(';')[1] + ")" 
performanceRamFilter  = filters.SliderDoubleFilter('perfRam', u'Оперативная память:',0, 16, [4, 8], 
											cut_function = ram_cut_function,
											heterogeneity = [6, 8], 
											dimension = u' Gb', step = 1, style = "width: 45%")

performanceCFilter = filters.ContainerFilter([performanceCpuFilter, performanceRamFilter])
performanceFilter = filters.TwoPartFilter('perf', cPart =  performanceCFilter, nPart =  performanceNFilter)

performanceFilter.set_parent_question(priceFilter)

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#Video:
def videoN_dss_function(selected_values):
	return {'vga' : int(selected_values[0])*1.5}
	

descriptionVideoN = 'video'
videoNFilter = filters.SliderSingleFilter('videoN', u'Видео:', 0, 5, 0,
									labels = [u'Нормальная', u'Очень высокая'], description = descriptionVideoN, dss_function = videoN_dss_function)


texts = u"Всё равно", u"GeForce GT3xx", u'GeForce GT4xx',u'GeForce GT5xx',u'GeForce GT6xx', u'GeForce GTX4xx',\
u'GeForce GTX5xx', u'GeForce GTX6xx' , u'Intel HD Graphics', u'nVidia ION', u'Quadro', u'Radeon HD 3xxx', u'Radeon HD 4xxx', u'Radeon HD 5xxx', u'Radeon HD 6xxx', u'Radeon HD 7xxx'
values = texts[:]

def videoC_cut_function(selected_values):
	if selected_values[0] == u"Всё равно":
		return ''
	for s in selected_values:
		s = s.replace('x','')	
		return 'vga_model LIKE "%' + s+ '%"'

videoSeriyaFilter  = filters.SelectFilter('videoSeriya', u'Серия видеокарты:', 
									texts, values, cut_function = videoC_cut_function)
videoFilter = filters.TwoPartFilter('video', cPart =  videoSeriyaFilter, nPart =  videoNFilter, defPart = 1, dtype = 'computer')

videoFilter.set_parent_question(performanceFilter)
#----------------------------------------------------------------------------------------------------------------------------------------------------------
#VideoNotebook:
def videoN_dss_function(selected_values):
	return {'vga' : int(selected_values[0])*1.5}
	

videoNFilterNotebook = filters.SliderSingleFilter('videoNoteN', u'Видео:', 0, 5, 0,
									labels = [u'Нормальная', u'Очень высокая'], description = descriptionVideoN, dss_function = videoN_dss_function)


texts = u"Всё равно", u"GeForce GT3xx", u'GeForce GT4xx',u'GeForce GT5xx',u'GeForce GT6xx', u'GeForce GTX4xx',\
u'GeForce GTX5xx', u'GeForce GTX6xx' , u'Intel GMA 4000',  u'Intel GMA 3000',  u'Intel GMA 2000', u'Quadro', u'Radeon HD 4xxx', u'Radeon HD 5xxx', u'Radeon HD 6xxx', u'Radeon HD 7xxx'
values = texts[:]

def videoC_cut_function(selected_values):
	if selected_values[0] == u"Всё равно":
		return ''
	if selected_values[0] == u'Quadro':
		return '(vga_model = "nVIDIA Quadro" OR vga_number LIKE "%NVS%")'
	if selected_values[0] == u'GeForce GT3xx':
		return '(vga_model = "nVIDIA GeForce" AND vga_number LIKE "%GT 3%")'
	if selected_values[0] == u'GeForce GT4xx':
		return '(vga_model = "nVIDIA GeForce" AND vga_number LIKE "%GT 4%")'
	if selected_values[0] == u'GeForce GT5xx':
		return '(vga_model = "nVIDIA GeForce" AND vga_number LIKE "%GT 5%")'
	if selected_values[0] == u'GeForce GT6xx':
		return '(vga_model = "nVIDIA GeForce" AND vga_number LIKE "%GT 6%")'
	if selected_values[0] == u'GeForce GTX4xx':
		return '(vga_model = "nVIDIA GeForce" AND vga_number LIKE "%GTX 4%")'
	if selected_values[0] == u'GeForce GTX5xx':
		return '(vga_model = "nVIDIA GeForce" AND vga_number LIKE "%GTX 5%")'
	if selected_values[0] == u'GeForce GTX6xx':
		return '(vga_model = "nVIDIA GeForce" AND vga_number LIKE "%GTX 6%")'		
	if selected_values[0] == u'Intel GMA 4000':
		return '(vga_model = "Intel GMA" AND vga_number = "HD 4000")'
	if selected_values[0] == u'Intel GMA 3000':
		return '(vga_model = "Intel GMA" AND vga_number = "HD 3000")'
	if selected_values[0] == u'Intel GMA 2000':
		return '(vga_model = "Intel GMA" AND vga_number = "HD 2000")'
	if selected_values[0] == u'Radeon HD 4xxx':
		return '(vga_model = "AMD Mobility Radeon" AND vga_number LIKE "%HD 4")'
	if selected_values[0] == u'Radeon HD 5xxx':
		return '(vga_model = "AMD Mobility Radeon" AND vga_number LIKE "%HD 5%")'
	if selected_values[0] == u'Radeon HD 6xxx':
		return '(vga_model = "AMD Mobility Radeon" AND vga_number LIKE "%HD 6%")'		
	if selected_values[0] == u'Radeon HD 7xxx':
		return '(vga_model = "AMD Mobility Radeon" AND vga_number LIKE "%HD 7%")'


videoSeriyaFilterNotebook  = filters.SelectFilter('videoNoteSeriya', u'Серия видеокарты:', 
									texts, values, cut_function = videoC_cut_function)
videoFilterNotebook = filters.TwoPartFilter('videoNote', cPart =  videoSeriyaFilterNotebook, nPart =  videoNFilterNotebook, defPart = 1, dtype = 'notebook')

videoFilterNotebook.set_parent_question(videoFilter)
#----------------------------------------------------------------------------------------------------------------------------------------------------------
#Display:

texts = [u'обязательно']
values = ['musthave']
def display_cut_function(selected_values):
	return 'display_diagonal IS NOT NULL'
def display_dss_function(selected_values):
	return {'display' : 2, 'vga' : 1}
displayCheckFilter = filters.CheckboxFilter('dispCheck', u'Встроенный дисплей', 
									texts, values, cut_function = display_cut_function, dss_function = display_dss_function)
def display_diagonal_cut_function(selected_values):
	return '(display_diagonal IS NULL OR (display_diagonal >= ' + selected_values[0].split(';')[0]  + ' AND ' + 'display_diagonal <= ' + selected_values[0].split(';')[1] + "))"
displayDiagonalFilter  = filters.SliderDoubleFilter('dispDiagonal', u'Диагональ экрана дисплея:',15, 27, [14, 24], 
											cut_function = display_diagonal_cut_function, 
											dimension = u' "', step = 1)
displayFilter = filters.ContainerFilter([displayCheckFilter, displayDiagonalFilter], 'disp', dtype = 'computer')

displayFilter.set_parent_question(videoFilterNotebook)
#----------------------------------------------------------------------------------------------------------------------------------------------------------
#DisplayNotebook:

texts = [u'всё равно',u'глянцевое',u'матовое']
values = ['all', 'glyancevoe','matovoe']
def display_cover_cut_function(selected_values):
	if selected_values[0] == 'all': return ''
	if selected_values[0] == 'glyancevoe': return 'display_cover LIKE "%' + u'глянцевое'+ '%"'
	if selected_values[0] == 'matovoe': return 'display_cover LIKE "%' + u'матовое' + '%"'
	return ''

displayCoverFilter = filters.RadioFilter('dispNoteCover', u'Покрытие дисплея', 
									texts, values, cut_function = display_cover_cut_function)

texts = u'всё равно', u'TN+Film', u'IPS'
values =  'all', 'TN+Film', 'IPS'
def matrix_cut_function(selected_values):
	if 'all' in selected_values: return ""
	if 'TN+Film' in selected_values : return"'display_matrix = 'TN+Film'"
	if 'IPS' in selected_values : return"display_matrix = 'IPS'"		
	if len(filters) > 1: return ' AND '.join(filters)
	return ''
displayMatrixFilter = filters.RadioFilter('dispNoteMatrix', u'Тип матрицы:', 
									texts, values, cut_function = matrix_cut_function, style = "width: 20%")

def display_diagonal_cut_function(selected_values):
	return '(display_diagonal IS NULL OR (display_diagonal >= ' + selected_values[0].split(';')[0]  + ' AND ' + 'display_diagonal <= ' + selected_values[0].split(';')[1] + "))"
displayDiagonalFilterNotebook  = filters.SliderDoubleFilter('dispDiagonalNote', u'Диагональ экрана дисплея:',7, 18, [11, 18], 
											cut_function = display_diagonal_cut_function, 
											dimension = u' "', step = 1, dtype = 'notebook')

texts = [u'обязательно']
values = ['musthave']
def display_sensor_cut_function(selected_values):
	return u"display_sensor IS NOT NULL"

displaySensorFilter = filters.CheckboxFilter('dispNoteSensor', u'Сенсорный экран', 
									texts, values, cut_function = display_sensor_cut_function )

displayFilterNotebook = filters.ContainerFilter([displayCoverFilter, displayMatrixFilter, displaySensorFilter], 'dispNote', dtype = 'notebook')


displayDiagonalFilterNotebook.set_parent_question(displayFilter)
displayFilterNotebook.set_parent_question(displayDiagonalFilterNotebook)
#----------------------------------------------------------------------------------------------------------------------------------------------------------
#Hdd:


def hdd_diagonal_cut_function(selected_values):
	return 'hdd_clear_capacity >= ' + selected_values[0].split(';')[0]  + ' AND ' + 'hdd_clear_capacity <= ' + selected_values[0].split(';')[1]
hddFilter  = filters.SliderDoubleFilter('hdd', u'Объем памяти:',50, 2000, [100, 2000],
											dimension = u' Gb', step = 50, cut_function = hdd_diagonal_cut_function)

hddFilter.set_parent_question(displayFilterNotebook)

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#Battery + Weight:


def battery_dss_function(selected_values):
	return {'battery' : int(selected_values[0])}	
descriptionBatteryN = 'battery'
batteryFilter = filters.SliderSingleFilter('compactbattery', u'Батарея:', 0, 5, 0,
									labels = [u'Обычная', u'Максимальная автономность'], description = descriptionBatteryN,
									 dss_function = battery_dss_function, style = "width: 40%")



def weight_dss_function(selected_values):
	return {'weight' : -int(selected_values[0])*1.6}	
descriptionWeight = "weight"
weightFilter = filters.SliderSingleFilter('compactWeight', u'Вес', 0, 5, 2,
									labels = [u'Не имеет значения', u'Максимально легкий'], description = descriptionWeight, 
									dss_function = weight_dss_function, style = "width: 40%")

compactnessFilter = filters.ContainerFilter([batteryFilter, weightFilter], 'compact', dtype = 'notebook')

compactnessFilter.set_parent_question(hddFilter)
#----------------------------------------------------------------------------------------------------------------------------------------------------------
#os:

def os_cut_function(selected_values):
	filters = []	
	for s in selected_values:
		filters.append('os LIKE "%' + s + '%"')
	if len(filters) > 1: return '(' + ' OR '.join(filters) + ')'
	return filters[0] if filters else ''

texts = 'Windows', 'Mac',  "Linux"
values =  'Windows', 'Mac', 'Linux'

osFilter = filters.CheckboxFilter('osFilter', u'Обязательно с ОС:', 
									texts, values, type = "inline", cut_function = os_cut_function)

osFilter.set_parent_question(compactnessFilter)


#----------------------------------------------------------------------------------------------------------------------------------------------------------
#color:

def color_cut_function(selected_values):
	if selected_values[0] == u"Всё равно":
		return ''
	if selected_values[0] == u'другие яркие цвета': 
		other_colors = u'синий', u'красный' , u'розовый',  u'золотистый', u"бордовый", u"оранжевый", u"фиолетовый"
		filters = []
		for s in other_colors:
			filters.append('color LIKE "%' + s + '%"')
		return '(' + ' OR '.join(filters) + ')'
	return 'color LIKE "%' + selected_values[0] + '%"'
	

texts = u"Всё равно", u"чёрный", u'серебристый', u'серый', u'коричневый', u'белый', u'другие яркие цвета'
values = texts[:]

colorFilter = filters.SelectFilter('colorFilter', u'Цвет:', 
									texts, values, cut_function = color_cut_function, dtype = 'notebook')

colorFilter.set_parent_question(osFilter)

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#Web camera:

def web_camera_dss_function(selected_values):
	return {'web_camera' : int(selected_values[0])}	

def web_camera_cut_function(selected_values):
	if int(selected_values[0]) > 0: return 'web_camera LIKE "%' + u'МПикс'+ '%"'
	return ""

webCameraFilter = filters.SliderSingleFilter('webCamera', u'Веб камера:', 0, 3, 0,
									labels = [u'Всё равно', u'Максимально лучшая'],cut_function = web_camera_cut_function,
									 dss_function = web_camera_dss_function, scale = '[0, 1, 2, 3]', style = "width: 40%", dtype = 'notebook')

webCameraFilter.set_parent_question(colorFilter)

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#Required Parameters:
texts = u"BluRay", u"Wi-Fi", u'Bluetooth',u'USB 3.0', u'картридер', u'веб камера', u'ТВ-тюнер',u'пульт ДУ'
values =  'bluray', 'wifi', 'bluetooth','usb3', 'cardreader', 'media_web_camera', 'media_tv_tunner', 'remote'
def required_parameters_cut_function(selected_values):
	filters = []
	for s in selected_values:
		if s == 'wifi': filters.append('network LIKE "%' + 'Wi-Fi'+ '%"')
		if s == 'bluray': filters.append('panel_drive LIKE "%' + 'BluRay'+ '%"')
		if s == 'bluetooth': filters.append('network LIKE "%' + 'Bluetooth' + '%"')
		if s == 'usb3': filters.append('panel_usb3 IS NOT NULL')
		if s == 'cardreader': filters.append('panel_cardreader = 1')
		if s == 'media_tv_tunner': filters.append('media_tv_tunner = 1')
		if s == 'media_web_camera': filters.append('media_web_camera = 1')
		if s == 'remote': filters.append('media_remote = 1')
	if len(filters) > 1: return ' AND '.join(filters)
	return filters[0] if filters else '' 
required_parameters = filters.CheckboxFilter('rpComp', u'Я хочу чтоб обязательно был:', 
									texts, values, type = "table", cut_function = required_parameters_cut_function)

texts = u'всё равно', u'звук 5.1', u'звук 7.1'
values =  'all', 'media_sound_5', 'media_sound_7'
def audio_cut_function(selected_values):
	if 'all' in selected_values: return ""
	if 'media_sound_5' in selected_values : return'media_sound = 5.1'
	if 'media_sound_7' in selected_values : return'media_sound = 7.1'		
	if len(filters) > 1: return ' AND '.join(filters)
	return ''

audioFilter = filters.RadioFilter('audio', u'Аудио:', 
									texts, values, cut_function = audio_cut_function)

commonFilter = filters.ContainerFilter([required_parameters, audioFilter], 'common', dtype = 'computer')

commonFilter.set_parent_question(webCameraFilter)

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#Required Parameters Notebook: 
texts = u"BluRay", u"LAN", u'Bluetooth', u'USB 3.0', u'Thunderbolt', u'кардридер', u'GPS-модуль', u'Wi-Fi стандарта 802.11n', u'подсветка клавиатуры', u'доп. вход для наушников', u'подключение к док-станции', u'влагозащищенный корпус'
values =  'bluray', 'lan',  'bluetooth','usb3', 'thunderbolt','cardreader','gps', 'wifi', 'keyboardBacklight','additionalHeadphones', 'docStation', 'waterproof'
def required_parameters_note_cut_function(selected_values):
	filters = []
	for s in selected_values:
		if s == 'wifi': filters.append('com_wifi LIKE "%' + '802.11n'+ '%"')
		if s == 'bluray': filters.append('panel_bluraydrive IS NOT NULL')
		if s == 'bluetooth': filters.append('com_bluetooth IS NOT NULL')
		if s == 'usb3': filters.append('panel_usb3 IS NOT NULL')
		if s == 'cardreader': filters.append('multimedia LIKE "%' + u'Картридер' + '%"')
		if s == 'lan': filters.append('lan LIKE "%' + u'10/100' + '%"')
		if s == 'gps': filters.append('multimedia LIKE "%' + u'GPS-модуль' + '%"')
		if s == 'thunderbolt': filters.append('thunderbolt IS NOT NULL')
		if s == 'keyboardBacklight': filters.append('input_keyboard_backlight LIKE "%' + '+' + '%"')
		if s == 'additionalHeadphones': filters.append('additional_headphones_port IS NOT NULL')
		if s == 'docStation': filters.append('doc_station_connection IS NOT NULL')
		if s == 'waterproof': filters.append('waterproof IS NOT NULL')
		
	if len(filters) > 1: return ' AND '.join(filters)
	return filters[0] if filters else '' 
required_parameters_notebook = filters.CheckboxFilter('rpNote', u'Я хочу чтоб обязательно был:', 
									texts, values, type = "table", cut_function = required_parameters_note_cut_function, dtype = 'notebook')
required_parameters_notebook.set_parent_question(commonFilter)

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------

FILTERS = priceFilter, performanceFilter, videoFilter, displayFilter, hddFilter, osFilter, commonFilter, webCameraFilter, \
videoFilterNotebook, displayDiagonalFilterNotebook, displayFilterNotebook, compactnessFilter, required_parameters_notebook, colorFilter

def init_comp_filters(filters):
	rez = []
	for filter in filters:
		if filter.dtype == None or filter.dtype == 'computer':
			rez.append(filter)
	return rez
def init_notebook_filters(filters):
	rez = []
	for filter in filters:
		if filter.dtype == None or filter.dtype == 'notebook':
			rez.append(filter)
	return rez
def init_all_filters(filters):
	rez = []
	parent_filter = None
	for filter in filters:
		if filter.parent_question == None:
			parent_filter = filter	
	has_children = True
	while has_children:
		rez.append(parent_filter)
		has_children = False
		for filter in filters:
			if filter.parent_question:
				if filter.parent_question.name == parent_filter.name:
					parent_filter = filter
					has_children = True
					break

	return rez

COMP_FILTERS = init_comp_filters(FILTERS)
NOTEBOOK_FILTERS = init_notebook_filters(FILTERS)	
ALL_FILTERS = init_all_filters(FILTERS)
