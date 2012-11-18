#coding: utf-8
'''
Created on Sep 30, 2012

@author: Pavel

This class describes all filters for answers. Every filter has to realise class filters.Filter or its implementation.
For more details look filters.py 
'''
from sqlorm import wc_Computer
from dss import DSS_WEIGHTS
import filters

#example of checkbox filter: all yes/no parameters
def yesno_cut_function(selected_values):
	'''
	First we define cut function: it gets all selected values and creates 'where' string 
	'''
	filters = []
	for s in selected_values:
		filters.append('wc_Computer.' + s + ' > 0')
	if len(filters) > 1: return ' AND '.join(filters)# if where are more then one filter, join filters  by 'AND'
	return filters[0] if filters else ''#if there is no filters returns empty string, if one filter - returns it without 'AND'

'''
Secondly we define filter values
'''
#what we show to user:
texts = u"Цена > 0", u'wifi', u'Bluetooth', u'картридер', u'модем 56', u'вебкамера', u'3G', u'wimax', u'сетевой адаптер'
#what we get to function:
values =  'price', 'wifi', 'Bluetooth', 'cardreader', 'modem56', 'webcamera', 'G3', 'wimax', 'network_adapter'
#what is selected at the first time:
selected_values = ('price',)

'''
At last we define filter: (description: u'Дополнительные параметры:', name:'yesnoFilter')
''' 
yesnoFilter = filters.CheckboxFilter(u'Дополнительные параметры:', 'yesnoFilter',
										texts, values, selected_values, cut_function = yesno_cut_function)

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#Other example of checkbox filter(filter for os):
def os_cut_function(selected_values):
	filters = []
	for s in selected_values:
		filters.append('wc_Computer.os LIKE "' + s + '"')
	if len(filters) > 1: return '(' + ' OR '.join(filters) + ')'
	return filters[0] if filters else ''

texts = "Linux", 'Mac', 'Windows', 
values =  'linux', 'mac', 'windows'
selected_values = 'linux', 'mac', 'windows'

osFilter = filters.CheckboxFilter(u'Операционная система:', 'osFilter',
									texts, values, selected_values, cut_function = os_cut_function)

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#Example of slider filter(filter for min ram amount):
def ram_dss_function(selected_values):
	'''
	if user set this filter higher we increase dss value of ram 
	'''
	pass

def ram_cut_function(selected_value):
	print selected_value
	pass

min_value, max_value = 2, 8
start_value = 2

ramFilter = filters.SliderFilter(u'Объем оперативной памяти:', 'ramFilter',
									min_value, max_value, start_value,
									dss_function = ram_dss_function, cut_function = ram_cut_function)

#all filters to use at page:
ALL_FILTERS = typeFilter, yesnoFilter, osFilter, oddFilter