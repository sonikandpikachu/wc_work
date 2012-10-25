#coding: utf-8
'''
Created on Sep 30, 2012

@author: Pavel
'''

DSS_WEIGHTS = {'cpu' : 1, 'ram' : 0.8, 'vga' : 0.9, 
 	 'battery' : 0.5, 'hd' : 0.7, 'odd' : 0.1, 'os' : 0.2}

DSS_COMPWEIGHTS = {'norm_price' : -6, 'weight' : -0.3, 'webcamera' : 0.05, 'Bluetooth' : 0.05, 'wifi' : 0.4}

def get_dss_weight (components):
	weight = 0
	for w in DSS_WEIGHTS:
		if components[w]:
			if components[w].dss: weight += DSS_WEIGHTS[w]*components[w].dss
	print weight
	for w in DSS_COMPWEIGHTS:
		if w in components['comp'].__dict__:
			if components['comp'].__dict__[w]: weight += components['comp'].__dict__[w] * DSS_COMPWEIGHTS[w]
	print weight
	return weight


