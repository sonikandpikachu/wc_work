'''
Created on Sep 18, 2012

@author: Pavel
settings for project. In production version need to move main part of settings to .config file
'''

import os

from flask.ext.mail import Mail
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

#database configurations:
DATABASE = 'mysql://'
USERNAME = 'root'
PASSWORD = 'wcomp'
HOST = '127.0.0.1:3307'
DB_SCHEME = 'wc'
SQLALCHEMY_DATABASE_URI = DATABASE + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DB_SCHEME + '?charset=utf8'


# administrator list
ADMINS = ['whatcompute@gmail.com']


print 'hi!'

#flask configurations:
app = Flask('wcapp')
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'  # test
app.config.from_object(__name__)
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'whatcompute',
    MAIL_PASSWORD = 'ilovecloude'
)
db = SQLAlchemy(app)
mail = Mail(app)
