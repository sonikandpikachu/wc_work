# coding: utf-8
'''
this module converts database data to data witch is going to be showm to user
'''

def small_computer(computer):
	'''
	prepare computer for QandA page
	'''
	pretty_computer = {
		'name' : computer.name,
		'dss' : computer.dss,
		'cpu_name' : computer.CPU.name,
		'cpu_frequency' : computer.CPU.frequency,
		'cpu_dss' : computer.CPU.dss,
		'ram_amount' : computer.RAM.amount,
		'ram_dss' : computer.RAM.dss,
		'hdd_amount' : computer.HD.hdd_amount,
		'ssd_amount' : computer.HD.ssd_amount,
		'hd_dss' : computer.HD.dss,
		'norm_price' : computer.norm_price,
		'os_name' : computer.OS.name,
		'os_dss' : computer.OS.dss,
		'price' : computer.price,
		'type_name' : computer.Type.name
	}
	return pretty_computer 

