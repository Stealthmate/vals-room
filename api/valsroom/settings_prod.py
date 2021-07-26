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
ALLOWED_HOSTS = [ 'localhost' ]
CORS_ALLOWED_ORIGINS = [ 'https://www.vals-room.top' ]
CSRF_TRUSTED_ORIGINS = [ 'www.vals-room.top' ]
