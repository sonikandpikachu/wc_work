#coding: utf-8
'''
Created on Sep 30, 2012

@author: Pavel

This module contains all types of filters. For realisation examples see settings.py,
html macroses for this filters situated in templates/filters.html
'''



class Filter(object):
	'''
	Abstract class for all types of filters
	Parameters: 
				ftype - deffines filters type for html macros. Usually this parameters defined in subclasses
				name - unique name of filter
				question - filter description
				cut_function - function, which returns string. This string will be in 'where' part of query
				dss_function - function, which returns dict. Key of dict is name of dss parameter,
					value of dict - new value of dss parameter

				cut_function and dss_function gets selected values as input parameters

				For examples see settings.py 
	'''
	def __init__(self, ftype, name, description, cut_function = None, dss_function = None):
		self.ftype = ftype
		self.cut_function = cut_function
		self.dss_function = dss_function
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
		self.slider_min, self.slider_max = slider_min, slider_max  
		self.start_value = start_value
 	

 	



