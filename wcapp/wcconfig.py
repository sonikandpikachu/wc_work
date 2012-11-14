'''
Created on Sep 18, 2012

@author: Pavel
settings for project. In production version need to move main part of settings to .config file
'''

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

#database configurations:
DATABASE = 'mysql://'
USERNAME = 'root'
PASSWORD = 'wcomp'
HOST = '127.0.0.1:3306'
DB_SCHEME = 'wc'
SQLALCHEMY_DATABASE_URI = DATABASE + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DB_SCHEME + '?charset=utf8'

print 'hi!'

app = Flask('wcapp')
app.config.from_object(__name__)
db = SQLAlchemy(app)
