# coding: utf-8
'''
This module gets data from database, cuts it, sorts it
'''

from wcconfig import db
import sqlorm as sql

def cutted_computers (cut_string):
    return sql.wc_Computer.query.filter(cut_string).all()


def sorted_computers ():
    pass


#for development only
def __values_for_dss ():
    prefixes = 'hdd', 'cpu', 'display', 'ram', 'vga'
    for prefix in prefixes:
        all_values = set()
        print 'PREFIX', prefix
        comp_dict = sql.wc_Computer.query.first().__dict__.keys()
        columns = [name for name in comp_dict if prefix in name]
        for comp in sql.wc_Computer.query.all():
            values = tuple(comp.__dict__[column] for column in columns)
            all_values.add(values)
        print len(all_values)



if __name__ == '__main__':
    __values_for_dss()



