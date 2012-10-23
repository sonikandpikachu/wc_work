#coding: utf-8
'''
Created on Sep 18, 2012

@author: Pavel
'''
import operator

from sqlorm import *
from filters.settings import ALL_FILTERS
from filters import dss

from flask import Flask, render_template, request, abort

COMPUTERS_ON_PAGE = 10

app = Flask(__name__)
computer_components = None


@app.route('/')
def first():
    return render_template('index.html', name = request.method) 
    
    
@app.route('/qa/', methods=['POST', 'GET'])
def second():
    controller = SQLController()
    session = controller.create_sql_session()
    global computer_components
    #getting all computer_components for first query:
    if not computer_components:
        computers = session.query(wc_Computer).all()
        computer_components = [component for component in _get_all_components(session, computers) if component['comp'].price > 0]
        _norm_all_components(computer_components)
        computer_components = sorted(computer_components, key = lambda component: component['dss'],  reverse = True) 
    controller.close_sql_session()
    # if request.method == 'POST':
    #     computers = filter_computers(session, computers, ALL_FILTERS, request.form)#obrezalovka
    
    #pagination
    last_page = int(round(len(computer_components) / COMPUTERS_ON_PAGE + 0.49))
    print 'last_page', last_page, len(computer_components) 
    try:
        page = int(request.args.get('page', '')) if 'page' in request.args else 1
    except ValueError:
        abort(404)
    if page > last_page or page < 1:
        abort(404)
    page_components = computer_components[(page-1) * COMPUTERS_ON_PAGE : min(page * COMPUTERS_ON_PAGE, len(computer_components))]

    return render_template('QandA.html', computers = page_components, filters = ALL_FILTERS,
        current_page = page, pagination_pages = _get_pagination_pages(page, last_page))


def filter_computers(session, computers, filters, form):
    for f in filters:
        if f.name in form.keys():
            if f.cut_function: computers = f.cut_function(session, computers, form[f.name]) 
            if f.dss_function: f.dss_function(form[f.name])
    return computers


def _get_all_components(session, computers):
    components = []
    for computer in computers:
        battery = session.query(wc_Battery).filter_by(id = computer.id_wc_Battery).first()
        vga = session.query(wc_VGA).filter_by(id = computer.id_wc_VGA).first()
        hd = session.query(wc_HD).filter_by(id = computer.id_wc_HD).first()
        odd = session.query(wc_ODD).filter_by(id = computer.id_wc_ODD).first()
        type = session.query(wc_Type).filter_by(id = computer.id_wc_Type).first()
        chipset = session.query(wc_Chipset).filter_by(id = computer.id_wc_Chipset).first()
        screen = session.query(wc_Screen).filter_by(id = computer.id_wc_Screen).first()
        ram = session.query(wc_RAM).filter_by(id = computer.id_wc_RAM).first()
        os = session.query(wc_OS).filter_by(id = computer.id_wc_OS).first()
        cpu = session.query(wc_CPU).filter_by(id = computer.id_wc_CPU).first()        
        dictionary = {'battery': battery, 'vga' : vga, 'hd' : hd, 'odd' : odd, 'type' : type, 'chipset' : chipset,
                      'screen' : screen, 'ram' : ram, 'os' : os, 'cpu' : cpu, 'comp' : computer}
        dss_weight = dss.get_dss_weight(dictionary)
        dictionary['dss'] = dss_weight
        components.append(dictionary)

    
    return components


def _norm_all_components(components):
    minimum, maximum = min([component['dss'] for component in components]), max([component['dss'] for component in components])
    for component in components:
        component['dss'] = (component['dss'] - minimum) * 100/(maximum - minimum)
    return components


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

