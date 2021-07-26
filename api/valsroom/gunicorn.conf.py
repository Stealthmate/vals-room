import multiprocessing
from os import environ

bind = f'0.0.0.0:{environ["VALSROOM_PORT"]}'
workers = 1
loglevel = 'info'
accesslog='/var/log/app/access.log'
errorlog='/var/log/app/error.log'
