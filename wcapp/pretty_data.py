# coding: utf-8
'''
this module converts database data to data witch is going to be showm to user
'''
import operator

import sqlorm as sql
from wcconfig import db

def small_computers(computers_id, computers_dss, dbwrapper):
	'''
	prepare computer for QandA page
	'''
	dsses = dbwrapper.dss_by_id(computers_id)
	computers = dbwrapper.parameters_by_id(computers_id)
	pretty_computers = []
	for index, dss, computer in zip(range(len(dsses)), dsses, computers):		
		pretty_computer = {
		#
		#   A mozno mne peredat otdelno vse dostupnie dss vmeste spiskop
		#	Toest chtob bilo i 'price_dss',vga_dss',... i  prosto spisok - dsses
		#	
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
            'os_dss' : dss.os,
			'price' : computer.price,
			'vga' : computer.vga_model,
			'vga_amount' : computer.vga_amount,
			'vga_dss' : dss.vga,
			'price_dss' : dss.price,
            'display_dss' : dss.display
		}
		pretty_computers.append(pretty_computer)
	return pretty_computers 

#I think this function code is bad, but no ideas how to make it better :( 
def pagination_pages(current_page, last_page):
    pages = set((1,2,current_page-1,current_page,current_page+1,last_page-1,last_page))
    if 0 in pages: pages.remove(0)
    if last_page+1 in pages: pages.remove(last_page+1)
    pages = list(pages)
    pages.sort()
    pagination_pages = []
    for i in range(len(pages)-1):
        pagination_pages.append(pages[i])
        if pages[i]+1 != pages[i+1]:
            pagination_pages.append('...')
    pagination_pages.append(pages[-1])
    return pagination_pages

