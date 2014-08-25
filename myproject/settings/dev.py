"""
DEV settings
Dev environment is set using DJANGO_SETTINGS_MODULE

"""

from base import *
import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = True

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tbone00',                      
        'USER': 'tbone00',
        'PASSWORD': '',
        'HOST': '',
    }
}
