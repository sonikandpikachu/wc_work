#coding: utf-8
'''
Created on Sep 18, 2012

@author: Pavel
'''
import operator
import sys

from sqlorm import *
from flask import Flask, render_template, request, abort, redirect, url_for, session

from wcconfig import app
from filters.settings import ALL_FILTERS
from filters import dss
import pretty_data
import db_queries

#move to html settings
COMPUTERS_ON_PAGE = 10

@app.route('/')
def first():
    return render_template('index.html') 
    
    
@app.route('/qa/', methods=['POST', 'GET'])
def second():
    #need refactor dbwrapper calls
    dbwrapper = db_queries.DBWrapper('computer')
    #getting computers id:
    if request.method == 'POST':
        session['type'] = request.form['type']
        dbwrapper = db_queries.DBWrapper(request.form['type'])
        devices_id, devices_dss, dss_dict = filtered_devices_id(ALL_FILTERS, request.form, dbwrapper)
        if 'user_id' in session: 
            dbwrapper.delete_user(session['user_id'])
            del session['user_id']
        user_id = dbwrapper.add_user(devices_id, devices_dss)
        session['user_id'] = user_id
    else:
        if 'user_id' in session:
            dbwrapper = db_queries.DBWrapper(session['type'])
            user = dbwrapper.get_user(session['user_id'])
            if user:
                devices_id, devices_dss = user.devices_id, user.devices_dss
                dss_dict = {}#????
            else:#there is no such user in our db
                del session['user_id']
                devices_id, devices_dss, dss_dict  = [], [], {}#nothing to return 
        else:
            devices_id, devices_dss, dss_dict  = [], [], {}#nothing to return 
    
    #pagination test(if bad or wrong page) - REWRITE!!!
    last_page = int(round(len(devices_id) / COMPUTERS_ON_PAGE + 0.49))
    try:
        page = int(request.args.get('page', '')) if 'page' in request.args else 1
    except ValueError:
        abort(404)
    # if page > last_page or page < 1:
    #     abort(404)

    first_comp_index = (page-1)*COMPUTERS_ON_PAGE
    last_comp_index = min(page*COMPUTERS_ON_PAGE, len(devices_id))
    devices_id_on_page = devices_id[first_comp_index : last_comp_index]    
    devices_dss_on_page = devices_dss[first_comp_index : last_comp_index]

    print 'page', page, 'last_page', last_page
    print 'pagination_pages', pretty_data.pagination_pages(page, last_page)

    pretty_devices = pretty_data.small_devices(devices_id_on_page, devices_dss_on_page, dbwrapper)

    return render_template('QandA.html', computers = pretty_devices, filters = ALL_FILTERS,
        current_page = page, pagination_pages = pretty_data.pagination_pages(page, last_page), dss_dict = dss_dict)


def filtered_devices_id(filters, form, dbwrapper):
    '''
    Gets parameters from request form, executes filters functions and finally returns filtered computers id
    '''
    #choosing with what device we are working
    dss_values, cut_values = [], []
    for filt in filters:
        values_dict = dict((key,form[key]) for key in form if key.startswith(filt.name))
        if values_dict:
            dss, cut = filt.get_answers(values_dict)
            if dss: dss_values.append(dss)
            if cut: cut_values.append(cut)
    print 'cut_values', cut_values, 'dss_values', dss_values
    print dbwrapper.sorted_devices_id(cut_values, dss_values)
    return dbwrapper.sorted_devices_id(cut_values, dss_values)


@app.route('/computer/<id>/')
def third_computer(id):
    dbwrapper = db_queries.DBWrapper(session['type'])
    concdevices = dbwrapper.concdevices_by_device_id(id)
    big_pretty_comp =  pretty_data.big_computer(id, dbwrapper)
    small_pretty_comp = pretty_data.small_devices([id], [0], dbwrapper)[0]
    return render_template('Comp.html', big_comp = big_pretty_comp,
                                small_comp = small_pretty_comp,
                                conccomps = concdevices)

 
if __name__ == '__main__':
    #app.run(debug = True, host = '192.168.1.100', port = 80)
    app.run(debug = True)
    # controller = SQLController()
    # session = controller.create_sql_session()
    # components =  wc_RAM, wc_HD, wc_CPU, wc_OS, wc_ODD, wc_Screen, wc_Type, wc_Chipset
    # query = session.query(wc_Computer).join(*components)
    # print query.filter('wc_HD.id = 1 and wc_CPU.id > 2').all()
        