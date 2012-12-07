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
	dsses = [db.session.query(sql.wc_DSS).filter_by(id = cid).one() for cid in computers_id]
	computers = [db.session.query(sql.wc_Computer).filter_by(id = cid).one() for cid in computers_id]
	pretty_computers = []
	for index, dss, computer in zip(range(len(dsses)), dsses, computers):		
		pretty_computer = {		
			'id' : str(computer.id),
			'name' : computer.name,
			'dss' : computers_dss[index],
			'cpu_name' : computer.cpu_name,
			'cpu_model' : computer.cpu_model,
			'cpu_frequency' : computer.cpu_frequency,
			'cpu_dss' : dss.cpu,			
			'ram_amount' : computer.ram_amount,
			'ram_dss' : dss.ram,
			'hdd_capacity' : computer.hdd_capacity,
			'hdd_dss' : dss.hdd,
			'os' : computer.os,
			'price' : computer.price,
			'vga' : computer.vga_model,
			'vga_amount' : computer.vga_amount,
			'vga_dss' : dss.vga,
			'price_dss' : dss.price
		}
		pretty_computers.append(pretty_computer)
	return pretty_computers 

