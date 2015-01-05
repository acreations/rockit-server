import logging
import pytz
import requests

from celery.execute import send_task
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
                self.logger.debug('Run action for this schedule')

                node = self.get_node("be174f43-c616-4b31-a64d-8beea39688bc")

                if node:

                    update = send_task("%s.node.command.update.value" % node.association.entry, kwargs={
                        'identifier': node.aid,
                        'command_id': "devices.3.instances.0.commandClasses.37",
                        'value': self.normalize_value("true")
                        })
                    value = update.wait(timeout=30)

                    if value is not None:
                        self.logger.debug('Successful update value ... saving')

                        # schedule.save()
                    else:
                        self.logger.warn('Failed to set value of node %s' % node.uuid)
            else:
                self.logger.info('Schedule has not been triggered yet')

    def get_node(self, uuid):
        try:
            return models.Node.objects.get(uuid=uuid)
        except:
            self.logger.error('Could not find node with uuid %s' % uuid)
        return None

    def has_triggered_schedule(self, schedule):
        '''
        Check if schedule has beed triggered based on cron setting
        '''

        cron = croniter(schedule.cron, schedule.date_modified)
        next = cron.get_next(datetime)
        now  = self.tmzone.localize(datetime.now())

        return now > next

    def normalize_value(self, value):
        if isinstance(value, bool):
            return bool(value)

        return value