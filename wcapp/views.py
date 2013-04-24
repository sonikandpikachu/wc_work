#coding: utf-8
'''
Created on Sep 18, 2012

@author: Pavel
'''

import os
from sqlorm import *
from flask import render_template, request, abort, session, jsonify, render_template_string
from tooltips import TOOLTIPS_DICT
import json

from wcconfig import app, PROM
import filters.settings
import pretty_data
import db_queries
import mail


#move to html settings
COMPUTERS_ON_PAGE = 10
DEFFAULT_DEVICE_TYPE = u'computer'


FILTERS = {
    u'computer': filters.settings.COMP_FILTERS,
    u'notebook': filters.settings.NOTEBOOK_FILTERS,
    u'all': filters.settings.ALL_FILTERS
}


@app.route('/')
def first():
    return render_template('index.html')


@app.route('/qa/', methods=['GET'])
def second():
    #need refactor dbwrapper calls
    dbwrapper = db_queries.DBWrapper(DEFFAULT_DEVICE_TYPE)
    #getting computers id:
    if 'type' in request.args.keys():
        session['type'] = request.args['type']
        dbwrapper = db_queries.DBWrapper(request.args['type'])
        devices_id, devices_dss, dss_dict = filtered_devices_id(FILTERS[dbwrapper.device], request.args, dbwrapper)
        if 'user_id' in session:
            db_queries.delete_user(session['user_id'])
            del session['user_id']
        user_id = db_queries.add_user(devices_id, devices_dss)
        session['user_id'] = user_id
    else:
        devices_id, devices_dss, dss_dict = None, None, {}  # nothing to return

    if devices_id:
        last_page = int(round(float(len(devices_id)) / COMPUTERS_ON_PAGE + 0.49))
        first_comp_index = 0
        last_comp_index = min(COMPUTERS_ON_PAGE, len(devices_id))
        devices_id_on_page = devices_id[first_comp_index: last_comp_index]
        devices_dss_on_page = devices_dss[first_comp_index: last_comp_index]
        pretty_devices = pretty_data.small_devices(devices_id_on_page, devices_dss_on_page, dbwrapper)
        return render_template('QandA.html', computers=pretty_devices, filters=FILTERS[u'all'],
            pagination_pages=pretty_data.pagination_pages(last_page), dss_dict=dss_dict, prom = PROM)

    return render_template('QandA.html', computers=[], filters=FILTERS[u'all'], pagination_pages=[], dss_dict=dss_dict, prom = PROM)


def filtered_devices_id(filters, args, dbwrapper):
    '''
    Gets parameters from request args, executes filters functions and finally returns filtered computers id
    '''
    #choosing with what device we are working
    #print 'args', args
    dss_values, cut_values = [], []
    for filt in filters:
        print filt.name
        names = filt.get_names()
        values_dict = dict((key, args[key]) for key in args.keys() if key.split('_')[0] in names)
        print 'values_dict', values_dict        
        if values_dict:
            dss, cut = filt.get_answers(values_dict)
            if dss:
                dss_values.append(dss)
            if cut:
                cut_values.append(cut)    
    return dbwrapper.sorted_devices_id(cut_values, dss_values)


@app.route('/computer/<id>/<dss>/')
def third_computer(id, dss):
    dbwrapper = db_queries.DBWrapper("computer")
    concdevices = dbwrapper.concdevices_by_device_id(id)
    big_pretty_comp = pretty_data.big_computer(id, dbwrapper)
    small_pretty_comp = pretty_data.small_devices([id], [float(dss)], dbwrapper)[0]
    return render_template('Comp.html', big_comp=big_pretty_comp,
                                small_comp=small_pretty_comp,
                                tooltips = TOOLTIPS_DICT,
                                conccomps=concdevices, prom = PROM)


@app.route('/notebook/<id>/<dss>/')
def third_notebook(id, dss):
    dbwrapper = db_queries.DBWrapper("notebook")
    concdevices = dbwrapper.concdevices_by_device_id(id)
    big_pretty_notebook = pretty_data.big_notebook(id, dbwrapper)
    small_pretty_notebook = pretty_data.small_devices([id], [float(dss)], dbwrapper)[0]
    return render_template('Comp.html', big_comp=big_pretty_notebook,
                                small_comp=small_pretty_notebook,
                                
                                tooltips = TOOLTIPS_DICT,
                                conccomps=concdevices, prom = PROM)


@app.route('/getPage/<page>/<type>/')
def getPage(page, type):
    dbwrapper = db_queries.DBWrapper(type)
    user = db_queries.get_user(session['user_id'])
    if user:
        devices_id, devices_dss = user['devices_id'], user['devices_dss']
        dss_dict = {}  # ????
    else:  # there is no such user in our db
        del session['user_id']
        devices_id, devices_dss, dss_dict = [], [], {}  # nothing to return
    first_comp_index = (int(page) - 1) * COMPUTERS_ON_PAGE
    last_comp_index = min(int(page) * COMPUTERS_ON_PAGE, len(devices_id))
    devices_id_on_page = devices_id[first_comp_index: last_comp_index]
    devices_dss_on_page = devices_dss[first_comp_index: last_comp_index]

    pretty_devices = pretty_data.small_devices(devices_id_on_page, devices_dss_on_page, dbwrapper)
    resp = jsonify({"pretty_devices": pretty_devices})
    resp.status_code = 200
    return resp


@app.route('/feedback/', methods=['GET'])
def feedback():
    mail.save_feedback(request.args['msg'], request.args['email'])
    resp = jsonify({"Send":"true"})
    resp.status_code = 200
    return resp

@app.route('/tooltip/<key>/')
def tooltip(key):        
    return render_template_string(TOOLTIPS_DICT[key])

@app.route('/gallery/<type>/<id>/')
def gallery(type,id):
    dir = os.path.join(os.path.dirname(__file__), 'static/img/' + type + 's/' + id + "_img")
    names = os.listdir(dir)   # список файлов и поддиректорий в данной директории
    if len (names) != 1: names.remove('main.jpg')
    return render_template('gallery.html', images=names, type = type, id = id)


if __name__ == '__main__':
    #app.run(host = '192.168.1.100', port = 80)
    #port = int(os.environ.get('PORT', 5000))
    #app.run(host='0.0.0.0', port=port)
    app.run(debug=True)
    # controller = SQLController()
    # session = controller.create_sql_session()
    # components =  wc_RAM, wc_HD, wc_CPU, wc_OS, wc_ODD, wc_Screen, wc_Type, wc_Chipset
    # query = session.query(wc_Computer).join(*components)
    # print query.filter('wc_HD.id = 1 and wc_CPU.id > 2').all()
