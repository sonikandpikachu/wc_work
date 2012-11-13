#coding: utf-8

import os
import re

import save_load as sl

def computers(pkl_folder, config):
    '''
    pkl_path - path to folder with .pkl path; config - path to .config file
    Retunrs dicts for each computer
    '''
    computers = []
    config_lines = _config_lines(config)
    for pkl in [pkl for pkl in os.listdir(pkl_folder) if pkl.endswith('.pkl')]:
        computers.append(_computer(sl.pickle_load(os.path.join(pkl_folder, pkl)), config_lines))
    return computers


def _config_lines(config):
    '''
    Reads lines from configs files, splits them into rus_name, names, parsers
    '''
    config_lines = []
    f = open(config)
    for line in f.xreadlines():
        rus_name, names, parsers, types =  line.split('|')[:4]
        config_line = {
            'rus_name' : rus_name.strip().replace('_', '.'),
            'names' : [name.strip().lower() for name in names.split(';')],
            'parsers' : [parser.strip() for parser in parsers.split(';')],
            'types' : [type.strip() for type in types.split(';')],
        }
        config_lines.append(config_line)
    return config_lines


def _parse(parser, value):
    repart = parser.split('$')[0].strip()
    parsed = re.findall(repart, value)
    index = int(parser.split('$')[1].strip()) if '$' in parser else 0
    return parsed[index]


def _computer(pkl_computer, config_lines):
    computer = {} 
    for line in config_lines:
        if line['rus_name'] in pkl_computer:
            for name, parser, type in zip(line['names'], line['parsers'], line['types']):
                computer[name] = _parse(parser, pkl_computer[line['rus_name']])
                if type == 'Boolean': computer[name] = True if '+' in computer[name] else False
    return computer
