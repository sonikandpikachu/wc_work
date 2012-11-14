#coding: utf-8
import support.pkl_to_dict as ptd
import sqlorm
from wcconfig import db

# shops = ptd.shops('../data/computers', 'Устройство.магазины')
# for shop in shops:
#     s = sqlorm.wc_Shop(name = shop)
#     db.session.add(s)
# db.session.commit()

pairs = ptd.conccomputers('../data/computers', 'Устройство.магазины', 'Устройство.цены_длр', 'Устройство.цены_грн')
sqlorm.add_conccomputers(pairs)
