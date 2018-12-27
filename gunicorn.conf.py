import os
import multiprocessing

current_path = os.path.dirname(os.path.abspath(__file__))
bind = '0.0.0.0:8080'
workers = multiprocessing.cpu_count() * 2 + 1
threads = workers
name = 'inbox'
env = 'DJANGO_SETTINGS_MODULE=casepro.settings'
proc_name = 'inbox'
default_proc_name = proc_name
chdir = current_path
loglevel = 'info'
accesslog = '/tmp/stdout'
errorlog = '/tmp/stderr'
timeout = 120
