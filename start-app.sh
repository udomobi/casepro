#!/bin/sh
cd $WORKDIR
python3.6 manage.py migrate --noinput
python3.6 manage.py collectstatic --noinput
python3.6 manage.py compress --extension=.haml,.html
python3.6 manage.py compilemessages

gunicorn casepro.wsgi --log-config gunicorn-logging.conf -c gunicorn.conf.py --workers 4
