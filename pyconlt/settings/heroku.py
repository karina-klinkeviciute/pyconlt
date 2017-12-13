from .base import *

import os

DB_PASSWORD = os.environ['DB_PASSWORD']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'pyconlt',  # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'pyconlt',
        'PASSWORD': DB_PASSWORD,
        'HOST': 'localhost',
        # Empty for localhost through domain sockets or
        #  '127.0.0.1' for localhost through TCP.
        'PORT': '',  # Set to empty string for default.
    }
}

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['127.0.0.1', 'pyconlt.herokuapp.com']

DEBUG = False
