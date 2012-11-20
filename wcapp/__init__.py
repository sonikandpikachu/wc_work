#coding: utf-8
# import support.pkl_to_dict as ptd
# import sqlorm
# from wcconfig import db
# import support.utf8_converter

# #inserting computers:
# pkl_computers = ptd.computers("../data/computers", 'support/config/computers.config')
# for c in pkl_computers:
#     print c
#     sqlcomp = sqlorm.wc_Computer(**c)
#     db.session.add(sqlcomp)
# db.session.commit()

# #inserting shops:
# pkl_shops = ptd.shops("../data/computers", "Устройство.магазины")
# for s in pkl_shops:
#     shop = sqlorm.wc_Shop(name = s)
#     db.session.add(shop)
# db.session.commit()

# #inserting conccomputers:
# conccomputers = ptd.conccomputers("../data/computers", "Устройство.магазины", "Устройство.цены_грн", "Устройство.цены_длр")
# for cc in conccomputers:
#     comp = sqlorm.wc_Computer.query.filter_by(url = cc['url']).one()
#     shop = sqlorm.wc_Shop.query.filter_by(name = cc['shop']).one()
#     sqlconccomp = sqlorm.wc_ConcComputer(price_usd = cc['price_usd'], price_grn = cc['price_grn'],
#                                         computer = comp, shop = shop)
#     db.session.add(sqlconccomp)
# db.session.commit() 