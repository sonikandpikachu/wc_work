#coding: utf-8
'''
Created on Sep 30, 2012

@author: Pavel
This module works with dss weights and values.  
'''

DSS_WEIGHTS = {'CPU' : 1, 'RAM' : 0.8, 'VGA' : 0.9, 
 	 'Battery' : 0.5, 'HD' : 0.7, 'ODD' : 0.1, 'OS' : 0.2}

DSS_COMPWEIGHTS = {'norm_price' : -3, 'weight' : -0.3, 'webcamera' : 0.05, 'Bluetooth' : 0.05, 'wifi' : 0.4}

def dss_weight (computer):
	'''
	gets sqlorm.wc_Computer and returns dss weight for this computer
	'''
	weight = 0
	for w in (w for w in DSS_WEIGHTS if w in computer.__dict__):
		if computer.__dict__[w].dss: weight += DSS_WEIGHTS[w]*computer.__dict__[w].dss
	return weight
	# print weight
	# for w in DSS_COMPWEIGHTS:
	# 	if w in components['comp'].__dict__:
	# 		if components['comp'].__dict__[w]: weight += components['comp'].__dict__[w] * DSS_COMPWEIGHTS[w]
	# print weight
	# return weight


