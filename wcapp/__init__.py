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



print len(sqlorm.wc_Computer.query.all())

# #inserting computers:
# pkl_notebooks = ptd.computers("../data/notebooks", 'support/config/computers.config')
# for c in pkl_notebooks:
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
conccomputers = ptd.conccomputers("../data/notebooks", "Устройство.магазины", "Устройство.цены_грн", "Устройство.цены_длр")
print len(conccomputers)
for cc in conccomputers:
    comp = sqlorm.wc_Computer.query.filter_by(url = cc['url']).one()
    try: shop = sqlorm.wc_Shop.query.filter_by(name = cc['shop']).one()
    except sqlalchemy.orm.exc.MultipleResultsFound: 
        shops = sqlorm.wc_Shop.query.filter_by(name = cc['shop'])
        shop = shops[0]
        db.session.query(sqlorm.wc_Shop).filter_by(id = shops[1].id).delete()
    sqlconccomp = sqlorm.wc_ConcComputer(price_usd = cc['price_usd'], price_grn = cc['price_grn'],
                                        computer = comp, shop = shop)
    print comp.id, shop.id
    db.session.add(sqlconccomp)
db.session.commit() 