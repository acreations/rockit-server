import celery
import datetime
import time

from celery import task
from celery.execute import send_task
from celery.utils.log import get_task_logger

from croniter import croniter

from datetime import datetime
from datetime import timedelta

from django.core import management

from rockit.plugins.schedule import models

logger = get_task_logger(__name__)

@task(name='schedule.settings')
def settings(holder):
    return holder

@task(name='schedule.mixes')
def mixes(holder):
    holder.add_when(**{ 'identifier': 'schedule', 'name': 'Schedule' })
    return holder

@task(name='schedule.mixes.details')
def mixes_details(identifier, holder):

    holder.add_post(**{
        'identifier': 'schedule',
        'type': 'schedule',
        'label': 'schedule',
        'required': True
    })

    holder.add_post(**{
        'identifier': 'schedule-repeat',
        'type': 'checkbox',
        'label': 'Repeat',
        'required': False,
        'value': ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    })

    return holder

@task(name='schedule.mixes.when.create')
def mixes_then_create(uuid, criterias):

    if criterias:

        if criterias['schedule']:

            value = criterias['schedule']['value'].split(':')

            hour = value[0]
            minute = value[1]

            text = "%s %s * * *" % (minute, hour)
            cron = croniter(text, datetime.now())
            schedule = models.schedule.objects.create(cron=text, date_next=cron.get_next(datetime))

        return schedule.id
    return None

@task(name='schedule.mixes.when.validate')
def mixes_when_validate(identifier, criterias, holder):

    if criterias:

        if criterias['schedule']:
            try:
                time.strptime(criterias['schedule']['value'], '%H:%M')
                return holder
            except ValueError:
                holder.add_error(criterias['schedule']['id'], 'Criteria value does not have a time format')
        else:
            holder.add_error(criterias['schedule']['id'], 'Unknown id')
    else:
        holder.add_error('schedule', 'Value must be provided')

    return holder

@celery.decorators.periodic_task(run_every=timedelta(seconds=30), ignore_result=True, bind=True)
def check_schedule(self):
    logger.debug('Check for some task to run')

    management.call_command('schedule')