from valsroom.settings import *
from os import environ

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'valsroom',
        'USER': environ['PGUSER'],
        'PASSWORD': environ['PGPASSWORD'],
        'HOST': 'postgres',
        'PORT': 5432,
    }
}
DEBUG = False
ALLOWED_HOSTS = [ 'stealthmate.github.io' ]
