from valsroom.settings import *
from os import environ

SECRET_KEY = environ['DJANGO_SECRET_KEY']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'valsroom',
        'USER': environ['PGUSER'],
        'PASSWORD': environ['PGPASSWORD'],
        'HOST': environ['PGHOST'],
        'PORT': environ['PGPORT'],
    }
}
DEBUG = False
ALLOWED_HOSTS = [ 'www.vals-room.top' ]
