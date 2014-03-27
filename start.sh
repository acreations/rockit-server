#!/bin/bash
set -e
DJANGODIR=/opt/apps/rockit-server
DJANGO_SETTINGS_MODULE=rockit.settings

LOGFILE=/var/log/gunicorn/guni-project.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3
# user/group to run as
USER=pi
GROUP=pi
cd /opt/apps/rockit-server
source /home/pi/ENV/bin/activate

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

test -d $LOGDIR || mkdir -p $LOGDIR
exec /home/pi/ENV/bin/gunicorn_django -w $NUM_WORKERS \
  --user=$USER --group=$GROUP --log-level=debug \
  --log-file=$LOGFILE -b 0.0.0.0:8001 2>>$LOGFILE