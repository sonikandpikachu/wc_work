#coding: utf-8
'''
Created on Sep 30, 2012

@author: Pavel
This module works with dss weights and values.
DEPRECATED!!!  
'''

DSS_WEIGHTS = {'CPU' : 1, 'RAM' : 0.8, 'VGA' : 0.9, 'Battery' : 0.5, 'HD' : 0.7, 'ODD' : 0.1, 'OS' : 0.2}
DSS_NORM_COMPWEIGHTS = {'norm_price' : -6, 'norm_weight' : -0.3}
DSS_COMPWEIGHTS = {'wifi' : 0.1, 'Bluetooth' : 0.1, 'cardreader' : 0.1, 'modem56' : 0.1,
					 'webcamera' : 0.1, 'G3': 0.1, 'wimax' : 0.1, 'network_adapter' : 0.1}

error_el = set()
def dss_weight (computer):
	'''
	gets sqlorm.wc_Computer and returns dss weight for this computer
	'''
	weight = 0
	for w in DSS_WEIGHTS:
		if getattr(computer, w) and getattr(computer, w).dss: weight += DSS_WEIGHTS[w]*getattr(computer, w).dss
		# #only for testing:
		# if getattr(computer, w) and not getattr(computer, w).dss:
		# 	error_el.add((w, getattr(computer, w).id))
	for w in DSS_NORM_COMPWEIGHTS:
		if getattr(computer, w): weight += getattr(computer, w) * DSS_NORM_COMPWEIGHTS[w]
	for w in DSS_COMPWEIGHTS:
		weight += getattr(computer, w) * DSS_COMPWEIGHTS[w] * 100
	return weight



