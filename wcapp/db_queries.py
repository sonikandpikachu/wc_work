# coding: utf-8
'''
This module gets data from database, cuts it, sorts it
'''
import operator
import sqlalchemy

from wcconfig import db
import sqlorm as sql
from support import pkl_to_dict as ptd


class DBWrapper (object):
    '''
    This class executes all db queries
    Parameter device defines with what device we are currently working(computer, notebook, etc...)
    '''
    #in this dictionary we defines dsses for every device type
    _device_dss = {
        'computer' : {
                        'cpu' : 4, 
                        'ram' : 3, 
                        'vga' : 1, 
                        'os' : 1, 
                        'price' : -8
        },
    }

    _device_parameters = {
            'computer' : [sql.wc_Computer, sql.wc_ComputerDSS, sql.wc_ConcComputer]
            # 'notebook' : [sql]
    }

    def __init__(self, device):
        #This dict containes sql tables for every device type, which is in our base
        #so if you set device = 'computer' class will now that it have to work with
        #'computer' sql tables.
        self._device = device
        self.device_table, self.dss_table, self.concdevice_table = self._device_parameters[device]

    def device():
        doc = "The device property."
        def fget(self):
            return self._device
        def fset(self, value):
            self._device = value
            self.device_table, self.dss_table, self.concdevice_table = device_parameters[self._device]
        return locals()
    device = property(**device())

    def _cutted_computers_id (self, cut_values):
        '''
        Gets result of filters cut_function as list. Returns ids of filtered computers
        '''
        # print cut_values
        cut_string = ' AND '.join(cut_values)
        # print 'CUT STRING', cut_string
        computers_id = db.session.query(self.device_table.id).filter(cut_string).all()
        return tuple(int(comp[0]) for comp in computers_id)

    def sorted_computers_id (self, cut_values, dss_values):
        '''
        Cuts computers and sorts them by dss
        Notice that we can put initial dss values to _device_dss(upper)
        Returns 3 tuples: sorted_computers_id, sorted_computers_dss, initial dss values
        WHAT FOR DO WE NEED TO RETURN DSS_DICT???
        '''
        dss_dict = self._device_dss[self._device]
        print dss_dict
        for dss in dss_values: 
            for key in dss:
                dss_dict[key] += dss[key]
        computers_id = self._cutted_computers_id(cut_values)#all devices after cutting
        #getting dss for this devices from db
        sqldsses = db.session.query(self.dss_table).filter(self.dss_table.id.in_(computers_id)).all()
        computers_dss = {}#dict of id and dss for each device
        #adding pairs id:dss to this dict
        for sqldss in sqldsses:
            computers_dss[sqldss.id] = sum([sqldss.__dict__[key] * dss_dict[key] for key in dss_dict.iterkeys()])
        #if there is no computers - return empty lists
        if not computers_dss: return [], [], dss_dict
        _min, _max = min(computers_dss.values()), max(computers_dss.values())
        #sorting by dsses, gets list of tuples:
        computers_dss = sorted(computers_dss.iteritems(), key=operator.itemgetter(1), reverse = True)
        #if min == max (or we have only one device or all selected devices have equal dss)
        if _min == _max:
            sorted_computers_dss = tuple(100 for cd in computers_dss)
        else:
            sorted_computers_dss = tuple((cd[1] - _min)*100/(_max - _min) for cd in computers_dss)
        return (tuple(cd[0] for cd in computers_dss), 
                sorted_computers_dss,
                dss_dict)

    def parameters_by_id (self, ids):
        return [db.session.query(self.device_table).filter_by(id = id).one() for id in ids]

    def dss_by_id (self, ids):
        return [db.session.query(self.dss_table).filter_by(id = id).one() for id in ids]

    def max_and_min_price(self, device):
        all_prices = db.session.query(self.concdevice_table.price_grn).filter_by(device = device).\
            order_by(self.concdevice_table.price_grn).all()
        return float(all_prices[0][0]), float(all_prices[-1][0])

    #mb opertions with user shouldn`t be in this class
    def add_user (self, computers_id, computers_dss):
        user = sql.wc_User(computers_id = computers_id, computers_dss = computers_dss)
        db.session.add(user)
        db.session.commit()
        return user.id

    def delete_user(self, id):
        try:
            user = db.session.query(sql.wc_User).filter_by(id = id).one()
            db.session.delete(user)
            db.session.commit()
        except (sqlalchemy.orm.exc.NoResultFound): pass

    def get_user(self, id):
        try:
            user = db.session.query(sql.wc_User).filter_by(id = id).one()
        except (sqlalchemy.orm.exc.NoResultFound):
            user = None
        return user


