# -*- coding: utf-8 -*-
# ...
# available languages
# LANGUAGES = {
    # 'en': 'English',
    # 'es': 'Español'
# }

import os
basedir = os.path.abspath(os.path.dirname(__file__))

if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://sa:support@MSSQL-PYTHON-TEST'
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

# mail server settings
MAIL_SERVER = 'smtp3.hpe.com'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None
DOMAIN = 'hpe.com'

# administrator list
ADMINS = ['yi.li5@hpe.com']

# pagination
POSTS_PER_PAGE = 5

# initialize search
# WHOOSH_BASE = os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULTS = 50

AVATAR_URL = '/avatar' #The avatar url,default '/avatar/<text>/<width>'
AVATAR_RANGE = [0,512] #set avatar range to allow generate,if disallow,abort(404).Default [0,512]

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

# OPENID_PROVIDERS = [
    # {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    # {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    # {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    # {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    # {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]
