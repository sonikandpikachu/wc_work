#coding: utf-8
'''
Created on Sep 18, 2012

@author: Pavel
'''
import operator

from sqlorm import *
from flask import Flask, render_template, request, abort, redirect, url_for, session

from wcconfig import app
from filters.settings import ALL_FILTERS
from filters import dss
import pretty_data
import db_queries

#move to html settings
COMPUTERS_ON_PAGE = 3

@app.route('/')
def first():
    return render_template('index.html', name = request.method) 
    
    
@app.route('/qa/', methods=['POST', 'GET'])
def second():
    #getting computers id:
    if request.method == 'POST': 
        computers_id, computers_dss, dss_dict = filtered_computers_id(ALL_FILTERS, request.form)
        session['computers_id'], session['computers_dss'], session['dss_dict'] = computers_id, computers_dss, dss_dict
    else:        
        if 'computers_id' in session and 'computers_dss' in session and 'dss_dict' in session:
            computers_id, computers_dss, dss_dict = session['computers_id'], session['computers_dss'], session['dss_dict']
        else:
            computers_id, computers_dss, dss_dict  = db_queries.sorted_computers_id([], [])#list of all sorted computers
            session['computers_id'], session['computers_dss'], session['dss_dict'] = computers_id, computers_dss, dss_dict
    #print 'COMPUTERS_ID AND DSS:', zip(computers_id, computers_dss)
    #pagination test(if bad or wrong page)
    #print 'dss_dict', dss_dict
    last_page = int(round(len(computers_id) / COMPUTERS_ON_PAGE + 0.49))
    #TODO: rewrite
    try:
        page = int(request.args.get('page', '')) if 'page' in request.args else 1
    except ValueError:
        abort(404)
    if page > last_page or page < 1:
        abort(404)
 
    first_comp_index = (page-1)*COMPUTERS_ON_PAGE
    last_comp_index = min(page*COMPUTERS_ON_PAGE, len(computers_id))
    computers_id_on_page = computers_id[first_comp_index : last_comp_index]    
    computers_dss_on_page = computers_dss[first_comp_index : last_comp_index]
    print computers_id_on_page
    print computers_dss_on_page
    pretty_computers = pretty_data.small_computers(computers_id_on_page, computers_dss_on_page)

    return render_template('QandA.html', computers = pretty_computers, filters = ALL_FILTERS,
        current_page = page, pagination_pages = _get_pagination_pages(page, last_page), dss_dict = dss_dict)


def filtered_computers_id(filters, form):
    '''
    Gets parameters from request form, executes filters functions and finally returns filtered computers id
    '''
    print 'FORM:', form
    dss_values, cut_values = [], []
    for filt in filters:
        values_dict = dict((key,form[key]) for key in form if key.startswith(filt.name))
        print 'NAME: ', filt.name, "values_dict", values_dict
        if values_dict:
            dss, cut = filt.get_answers(values_dict)
            if dss: dss_values.append(dss)
            if cut: cut_values.append(cut)
    print 'VALUES:', dss_values, cut_values
    return db_queries.sorted_computers_id(cut_values, dss_values)


#TODO: move to pretty_data module
def _get_pagination_pages(current_page, last_page):
    pages = set((1,2,current_page-1,current_page,current_page+1,last_page-1,last_page))
    if 0 in pages: pages.remove(0)
    if last_page+1 in pages: pages.remove(last_page+1)
    pages = list(pages)
    pages.sort()
    pagination_pages = []
    for i in range(len(pages)-1):
        pagination_pages.append(pages[i])
        if pages[i]+1 != pages[i+1]:
            pagination_pages.append('...')
    pagination_pages.append(pages[-1])
    return pagination_pages

 
if __name__ == '__main__':
    #app.run(debug = True, host = '192.168.1.100', port = 80)
    app.run(debug = True)
    # controller = SQLController()
    # session = controller.create_sql_session()
    # components =  wc_RAM, wc_HD, wc_CPU, wc_OS, wc_ODD, wc_Screen, wc_Type, wc_Chipset
    # query = session.query(wc_Computer).join(*components)
    # print query.filter('wc_HD.id = 1 and wc_CPU.id > 2').all()
        