import os
import dj_database_url


# prod
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# prod
ALLOWED_HOSTS = ['djangohero.herokuapp.com/']


# prod
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.path.join(BASE_DIR, ''),
    }
}


# prod
DATABASES['default'] = dj_database_url.config()


# prod
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
