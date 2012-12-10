#coding: utf-8
'''
Created on Sep 30, 2012

@author: Pavel

This class describes all filters for answers. Every filter has to realise class filters.Filter or its implementation.
For more details look filters.py 
'''
from sqlorm import wc_Computer
from wcconfig import db
from dss import DSS_WEIGHTS
import filters

#example of checkbox filter: all yes/no parameters
def yesno_cut_function(selected_values):
	'''
	First we define cut function: it gets all selected values and creates 'where' string 
	'''
	filters = []
	for s in selected_values:
		filters.append(s + ' > 0')
	if len(filters) > 1: return ' AND '.join(filters)# if where are more then one filter, join filters  by 'AND'
	return filters[0] if filters else ''#if there is no filters returns empty string, if one filter - returns it without 'AND'

'''
Secondly we define filter values
'''
#what we show to user:
texts = u"Встроеные динамики", u'ВЕБ-камера', u'Микрофон', u'картридер'
#what we get to function:
values =  'media_builtin_dinamics', 'media_web_camera', 'media_microphone', 'panel_cardreader'
#what is selected at the first time:
selected_values = tuple()

'''
At last we define filter: (description: u'Дополнительные параметры:', name:'yesnoFilter')
''' 
yesnoFilter = filters.CheckboxFilter('yesnoFilter', u'Дополнительные параметры:',
										texts, values, selected_values, cut_function = yesno_cut_function)

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#Other example of checkbox filter(filter for os):
def os_cut_function(selected_values):
	filters = []
	for s in selected_values:
		filters.append('os LIKE "%' + s + '%"')
	if len(filters) > 1: return '(' + ' OR '.join(filters) + ')'
	return filters[0] if filters else ''

texts = "Linux", 'Mac', 'Windows', 
values =  'linux', 'mac', 'windows'
selected_values = 'linux', 'mac', 'windows'

osFilter = filters.CheckboxFilter('osFilter', u'Операционная система:', 
									texts, values, selected_values, cut_function = os_cut_function)

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#Example of slider filter(filter for min ram amount):
def ram_dss_function(selected_values):
	'''if user set this filter higher we increase dss value of ram '''
	return {'ram' : 20 * int(selected_values[0])}

def ram_cut_function(selected_values):
	return 'ram_amount > ' + selected_values[0]


descriptionPerformanceN = u'<p style = "text-indent: 10px;">Значение определяет на сколько увеличиться важность видеокарты </br>\
в подбираемой модели в ущерб остальным параметрам</p>'

moneyCFilter = filters.SliderDoubleFilter('moneyCFilter', u'Цена:',
									1000, 50000, [4000, 10000],
									dss_function = ram_dss_function, cut_function = ram_cut_function, 
									heterogeneity = [10000, 20000], dimension = u' грн', step = 50)

performanceNFilter = filters.SliderSingleFilter('performanceNFilter', u'Производительность:', 1, 5, 1,
									labels = [u'Нормальная', u'Очень высокая'], description = descriptionPerformanceN, 
									style = "width: 80%", dss_function = ram_dss_function, cut_function = ram_cut_function)
performanceNFilter1 = filters.SliderSingleFilter('performanceNFilter1', u'Производительность:', 1, 5, 1,
									labels = [u'Нормальная', u'Очень высокая'], description = descriptionPerformanceN, 
									style = "width: 80%", dss_function = ram_dss_function, cut_function = ram_cut_function)
texts = "Linux", 'Mac', 'Windows', 
values =  'linux', 'mac', 'windows'
selected_values = 1, 2

osFilterC = filters.CheckboxFilter('osFilterC', u'Операционная система:', 
									texts, values, selected_values, description = descriptionPerformanceN,
									cut_function = os_cut_function)
osFilterR = filters.RadioFilter('osFilterR', u'Операционная система:', 
									texts, values, cut_function = os_cut_function)
osFilterS = filters.SelectFilter('osFilterS', u'Операционная система:', 
									texts, values, description = descriptionPerformanceN,
									cut_function = os_cut_function)

containerTestFilter = filters.ContainerFilter([osFilterS, moneyCFilter])
TwoPartTestFilter = filters.TwoPartFilter('TwoPartTest', cPart =  containerTestFilter, nPart =  performanceNFilter1)

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#Type:
texts = u"Компьютер", u'Ноутбук', u'Планшет', u'еще не знаю'
values =  'computer', 'notebook', 'tablet', "all"
def type_cut_function(selected_values):		
	acceptTypes = []
	for s in selected_values:
		if s == 'computer' : acceptTypes.extend([u"неттоп", u"моноблок", u"игровой", u"настольный" , u"настольный / с монитором /"])
		if s == 'notebook': acceptTypes.extend([u"ноутбук", u"нетбук", u"ультрабук", u"трансформер"])
		if s == 'tablet': acceptTypes.extend([u"ноутбук"])
		if s == 'all': acceptTypes.extend([u"неттоп", u"моноблок", u"игровой", u"настольный" , u"настольный / с монитором /", u"ноутбук", \
									u"нетбук", u"ультрабук", u"трансформер"])
	filters = []	
	for aT in acceptTypes:		 
			filters.append('type LIKE "%' + aT + '%"')
	if len(filters) > 1: return '(' + ' OR '.join(filters) + ')'	
	return filters[0] if filters else '' 
deviceType = filters.RadioFilter('type', u'Я хочу ...', 
									texts, values, selected_value = 3,cut_function = type_cut_function)


#----------------------------------------------------------------------------------------------------------------------------------------------------------
#Price:

def priceC_cut_function(selected_values):
	return 'price > ' + selected_values[0].split(';')[0]  + ' AND ' + 'price < ' + selected_values[0].split(';')[1]
priceCFilter = filters.SliderDoubleFilter('priceC', u'Цена:',1000, 50000, [4000, 10000], style = "width: 80%",
											cut_function = priceC_cut_function, heterogeneity = [10000, 20000], 
											dimension = u' грн', step = 50)

def priceN_dss_function(selected_values):
	return {'price' : int(selected_values[0])}
# def priceN_cut_function(selected_values):
# 	'''!!!!!!!!!!!!!!!!!!Menya netu!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! '''
# 	return {'price' : int(selected_values[0])}

priceDescription = u'<p style = "text-indent: 10px;">Значение определяет на сколько увеличиться важность цены </br>\
в подбираемой модели в ущерб остальным параметрам. </br>  В точке 0 &mdash; &Prime;разумная цена&Prime;</p>'
priceNFilter = filters.SliderSingleFilter('priceN', u'Важность цены:', -3, 3, 0, scale = '[-3,-2,-1, 0, 1, 2, 3]',
									labels = [u'Не имеет значения', u'Максимальная економия'], description = priceDescription, 
									dss_function = priceN_dss_function)

priceFilter = filters.TwoPartFilter('price', cPart =  priceCFilter, nPart =  priceNFilter)

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#Performance:
def performanceN_dss_function(selected_values):
	print 'selected_values', selected_values
	return {'cpu' : int(selected_values[0])*1.5,'ram' : int(selected_values[0])}
# def performanceN_cut_function(selected_values):
# 	'''!!!!!!!!!!!!!!!!!!Menya netu!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! '''
# 	return {'price' : int(selected_values[0])}

descriptionPerformanceN = u'<p style = "text-indent: 10px;">Значение определяет на сколько увеличиться важность производительности </br>\
в подбираемой модели в ущерб остальным параметрам</p>'
performanceNFilter = filters.SliderSingleFilter('performanceN', u'Производительность:', 0, 5, 0,
									labels = [u'Нормальная', u'Очень высокая'], description = descriptionPerformanceN, dss_function = performanceN_dss_function)


texts = [comp.cpu_name for comp in db.session.query(wc_Computer).group_by(wc_Computer.cpu_name)]
values = texts[:]
performanceSeriyaFilter  = filters.SelectFilter('performanceSeriya', u'Процессор:', 
									texts, values)

def performanceC_cut_function(selected_values):
	print 'performance', selected_values[0]
	return 'cpu_frequency > ' + selected_values[0].split(';')[0]  + ' AND ' + 'cpu_frequency < ' + selected_values[0].split(';')[1]
performanceFreqFilter = filters.SliderDoubleFilter('performanceFreq', u'Частота процессора:',1, 4, [2, 3], 
											cut_function = performanceC_cut_function, 
											dimension = u' ГГц', step = 0.1)

performanceCFilter = filters.ContainerFilter([performanceSeriyaFilter, performanceFreqFilter])

performanceFilter = filters.TwoPartFilter('performance', cPart =  performanceCFilter, nPart =  performanceNFilter, defPart = 1)


#----------------------------------------------------------------------------------------------------------------------------------------------------------
#Required Parameters:
texts = u"Wi-Fi", u'Bluetooth', u'кардридер', u'ТВ-тюнер', u'звук 5.1', u'звук 7.1'
values =  'wifi', 'bluetooth', 'media_web_camera', 'media_tv_tunner', 'media_sound_5', 'media_sound_7'
def required_parameters_cut_function(selected_values):
	filters = []
	for s in selected_values:
		if s == 'media_sound_5': filters.append('media_sound = 5.1')
		if s == 'media_sound_7': filters.append('media_sound = 7.1')
		if s == 'wifi': filters.append('network LIKE "%' + 'Wi-Fi'+ '%"')
		if s == 'bluetooth': filters.append('network LIKE "%' + 'Bluetooth' + '%"')
		if s == 'media_tv_tunner': filters.append('media_tv_tunner = 1')
		if s == 'media_web_camera': filters.append('media_web_camera = 1')
	if len(filters) > 1: return ' AND '.join(filters)
	return filters[0] if filters else '' 
required_parameters = filters.CheckboxFilter('required_parameters', u'Я хочу чтоб обязательно был:', 
									texts, values, type = "table", selected_values = [0, 1, 2], cut_function = required_parameters_cut_function)


#----------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------

#all filters to use at page:
#ALL_FILTERS = TwoPartTestFilter, performanceNFilter, osFilterC, osFilterR, required_parameters
ALL_FILTERS = deviceType, priceFilter, performanceFilter, required_parameters