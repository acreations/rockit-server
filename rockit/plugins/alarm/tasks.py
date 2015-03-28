import celery
import datetime
import time

from celery import task
from celery.execute import send_task
from celery.signals import celeryd_init
from celery.signals import celeryd_after_setup
from celery.utils.log import get_task_logger

from croniter import croniter

from datetime import datetime
from datetime import timedelta

from django.core import management

from rockit.plugins.alarm import models

logger = get_task_logger(__name__)

@celeryd_after_setup.connect
def init(sender, instance, **kwargs):
    send_task('rockit.hey', ['alarm'], countdown=5)

@task(ignore_result=True)
def hey():
    logger = hey.get_logger()

    logger.debug('Received a hello back from rockit server')

    logger.debug('Trying to register alarm')

    send_task('rockit.register.association', kwargs={
        'name': 'Alarm',
        'namespace': 'rockit.plugins.alarm',
        'description': 'Alarm functionality for mixes',
        'entry': 'alarm'
    })

@task(name='alarm.settings')
def settings(holder):
    return holder

@task(name='alarm.mixes')
def mixes(holder):
    holder.add_when(**{ 'identifier': 'alarm', 'name': 'Alarm' })
    return holder

@task(name='alarm.mixes.details')
def mixes_details(identifier, holder):

    holder.add_post(**{
        'identifier': 'alarm',
        'type': 'alarm',
        'label': 'Alarm',
        'required': True
    })

    holder.add_post(**{
        'identifier': 'alarm-repeat',
        'type': 'checkbox',
        'label': 'Repeat',
        'required': False,
        'value': ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    })

    return holder

@task(name='alarm.mixes.when.create')
def mixes_then_create(uuid, criterias):

    if criterias:

        if criterias['alarm']:

            value = criterias['alarm']['value'].split(':')

            hour = value[0]
            minute = value[1]

            text = "%s %s * * *" % (minute, hour)
            cron = croniter(text, datetime.now())
            alarm = models.Alarm.objects.create(cron=text, date_next=cron.get_next(datetime))

        return alarm.id
    return None

@task(name='alarm.mixes.when.validate')
def mixes_when_validate(identifier, criterias, holder):

    if criterias:

        if criterias['alarm']:
            try:
                time.strptime(criterias['alarm']['value'], '%H:%M')
                return holder
            except ValueError:
                holder.add_error(criterias['alarm']['id'], 'Criteria value does not have a time format')
        else:
            holder.add_error(criterias['alarm']['id'], 'Unknown id')
    else:
        holder.add_error('alarm', 'Value must be provided')

    return holder

#@celery.decorators.periodic_task(run_every=timedelta(seconds=30), ignore_result=True, bind=True)
def check_alarm(self):
    logger.debug('Check for some task to run')

    management.call_command('alarm')