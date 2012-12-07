# coding: utf-8
'''
This module gets data from database, cuts it, sorts it
'''
import operator

from wcconfig import db
import sqlorm as sql
from support import pkl_to_dict as ptd

def _cutted_computers_id (cut_values):
    '''
    Gets result of filters cut_function as list. Returns ids of filtered computers
    '''
    print cut_values
    cut_string = ' AND '.join(cut_values)
    print 'CUT STRING', cut_string
    computers_id = db.session.query(sql.wc_Computer.id).filter(cut_string).all()
    return tuple(int(comp[0]) for comp in computers_id)


def sorted_computers_id (cut_values, dss_values):
    '''
    Cuts computers and sort them by dss
    Notice that we can put initial dss values to dss_dict
    '''
    dss_dict = {'hdd' : 0.5, 'cpu' : 4, 'ram' : 3, 'vga' : 1, 'price' : -8}   
    for dss in dss_values: 
        for key in dss:
            dss_dict[key] += dss[key]    
    computers_id = _cutted_computers_id(cut_values)
    sqldsses = db.session.query(sql.wc_DSS).filter(sql.wc_DSS.id.in_(computers_id)).all()
    computers_dss = {}#dict of id and dss for each computers
    for sqldss in sqldsses:
        computers_dss[sqldss.id] = sum([sqldss.__dict__[key] * dss_dict[key] for key in dss_dict.iterkeys()])        
    _min, _max = min(computers_dss.values()), max(computers_dss.values())
    computers_dss = sorted(computers_dss.iteritems(), key=operator.itemgetter(1), reverse = True)#sorting by values, gets list of tuples
    #ZeroDivisionError fix (if only ONE computer in answer):
    if _min == _max: return computers_dss[0], 100, dss_dict
    return tuple(cd[0] for cd in computers_dss), tuple((cd[1] - _min)*100/(_max - _min) for cd in computers_dss), dss_dict


#for development only
def __values_for_dss ():
    import xlwt
    wbk = xlwt.Workbook()
    prefixes = 'hdd', 'cpu', 'ram', 'vga'
    for prefix in prefixes:
        all_values = {}
        id_values = {}
        comp_dict = sql.wc_Computer.query.first().__dict__.keys()
        columns = [name for name in comp_dict if prefix in name]
        for comp in sql.wc_Computer.query.all():
            values = tuple(comp.__dict__[column] for column in columns)
            if values in all_values: 
                all_values[values].append(comp.url)
                id_values[values].append(comp.id)
            else: 
                all_values[values] = [comp.url]
                id_values[values] = [comp.id]
        sheet = wbk.add_sheet(prefix)
        for i, column in enumerate(columns + ['id', 'url', 'dss']):
            sheet.write(0, i, column)
        for i, values in enumerate(all_values):
            for j, value in enumerate(values):
                sheet.write(i+1, j, value)
            sheet.write(i+1, len(values) + 1, ', '.join(all_values[values]))
            sheet.write(i+1, len(values), ', '.join([str(v) for v in id_values[values]]))
    wbk.save('dss.xls')

#for development only(doesn`t work - rewrite)
def __dss_values_to_db():
    import xlrd
    wbk = xlrd.open_workbook('dss.xls')
    sheet_names = wbk.sheet_names()
    for name in sheet_names:
        sheet = wbk.sheet_by_name(name)
        column_names = dict( (row_value, i) for i, row_value in enumerate(sheet.row_values(0))) 
        assert 'url' in column_names and 'dss' in column_names, 'dss or url isn`t defined in sheet ' + name
        urls = [column_name.strip() for column_name in column_names['url']]

#for development only
def __write_prices():
    for comp in sql.wc_Computer.query.all():
        prices = [conc.price_usd for conc in comp.concretes]
        price = sum(prices)/len(prices) if prices else -1
        db.session.query(sql.wc_Computer).filter_by(id = comp.id).update({'price' : price}, synchronize_session=False)
    db.session.commit()


if __name__ == '__main__':
    __write_prices()
    # print  db.session.query(sql.wc_Computer.id).filter('os like "%mac%"').all()
    # print sorted_computers_id([], [{'hdd' : 1, 'cpu' : 3}])
    # __values_for_dss()
    # __dss_values_to_db()




