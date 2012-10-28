#coding: utf-8
'''
Created on Sep 30, 2012

@author: Pavel

This class describes all filters for answers. Every filter has to realise class filters.Filter or its implementation.
For more details look filters.py 
'''
from sqlorm import wc_Type, wc_OS, wc_CPU

from dss import DSS_WEIGHTS
import filters

#adding checkbox filter for computer type:
def type_cut_function(selected_values):
	if 'notebook' and 'desctop' in selected_values: return ''
	if 'notebook' in selected_values: return 'wc_Type.id < 4'
	if 'desctop' in selected_values: return 'wc_Type.id > 3'
	return '1 = 2'

typeFilter = filters.CheckboxFilter(u'Какой тип компьютера Вы хотите?',
										 'typeFilter', cut_function = type_cut_function)
typeFilter.texts = u"Ноутбук", u'Компьютер'
typeFilter.values =  "notebook", 'desctop'
typeFilter.selected_values = "notebook", 'desctop'

#adding checkbox filter for computer type:

def yesno_cut_function(selected_values):
	filters = []
	for s in selected_values:
		filters.append('wc_Computer.' + s + ' > 0')
	if len(filters) > 1: return ' AND '.join(filters)
	return filters[0] if filters else ''

yesnoFilter = filters.CheckboxFilter(u'Дополнительные параметры:',
										 'yesnoFilter', cut_function = yesno_cut_function)
yesnoFilter.texts = u"Цена > 0", u'wifi', u'Bluetooth', u'картридер', u'модем 56', u'вебкамера', u'3G', u'wimax', u'сетевой адаптер'
yesnoFilter.values =  'price', 'wifi', 'Bluetooth', 'cardreader', 'modem56', 'webcamera', 'G3', 'wimax', 'network_adapter'
yesnoFilter.selected_values = 'price'


def os_cut_function(selected_values):
	filters = []
	for s in selected_values:
		filters.append('wc_OS.type = "' + s + '"')
	if len(filters) > 1: return '(' + ' OR '.join(filters) + ')'
	return filters[0] if filters else ''

osFilter = filters.CheckboxFilter(u'Операционная система:',
										 'osFilter', cut_function = os_cut_function)
osFilter.texts = u"Linux", u'Mac', u'Windows'
osFilter.values =  'l', 'm', 'w'
osFilter.selected_values = 'l', 'm', 'w'


def odd_cut_function(selected_values):
	filters = []
	for s in selected_values:
		filters += ['wc_ODD.type = "' + t + '"' for t in s.split(',')]
	if len(filters) > 1: return ' OR '.join(filters)
	return filters[0] if filters else ''

oddFilter = filters.CheckboxFilter(u'Дисковод:',
										 'oddFilter', cut_function = odd_cut_function)
oddFilter.texts = u"DWD", u'Blueray', u'Blueray RW'
oddFilter.values =  'dwd', 'b1,b2', 'b3'
oddFilter.selected_values = 'dwd', 'b1,b2', 'b3'




# #adding radio filter for OS:
# def os_cut_function(selected_values):
# 	return [computer for computer in computers
# 		if session.query(wc_OS).filter_by(id = computer.id_wc_OS).first().name in answer ]

# osFilter = filters.CheckboxFilter(u'Какую ос вы предпочитаете?',
# 										 'osFilter', cut_function = os_cut_function, selected = 1)
# osFilter.texts = "DOS", "Mac OS x 10.7 Lion", 'Linux'
# osFilter.values =  u"DOS", u"Mac OS x 10.7 Lion", u'Linux'


# #adding slider filter for cpu frequency:
# def cpu_frequency_cut_function(session, computer_components, answer):
# 	cpuFrequencyFilter.value = answer
# 	return [computer for computer in computers
# 		if session.query(wc_CPU).filter_by(id = computer.id_wc_CPU).first().frequency >= float(answer)] 

# cpuFrequencyFilter = filters.SliderFilter('Please input frequency', 'cpuFrequencyFilter', value = '1.7',
# 					 cut_function = cpu_frequency_cut_function)

# cpuFrequencyFilter.slider_max = '3.2'
# cpuFrequencyFilter.slider_min = '0'


# #adding radio filter for kernel count
# def cpu_dss_function(answer):
# 	cpuFilter.selected = cpuFilter.values.index(answer)
# 	DSS_WEIGHTS['cpu'] = 2 if answer == u"Да" else 0
	
# cpuFilter = filters.CheckboxFilter(u'Будете ли Вы производить сложные вычисления?',
# 										 'cpuFilter', dss_function = cpu_dss_function, selected = 1)
# cpuFilter.texts = u"Да", u"Нет"
# cpuFilter.values =  u"yes", u"no"


#all filters to use at page:
ALL_FILTERS = typeFilter, yesnoFilter, osFilter, oddFilter