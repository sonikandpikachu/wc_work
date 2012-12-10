# coding: utf-8
'''
This module is only for database development - inserting deleting and updating somevalues.
Also it put dss values to .xls and imports them to table
Its highly recomendent not to use any of this methods in other modules

If you want to make some actions to some other devices(not computers), just change
workdss, workdevice, workconcdevice and datapass parameters
'''
import sqlalchemy

from wcconfig import db
import sqlorm as sql
from support import pkl_to_dict as ptd

workdevice = sql.wc_Computer
workconcdevice = sql.wc_ConcComputer
workdss = sql.wc_ComputerDSS
workpass = "../data/computers"
workconfig = 'support/config/computers.config'


def __values_for_dss ():
    ''' export data from db to dss.xls '''
    import xlwt
    wbk = xlwt.Workbook()
    prefixes = 'hdd', 'cpu', 'ram', 'vga'
    for prefix in prefixes:
        all_values = {}
        id_values = {}
        comp_dict = workdevice.query.first().__dict__.keys()
        columns = [name for name in comp_dict if prefix in name]
        for comp in workdevice.query.all():
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


def __dss_values_to_db():
    ''' writes dss values from file dss.xls to db. File have to be in the same folder'''
    import xlrd
    wbk = xlrd.open_workbook('dss.xls')
    sheet_names = wbk.sheet_names()
    print '111'
    for name in sheet_names:
        sheet = wbk.sheet_by_name(name)
        column_names = dict((row_value,i) for i, row_value in enumerate(sheet.row_values(0)))
        # print 'column_names', column_names
        assert 'id' in column_names,'dss or url isn`t defined in sheet ' + name
        print 'ssss'
        for nrow in range(1, sheet.nrows):
            row_values = sheet.row_values(nrow)
            ids = [int(rv.strip()) for rv in row_values[column_names['id']].split(',')]
            for id in ids:
                xlscomp = dict((cn, row_values[column_names[cn]]) for cn in column_names if not cn in ('Passmark G3D Mark', 'id'))
                if 'vga_amount' in xlscomp and not xlscomp['vga_amount']: del xlscomp['vga_amount']
                db.session.query(workdevice).filter_by(id = id).update(xlscomp)
            db.session.commit()
            print nrow


def __insert_computers():
    ''' inserts .pkl devices to notebooks, as it setted in config file'''
    pkldevices = ptd.computers(workpass, workconfig)
    for pkldevice in pkldevices:
        device = workdevice(**pkldevice)
        db.session.add(device)
    db.session.commit()


def __insert_prices():
    ''' adds average prices to every computer '''
    for comp in workdevice.query.all():
        prices = [conc.price_usd for conc in comp.concretes]
        price = sum(prices)/len(prices) if prices else -1
        db.session.query(workdevice).filter_by(id = comp.id).update({'price' : price}, synchronize_session=False)
    db.session.commit()


def __insert_concdevices():
    '''inserting concrete computers (comp with shop) to db'''
    conccomputers = ptd.conccomputers(workpass, "Устройство.магазины", "Устройство.цены_грн", "Устройство.цены_длр")
    print len(conccomputers)
    for cc in conccomputers:
        comp = workdevice.query.filter_by(url = cc['url']).one()
        try: shop = sql.wc_Shop.query.filter_by(name = cc['shop']).one()
        except sqlalchemy.orm.exc.MultipleResultsFound: 
            shops = sql.wc_Shop.query.filter_by(name = cc['shop'])
            shop = shops[0]
            db.session.query(sql.wc_Shop).filter_by(id = shops[1].id).delete()
        sqlconccomp = workconcdevice(price_usd = cc['price_usd'], price_grn = cc['price_grn'],
                                            computer = comp, shop = shop)
        db.session.add(sqlconccomp)
    db.session.commit()


def __insert_shops():
    '''Inserting all shops from workpass'''
    pkl_shops = ptd.shops(workpass, "Устройство.магазины")
    for s in pkl_shops:
        shop = sql.wc_Shop(name = s)
        db.session.add(shop)
    db.session.commit()


def __insert_empty_dss():
    '''inserts only dss id'''
    devices = db.session.query(workdevice).all()
    for device in devices:
        dss = workdss(id = device.id)
        db.session.add(dss)
    db.session.commit()


def __update_devices():
    '''updating devices'''
    pkl_notebooks = ptd.computers(workpass, workconfig)
    for c in pkl_notebooks:
        del c['id']
        db.session.query(workdevice).filter_by(id = id).update(c)
    db.session.commit()


def __update_auto_dss():
    '''inserting dss values, wich is autocalculated, based on deffault parameters. Works only for computers and 
    notebooks'''
    computers = workdevice.query.all()
    # Don't change!!!    
    allhdd = [comp.hdd_capacity for comp in computers if comp.hdd_capacity]
    allcpu = [comp.testcpu_passmark**0.25 for comp in computers if comp.testcpu_passmark]
    allvga = [comp.testvga_3dmark06**0.25 for comp in computers if comp.vga_amount] 
  
    hddmin, hddmax = min(allhdd), max(allhdd)
    cpumin, cpumax = min(allcpu), max(allcpu)
    vgamin, vgamax = min(allvga), max(allvga)

    ram_dss = {'1':20,'2':40,'3':50,'4':60,'6':70,'8':80,'12':90,'16':100}
    
    def oss_dss_calc(os_name):
        os_dss_dict = {'FreeDOS':0,'Linux':20,'Windows 7 Starter':30,'Windows 8':80,'Windows 7 Professional':100}
        os_dss = 50
        for key in os_dss_dict:
            if key in os_name: os_dss = os_dss_dict[key] 
        return os_dss

    for comp in computers:
        values = {
            'ram' : ram_dss[str(comp.ram_amount)] if comp.ram_amount else 0,
            'price' : comp.price / 500 if comp.price > 0 else 0,
            'os': oss_dss_calc(comp.os),
            # 'hdd' : 100*(comp.hdd_capacity - hddmin)  / (hddmax - hddmin) if comp.hdd_capacity.replace('-','') else 0,
            'cpu' : round(90*(comp.testcpu_passmark**0.25 - cpumin) / (cpumax - cpumin) + 10) if comp.testcpu_passmark else 0,
            'vga' : round(90*(comp.testvga_3dmark06**0.25 - vgamin) / (vgamax - vgamin) + 10) if comp.testvga_3dmark06 else 0
        }
        db.session.query(workdss).filter_by(id = comp.id).update(values)
    db.session.commit()


if __name__ == '__main__':
    __update_auto_dss()
    # __insert_prices()
    # __insert_shops()
    # __insert_concdevices()
    # __dss_values_to_db()