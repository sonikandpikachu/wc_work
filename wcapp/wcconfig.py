'''
Created on Sep 18, 2012

@author: Pavel
settings for project. In production version need to move main part of settings to .config file
'''

from flask import Flask

from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.redis import init_redis

#database configurations:
DATABASE = 'mysql://'
USERNAME = 'root'
PASSWORD = 'root'
HOST = '127.0.0.1:3306'
DB_SCHEME = 'wc'
SQLALCHEMY_DATABASE_URI = DATABASE + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DB_SCHEME + '?charset=utf8'

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'whatcompute'
MAIL_PASSWORD = 'ilovecloude'

# administrator list
ADMINS = ['whatcompute@gmail.com']

from local_config import *

#flask configurations:
app = Flask('wcapp')
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'  # test
app.config.from_object(__name__)

db = SQLAlchemy(app)
mail = Mail(app)
redis = init_redis(app)

if not app.debug:
    import logging
    from logging.handlers import SMTPHandler
    credentials = None
    if MAIL_USERNAME or MAIL_PASSWORD:
        credentials = (MAIL_USERNAME, MAIL_PASSWORD)
    mail_handler = SMTPHandler((MAIL_SERVER, MAIL_PORT), 'no-reply@' + MAIL_SERVER, ADMINS, 'wcomp failure', credentials)
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)

if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('tmp/wcomp.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('-- WCOMP Startup --')
