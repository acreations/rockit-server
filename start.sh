#!/bin/bash
set -e
DJANGODIR=/opt/apps/rockit-server
DJANGO_SETTINGS_MODULE=rockit.settings

LOGFILE=/opt/apps/logs/gunicorn/guni-project.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=1
# user/group to run as
USER=pi
GROUP=pi
cd /opt/apps/rockit-server

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

pip install -r requirements/developement

test -d $LOGDIR || mkdir -p $LOGDIR
exec /usr/local/bin/gunicorn_django -w $NUM_WORKERS \
  --user=$USER --group=$GROUP --log-level=debug \
  --log-file=$LOGFILE -b 0.0.0.0:8001 2>>$LOGFILE