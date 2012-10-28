#coding: utf-8
'''
Created on Sep 18, 2012

@author: Pavel
'''
import operator

from sqlorm import *
from flask import Flask, render_template, request, abort, redirect, url_for

from filters.settings import ALL_FILTERS
from filters import dss
import pretty_data


#move to html settings
COMPUTERS_ON_PAGE = 10

app = Flask(__name__)

@app.route('/')
def first():
    return render_template('index.html', name = request.method) 
    
    
@app.route('/qa/', methods=['POST', 'GET'])
def second():
    #getting all computer_components for first query:
    computers = filtered_computers(ALL_FILTERS, request.form) if request.method == 'POST' else filtered_computers(ALL_FILTERS)
    #pagination test(if bad or wrong page)
    last_page = int(round(len(computers) / COMPUTERS_ON_PAGE + 0.49))
    try:
        page = int(request.args.get('page', '')) if 'page' in request.args else 1
    except ValueError:
        abort(404)
    if page > last_page or page < 1:
        abort(404)

    computers_on_page = computers[(page-1) * COMPUTERS_ON_PAGE : min(page * COMPUTERS_ON_PAGE, len(computers))]

    return render_template('QandA.html', computers = computers_on_page, filters = ALL_FILTERS,
        current_page = page, pagination_pages = _get_pagination_pages(page, last_page))


def filtered_computers(filters, form = None):
    '''
    1. Setting new dss values bases on answers
    2. Getting filters string and executes filtering
    Returns filtered computers 
    '''
    controller = SQLController()
    session = controller.create_sql_session()

    components =  wc_RAM, wc_HD, wc_CPU, wc_OS, wc_ODD, wc_Screen, wc_Type, wc_Chipset#, wc_Battery, wc_Color,  wc_Audio, wc_VGA

    cut_strings = []
    if form:
        for f in (f for f in filters if f.values):
            selected_values = tuple(value for value in f.values if f.name + '_' + value in form)
            f.selected_values = selected_values
            if f.dss_function: f.dss_function(selected_values)
            if f.cut_function and f.cut_function(selected_values): cut_strings.append(f.cut_function(selected_values))
    filter_string = ' and '.join(cut_strings) if cut_strings else None
    print filter_string

    query = session.query(wc_Computer).join(*components)
    computers = query.filter(filter_string).all() if filter_string else query.all() #getting filtered computers
    for comp in computers: comp.dss = dss.dss_weight(comp) #counting theirs dss
    computers.sort(key = lambda comp: comp.dss, reverse = True) #sorting by dss
    computers = [pretty_data.small_computer(comp) for comp in computers]      
    controller.close_sql_session()
    return computers

#move to comp_db module
def _norm_all_components(components):
    minimum, maximum = min([component['dss'] for component in components]), max([component['dss'] for component in components])
    for component in components:
        component['dss'] = (component['dss'] - minimum) * 100/(maximum - minimum)
    return components

#move to 'pretty html' module
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
    app.run(debug = True)
    # controller = SQLController()
    # session = controller.create_sql_session()
    # components =  wc_RAM, wc_HD, wc_CPU, wc_OS, wc_ODD, wc_Screen, wc_Type, wc_Chipset
    # query = session.query(wc_Computer).join(*components)
    # print query.filter('wc_HD.id = 1 and wc_CPU.id > 2').all()
        