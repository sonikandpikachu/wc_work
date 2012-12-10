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
    #need to set this parameter bases on users choose
    dbwrapper = db_queries.DBWrapper('computer')
    #getting computers id:
    if request.method == 'POST': 
        computers_id, computers_dss, dss_dict = filtered_computers_id(ALL_FILTERS, request.form, dbwrapper)
        if 'user_id' in session: 
            dbwrapper.delete_user(session['user_id'])
            del session['user_id']
        user_id = dbwrapper.add_user(computers_id, computers_dss)
        session['user_id'] = user_id
    else:
        if 'user_id' in session:
            user = dbwrapper.get_user(session['user_id'])
            computers_id, computers_dss = user.computers_id, user.computers_dss
            dss_dict = {}#????
        else:
            computers_id, computers_dss, dss_dict  = [], [], {}#nothing to return 
    
    #pagination test(if bad or wrong page) - REWRITE!!!
    last_page = int(round(len(computers_id) / COMPUTERS_ON_PAGE + 0.49))
    try:
        page = int(request.args.get('page', '')) if 'page' in request.args else 1
    except ValueError:
        abort(404)
    # if page > last_page or page < 1:
    #     abort(404)

    first_comp_index = (page-1)*COMPUTERS_ON_PAGE
    last_comp_index = min(page*COMPUTERS_ON_PAGE, len(computers_id))
    computers_id_on_page = computers_id[first_comp_index : last_comp_index]    
    computers_dss_on_page = computers_dss[first_comp_index : last_comp_index]

    pretty_computers = pretty_data.small_computers(computers_id_on_page, computers_dss_on_page, dbwrapper)

    return render_template('QandA.html', computers = pretty_computers, filters = ALL_FILTERS,
        current_page = page, pagination_pages = pretty_data.pagination_pages(page, last_page), dss_dict = dss_dict)


def filtered_computers_id(filters, form, dbwrapper):
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
    return dbwrapper.sorted_computers_id(cut_values, dss_values)

 
if __name__ == '__main__':
    #app.run(debug = True, host = '192.168.1.100', port = 80)
    app.run(debug = True)
    # controller = SQLController()
    # session = controller.create_sql_session()
    # components =  wc_RAM, wc_HD, wc_CPU, wc_OS, wc_ODD, wc_Screen, wc_Type, wc_Chipset
    # query = session.query(wc_Computer).join(*components)
    # print query.filter('wc_HD.id = 1 and wc_CPU.id > 2').all()
        