# coding: utf-8
'''
This module gets data from database, cuts it, sorts it
'''
import xlwt
import xlrd

from wcconfig import db
import sqlorm as sql

def cutted_computers (cut_string):
    return sql.wc_Computer.query.filter(cut_string).all()


def sorted_computers ():
    pass


#for development only
def __values_for_dss ():
    wbk = xlwt.Workbook()
    prefixes = 'hdd', 'cpu', 'ram', 'vga'
    for prefix in prefixes:
        all_values = {}
        comp_dict = sql.wc_Computer.query.first().__dict__.keys()
        columns = [name for name in comp_dict if prefix in name]
        for comp in sql.wc_Computer.query.all():
            values = tuple(comp.__dict__[column] for column in columns)
            if values in all_values: all_values[values].append(comp.url)
            else: all_values[values] = [comp.url] 
        sheet = wbk.add_sheet(prefix)
        for i, column in enumerate(columns + ['url']):
            sheet.write(0, i, column)
        for i, values in enumerate(all_values):
            for j, value in enumerate(values):
                sheet.write(i+1, j, value)
            sheet.write(i+1, len(values), ', '.join(all_values[values]))
    wbk.save('dss.xls')

#for development only
def __dss_values_to_db():
    wbk = xlrd.open_workbook('dss.xls')
    sheet_names = wbk.sheet_names()
    for name in sheet_names:
        sheet = wbk.sheet_by_name(name)
        attributes = sheet.row_values(0)[:-1]
        dss_values = {}
        for rownum in xrange(1, sheet.nrows):
            dss_values[tuple(sheet.row_values(rownum)[:-1])] = sheet.row_values(rownum)[-1]
        # for value in dss_values:
        #     print value, ':', dss_values[value]
        for dbcomp in sql.wc_Computer.query.all():
            dbcomp_values = [dbcomp.__dict__[attr] for attr in attributes]
            for index in range(len(dbcomp_values)):
                if isinstance(dbcomp_values[index], str): dbcomp_values[index] = unicode(value)
                if not dbcomp_values[index]: dbcomp_values[index] = ''
                # if isinstance(dbcomp_values[index], long): print dbcomp_values[index]
            dbcomp_values = tuple(dbcomp_values)
            print 'id', sql.wc_DSS.query.filter_by(id = dbcomp.id).first().id
            sql.wc_DSS.query.filter_by(id = dbcomp.id).\
                update({name:dss_values[dbcomp_values]}, synchronize_session=False) 
            del dbcomp_values 
        sql.db.session.commit()



if __name__ == '__main__':
    __values_for_dss()




