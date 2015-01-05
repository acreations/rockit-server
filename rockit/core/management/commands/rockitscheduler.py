import logging
import pytz
import requests

from croniter import croniter
from datetime import datetime
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand

from rockit.core import models

class Command(BaseCommand):
    '''
    Rockit scheduler checks for actions to be triggered based on current time
    '''
    help = 'Run action based on current time'

    logger = logging.getLogger(__name__)
    tmzone = pytz.timezone(settings.TIME_ZONE)

    def handle(self, *args, **options):
        '''
        Handle it
        '''

        schedules = models.Schedule.objects.all()

        for schedule in schedules:

            if self.has_triggered_schedule(schedule):
                self.logger.info('Run action for this schedule')

                cid = "devices.3.instances.0.commandClasses.37"
                val = "on"

                node = models.Node.objects.filter(uuid="be174f43-c616-4b31-a64d-8beea39688bc")

                print node.name

                #schedule.save()

            else:
                self.logger.info('Schedule has not been triggered yet')

            #if schedule.date_modified < cron.get_next(datetime):
            #    self.logger.info('Cron passed, trigger action')



        print 'Check in database if some date has been passed'
        print 'Get the action from db'
        print 'Get the association for action'
        print 'Trigger a celery task with action data'

    def has_triggered_schedule(self, schedule):
        '''
        Check if schedule has beed triggered based on cron setting
        '''

        cron = croniter(schedule.cron, schedule.date_modified)
        next = cron.get_next(datetime)
        now  = self.tmzone.localize(datetime.now())

        return now > next