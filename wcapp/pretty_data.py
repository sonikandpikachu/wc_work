# coding: utf-8
'''
this module converts database data to data witch is going to be showm to user
'''
import operator

import sqlorm as sql
from wcconfig import db

def small_computers(computers_id, computers_dss):
	'''
	prepare computer for QandA page
	'''
	dsses = db.session.query(sql.wc_DSS).filter(sql.wc_DSS.id.in_(computers_id)).all()
	computers = db.session.query(sql.wc_Computer).filter(sql.wc_Computer.id.in_(computers_id)).all()
	# Tut nado sdelat pravilnuy sortirovku (poka v computers_id - pravilno, a v computers - ne pravilno)
	pretty_computers = []
	for index, dss, computer in zip(range(len(dsses)), dsses, computers):
		print str(computer.id), str(dss.id)
		pretty_computer = {
		#
		#   A mozno mne peredat otdelno vse dostupnie dss vmeste spiskop
		#	Toest chtob bilo i 'price_dss',vga_dss',... i  prosto spisok - dsses
 		#
			'id' : str(computer.id),
			'name' : computer.name,
			'dss' : computers_dss[index],
			'cpu_name' : computer.cpu_name,
			'cpu_frequency' : computer.cpu_frequency,
			'cpu_dss' : dss.cpu,
			'ram_amount' : computer.ram_amount,
			'ram_dss' : dss.ram,
			'hdd_capacity' : computer.hdd_capacity,
			'hdd_dss' : dss.hdd,
			'os' : computer.os,
			'price' : computer.price,
			'vga' : computer.vga_amount,
			'vga_dss' : dss.vga,
			'price_dss' : dss.price
		}
		pretty_computers.append(pretty_computer)
	return pretty_computers 

