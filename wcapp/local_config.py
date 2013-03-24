DATABASE = 'mysql://'
USERNAME = 'root'
PASSWORD = 'root'
HOST = '127.0.0.1:3306'
DB_SCHEME = 'wc'
SQLALCHEMY_DATABASE_URI = DATABASE + USERNAME + ':' + PASSWORD + '@' + HOST +\
                          '/' + DB_SCHEME + '?charset=utf8'
