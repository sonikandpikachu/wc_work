'''
Created on Sep 18, 2012

@author: Pavel
settings for project. In production version need to move main part of settings to .config file
'''

from flask import Flask

from flask.ext.redis import init_redis
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.redis import init_redis


#database configurations:
DATABASE = 'mysql://'
USERNAME = 'root'
PASSWORD = '123'
HOST = '127.0.0.1:3306'
DB_SCHEME = 'wc'
SQLALCHEMY_DATABASE_URI = DATABASE + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DB_SCHEME + '?charset=utf8'

UPDATE_DB_SCHEME = 'update_wc'
UPDATE_SQLALCHEMY_DATABASE_URI = DATABASE + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + UPDATE_DB_SCHEME + '?charset=utf8'
IS_UPDATE = False

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'whatcompute'
MAIL_PASSWORD = 'ilovecloude'
DEFAULT_MAIL_SENDER = 'some_user@gmail.com'

# administrator list
ADMINS = ['whatcompute@gmail.com']

from local_config import *

if IS_UPDATE:
    DB_SCHEME = UPDATE_DB_SCHEME
    SQLALCHEMY_DATABASE_URI = UPDATE_SQLALCHEMY_DATABASE_URI

#flask configurations:
app = Flask('wcapp')
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'  # test
app.config.from_object(__name__)

PROM = False

db = SQLAlchemy(app)
mail = Mail(app)
redis = init_redis(app)

import logging
from logging.handlers import RotatingFileHandler
file_handler = RotatingFileHandler('tmp/wcomp.log', 'a', 1 * 1024 * 1024, 10)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
app.logger.info('-- WCOMP Startup --')
