from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'pyconlt',  # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'pyconlt',
        'PASSWORD': '',
        'HOST': '',
        # Empty for localhost through domain sockets or
        #  '127.0.0.1' for localhost through TCP.
        'PORT': '',  # Set to empty string for default.
    }
}

SECRET_KEY = '8lu*6g0kdsjhiodshgfdsjkfgjkdsjgkhs2shmi1jcgihb*'

ALLOWED_HOSTS = ['127.0.0.1', 'marsaeigis.pythonanywhere.com', 'pycon.lt']

APPEND_SLASH = False

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'pyconlt', 'static')
print(STATIC_ROOT)

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'pyconlt', 'media')
print(MEDIA_ROOT)
