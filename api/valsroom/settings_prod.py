from valsroom.settings import *
from os import environ

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'valsroom',
        'USER': environ['VALSROOM_DB_USER'],
        'PASSWORD': environ['VALSROOM_DB_PASSWORD'],
        'HOST': environ['VALSROOM_DB_HOST'],
        'PORT': environ['VALSROOM_DB_PORT'],
    }
}
DEBUG = False
ALLOWED_HOSTS = [ 'stealthmate.github.io' ]