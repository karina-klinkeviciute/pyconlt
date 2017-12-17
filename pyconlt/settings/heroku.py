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



# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())

# import dj_database_url
# db_from_env = dj_database_url.config(conn_max_age=500)
# DATABASES['default'].update(db_from_env)
DEBUG = False

# MEDIA_URL = '/static/'
#
# MEDIA_ROOT = os.path.join(BASE_DIR, 'pyconlt', 'media')

MEDIA_ROOT = os.path.join(BASE_DIR, 'var', 'www', 'static')
