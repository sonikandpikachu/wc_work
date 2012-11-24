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
				title - question title
				description - question description (available like tooltip)
				question - filter title
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
	def __init__(self, ftype, name = "", title = "", style = "", description = None, cut_function = None,
	    dss_function = None):
		self.ftype = ftype
		self.cut_function = cut_function
		self.dss_function = dss_function
		self.title = title
		self.description = description
		self.name = name
		self.style = style

class ContainerFilter(Filter):
	"""Container for multifilter question"""

	def __init__(self, children):
		super(ContainerFilter, self).__init__('container')
		self.children = children

class TwoPartFilter(Filter):
	"""
	TwoPart question

	cPart - left
	nPart - right

	"""

	def __init__(self, name, cPart, nPart, defPart = 0):
		super(TwoPartFilter, self).__init__('twoPart', name)
		self.cPart = cPart
		self.nPart = nPart
		self.defPart = defPart			
		

class RadioFilter(Filter):
	'''
	Filter for radiobuttons. 
	Parameters:
		name, cut_function, dss_function - look class Filter
		values - list or tuple of values which will be in html input 'values'. 
		texts - list or tuple of text near checkbox(user see this text)
		selected_value - list of selected values
	'''
	
	def __init__(self, name, title, texts, values, selected_value = 0, description = None, style = "", type = "rows", cut_function = None, dss_function = None):
		super(RadioFilter, self).__init__('radio', name, title, style, description, cut_function, dss_function)
		self.texts = texts
		self.values = values
		self.selected_value = selected_value
		self.type = type	

class CheckboxFilter(Filter):
	'''
	Filter for checkboxes. 
	Parameters:
		name, cut_function, dss_function - look class Filter
		values - list or tuple of values which will be in html input 'values'. 
		texts - list or tuple of text near checkbox(user see this text)
		selected_values - list of selected values
	'''
	
	def __init__(self, name, title, texts, values, selected_values = None, description = None, style = "", type = "rows", cut_function = None, dss_function = None):
		super(CheckboxFilter, self).__init__('checkbox', name, title, style, description, cut_function, dss_function)
		self.texts = texts
		self.values = values
		self.selected_values = selected_values
		self.type = type

class SelectFilter(Filter):
	'''
	Filter for select. (Default - select first value) 
	Parameters:
		name, cut_function, dss_function - look class Filter
		values - list or tuple of values which will be in html input 'values'. 
		texts - list or tuple of text near checkbox(user see this text)
		selected_values - list of selected values
	'''
	
	def __init__(self, name, title, texts, values, description = None, style = "", cut_function = None, dss_function = None):
		super(SelectFilter, self).__init__('select', name, title, style, description, cut_function, dss_function)
		self.texts = texts
		self.values = values	

class SliderDoubleFilter(Filter):
	'''
	Filter for double slider with heterogeneity (nonlinear scale)
	Parameters:
		name, cut_function, dss_function - look class Filter
		min_value, max_value - minimum and maximum on the scale
		start_values- initial values

	'''

	def __init__(self, name, title, min_value, max_value, start_values, 
		description = None, style = "", cut_function = None, dss_function = None, 
		heterogeneity = False, dimension = ' ', step = 1):
		super(SliderDoubleFilter, self).__init__('sliderDouble', name, title, style, description, cut_function, dss_function)
		self.min_value, self.max_value = min_value, max_value  
		self.start_values = start_values
		self.heterogeneity = heterogeneity
		self.dimension = dimension
		self.step = step	

class SliderSingleFilter(Filter):
	'''
	Filter for single slider with ruled scale and labels
	Parameters:
		name, cut_function, dss_function - look class Filter
		min_value, max_value - minimum and maximum on the scale
		start_value - initial value
	'''

	def __init__(self, name, title, min_value, max_value, start_value, 
		labels = None, description = None, style = "", cut_function = None, 
		dss_function = None, scale = '[0, 1, 2, 3, 4, 5]', dimension = ' ', step = 1):
		super(SliderSingleFilter, self).__init__('sliderSingle', name, title, style, description, cut_function, dss_function)
		self.min_value, self.max_value = min_value, max_value  
		self.start_value = start_value
		self.scale = scale
		self.dimension = dimension
		self.step = step
		self.labels = labels			



