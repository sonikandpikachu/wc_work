#coding: utf-8
'''
Created on Sep 18, 2012

@author: Pavel
'''
import os

from sqlorm import *
from flask import render_template, request, abort, session

from wcconfig import app
import filters.settings
import pretty_data
import db_queries

#move to html settings
COMPUTERS_ON_PAGE = 10
DEFFAULT_DEVICE_TYPE = u'computer'


def unique_union(list_a, list_b):
    union = list(list_a)
    for el in list_b:
        if el not in list_a:
            union.append(el)
    return union


FILTERS = {
    u'computer': filters.settings.COMP_FILTERS,
    u'notebook': filters.settings.NOTEBOOK_FILTERS,
    u'all': unique_union(filters.settings.COMP_FILTERS, filters.settings.NOTEBOOK_FILTERS)
}


@app.route('/')
def first():
    return render_template('index.html')


@app.route('/qa/', methods=['GET'])
def second():
    #need refactor dbwrapper calls
    dbwrapper = db_queries.DBWrapper(DEFFAULT_DEVICE_TYPE)
    #getting computers id:
    print request.args
    if 'type' in request.args.keys():
        session['type'] = request.args['type']
        dbwrapper = db_queries.DBWrapper(request.args['type'])
        devices_id, devices_dss, dss_dict = filtered_devices_id(FILTERS[dbwrapper.device], request.args, dbwrapper)
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
                dss_dict = {}  # ????
            else:  # there is no such user in our db
                del session['user_id']
                devices_id, devices_dss, dss_dict = [], [], {}  # nothing to return
        else:
            devices_id, devices_dss, dss_dict = [], [], {}  # nothing to return

    last_page = int(round(float(len(devices_id)) / COMPUTERS_ON_PAGE + 0.49))
    # pagination test(if bad or wrong page) - REWRITE!!!
    try:
        page = int(request.args.get('page', '')) if 'page' in request.args else 1
    except ValueError:
        abort(404)
    # if page > last_page or page < 1:
    #     abort(404)

    first_comp_index = (page - 1) * COMPUTERS_ON_PAGE
    last_comp_index = min(page * COMPUTERS_ON_PAGE, len(devices_id))
    devices_id_on_page = devices_id[first_comp_index: last_comp_index]
    devices_dss_on_page = devices_dss[first_comp_index: last_comp_index]

    pretty_devices = pretty_data.small_devices(devices_id_on_page, devices_dss_on_page, dbwrapper)

    return render_template('QandA.html', computers=pretty_devices, filters=FILTERS[u'all'],
        current_page=page, pagination_pages=pretty_data.pagination_pages(page, last_page), dss_dict=dss_dict)


def filtered_devices_id(filters, args, dbwrapper):
    '''
    Gets parameters from request args, executes filters functions and finally returns filtered computers id
    '''
    #choosing with what device we are working
    print 'ARGS', args
    dss_values, cut_values = [], []
    for filt in filters:
        values_dict = dict((key, args[key]) for key in args.keys() if key.startswith(filt.name))
        if values_dict:
            dss, cut = filt.get_answers(values_dict)
            if dss:
                dss_values.append(dss)
            if cut:
                cut_values.append(cut)
    print 'cut_values', cut_values, 'dss_values', dss_values
    print dbwrapper.sorted_devices_id(cut_values, dss_values)
    return dbwrapper.sorted_devices_id(cut_values, dss_values)


@app.route('/computer/<id>/')
def third_computer(id):
    dbwrapper = db_queries.DBWrapper(session['type'])
    concdevices = dbwrapper.concdevices_by_device_id(id)
    big_pretty_comp = pretty_data.big_computer(id, dbwrapper)
    small_pretty_comp = pretty_data.small_devices([id], [0], dbwrapper)[0]
    return render_template('Comp.html', big_comp=big_pretty_comp,
                                small_comp=small_pretty_comp,
                                conccomps=concdevices)


if __name__ == '__main__':
    #app.run(host = '192.168.1.100', port = 80)
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
    # print FILTERS[u'computer']
    # print FILTERS[u'notebook']
    # print FILTERS[u'all']
    # controller = SQLController()
    # session = controller.create_sql_session()
    # components =  wc_RAM, wc_HD, wc_CPU, wc_OS, wc_ODD, wc_Screen, wc_Type, wc_Chipset
    # query = session.query(wc_Computer).join(*components)
    # print query.filter('wc_HD.id = 1 and wc_CPU.id > 2').all()
