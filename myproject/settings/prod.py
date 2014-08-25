"""
PROD settings
Prod environment is set using DJANGO_SETTINGS_MODULE

"""

from base import *
import os
import dj_database_url


BASE_DIR = os.path.dirname(os.path.abspath(__file__))[:-9] # chop off "settings/"

DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['djangohero.herokuapp.com']


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.path.join(BASE_DIR, ''),
    }
}

DATABASES['default'] = dj_database_url.config()


STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
