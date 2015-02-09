import logging

from celery.execute import send_task
from croniter import croniter
from datetime import datetime
from datetime import timedelta
from django.core.management.base import BaseCommand

from rockit.plugins.alarm import models
from rockit.plugins.alarm import tasks

class Command(BaseCommand):
    '''
    Rockit scheduler checks for actions to be triggered based on current time
    '''
    help = 'Run action based on current time'

    logger = logging.getLogger(__name__)

    def handle(self, *args, **options):
        '''
        Handle it
        '''
        alarms = models.Alarm.objects.filter(date_next__lte=(datetime.now() + timedelta(seconds=25)))

        for alarm in alarms:
            self.logger.debug('Run then actions for this alarm %s' % alarm.date_next)

            send_task("rockit.notify.when", ['alarm', alarm.id])

            cron = croniter(alarm.cron, alarm.date_next)

            alarm.date_next = cron.get_next(datetime)
            alarm.save()

