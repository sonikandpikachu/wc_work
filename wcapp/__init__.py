#coding: utf-8
import os
import codecs

import sqlalchemy
import support.pkl_to_dict as ptd
import support.sql_generator as gen
import support.save_load as sl
import sqlorm
from wcconfig import db
import support.utf8_converter

support.utf8_converter.setup_console()

#inserting dss values:
computers = sqlorm.wc_Computer.query.all()

# allprices = [comp.price for comp in computers if comp.price > 0]
allrams = [comp.ram_amount for comp in computers if comp.ram_amount]
# allhdd = [comp.hdd_capacity for comp in computers if comp.hdd_capacity]
allcpu = [comp.testcpu_passmark**0.25 for comp in computers if comp.testcpu_passmark]
allvga = [comp.testvga_3dmark06**0.25 for comp in computers if comp.testvga_3dmark06]
# pricemin, pricemax = min(allprices), max(allprices)
rammin, rammax = min(allrams), max(allrams)
# hddmin, hddmax = min(allhdd), max(allhdd)
cpumin, cpumax = min(allcpu), max(allcpu)
vgamin, vgamax = min(allvga), max(allvga)

ram_dss = {'1':'20','2':'40','3':'50','4':'60','6':'70','8':'80','12':'90','16':'100',
'1024':'20','2048':'40','3072':'50','3096':'51','4096':'60','6144':'70','8192':'80','12288':'90','16384':'100'}


print rammax, rammin
for comp in computers:
    values = {
        'ram' : ram_dss[str(comp.ram_amount)] if comp.ram_amount else 0,
#         'price' : 100*(comp.price - pricemin) / (pricemax - pricemin) if comp.price > 0 else 0,
#         'hdd' : 100*(comp.hdd_capacity - hddmin)  / (hddmax - hddmin) if comp.hdd_capacity else 0,
        'cpu' : round(80*(comp.testcpu_passmark**0.25 - cpumin) / (cpumax - cpumin) + 20) if comp.testcpu_passmark else 0,
        'vga' : round(80*(comp.testvga_3dmark06**0.25 - vgamin) / (vgamax - vgamin) + 20) if comp.testvga_3dmark06 else 0
    }
    db.session.query(sqlorm.wc_DSS).filter_by(id = comp.id).update(values)
db.session.commit()



# print len(sqlorm.wc_Computer.query.all())

#inserting computers:
#pkl_notebooks = ptd.computers("../data/computers", 'support/config/computers.config')
#for c in pkl_notebooks:
#    print c['url'], c['network']
#     sqlcomp = sqlorm.wc_Computer(**c)
#     db.session.add(sqlcomp)
# db.session.commit()

# #inserting shops:
# pkl_shops = ptd.shops("../data/notebooks", "Устройство.магазины")
# for s in pkl_shops:
#     shop = sqlorm.wc_Shop(name = s)
#     db.session.add(shop)
# db.session.commit()



# inserting conccomputers:
# conccomputers = ptd.conccomputers("../data/notebooks", "Устройство.магазины", "Устройство.цены_грн", "Устройство.цены_длр")
# print len(conccomputers)
# for cc in conccomputers:
#     comp = sqlorm.wc_Computer.query.filter_by(url = cc['url']).one()
#     try: shop = sqlorm.wc_Shop.query.filter_by(name = cc['shop']).one()
#     except sqlalchemy.orm.exc.MultipleResultsFound: 
#         shops = sqlorm.wc_Shop.query.filter_by(name = cc['shop'])
#         shop = shops[0]
#         db.session.query(sqlorm.wc_Shop).filter_by(id = shops[1].id).delete()
#     sqlconccomp = sqlorm.wc_ConcComputer(price_usd = cc['price_usd'], price_grn = cc['price_grn'],
#                                         computer = comp, shop = shop)
#     print comp.id, shop.id
#     db.session.add(sqlconccomp)
# db.session.commit() 