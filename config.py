import os 

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG = True

    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'f3ua84fd'
    MYSQL_DB = 'myflaskapp'
    MYSQL_CURSORCLASS = 'DictCursor'
 
