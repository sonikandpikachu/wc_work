#coding: utf-8
'''
Created on Sep 30, 2012

@author: Pavel

This module contains all types of filters. For realisation examples see settings.py,
html macroses for this filters situated in templates/filters.html

TODO: make check selected parameters function in filters.
'''



class Filter(object):
	'''
	Abstract class for all types of filters
	Parameters: 
				ftype - deffines filters type for html macros. Usually this parameters defined in subclasses
				name - unique name of filter
				question - filter description
				cut_function - function, returns string.
				dss_function - function, returns dict.

				cut_function and dss_function gets selected values as input parameters
				
				cut_function have to return 'WHERE' part of query to wc_Computer table. All of returned 
				strings will be joined by 'AND'
				
				dss_functin have to return dictionary, where keys are columns from wc_DSS table and values
				are weights for this columns

				Notice: dss_function always have to return dictionary, if there is no changes it has to 
				return empty dictionary, not None. Analogically cut_function has to return empty string

				For examples see settings.py 
	'''
	def __init__(self, ftype, name, description, cut_function = None, dss_function = None):
		self.ftype = ftype
		self.cut_function = cut_function
		self.dss_function = dss_function
		self.description = description
		self.name = name


class CheckboxFilter(Filter):
	'''
	Filter for checkboxes. 
	Parameters:
		name, cut_function, dss_function - look class Filter
		values - list or tuple of values which will be in html input 'values'. 
		texts - list or tuple of text near checkbox(user see this text)
		selected_values - list of selected values
	'''
	
	def __init__(self, name, description, texts, values, selected_values, cut_function = None, dss_function = None):
		super(CheckboxFilter, self).__init__('checkbox', name, description, cut_function, dss_function)
		self.texts = texts
		self.values = values
		self.selected_values = selected_values


class SliderFilter(Filter):
	'''
	Filter for slider
	Parameters:
		name, cut_function, dss_function - look class Filter
		min_value, max_value - minimum and maximum on the scale
		start_value - initial value
	'''

	def __init__(self, name, description, min_value, max_value, start_value, cut_function = None, dss_function = None):
		super(SliderFilter, self).__init__('slider', name, description, cut_function, dss_function)
		self.min_value, self.max_value = min_value, max_value  
		self.start_value = start_value
 	

 	



