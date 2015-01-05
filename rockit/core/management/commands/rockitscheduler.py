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

    def handle(self, *args, **options):
        '''
        Handle it
        '''
        schedules = models.Schedule.objects.filter(date_next__lte=datetime.now())

        for schedule in schedules:

            self.logger.info('Run action for this schedule')

            node = self.get_node("be174f43-c616-4b31-a64d-8beea39688bc")

            if node:

                update_time = datetime.now()
                update = send_task("%s.node.command.update.value" % node.association.entry, kwargs={
                    'identifier': node.aid,
                    'command_id': "devices.3.instances.0.commandClasses.37",
                    'value': self.normalize_value("true")
                    })
                value = update.wait(timeout=30)

                if value is not None:
                    self.logger.debug('Successful update value ... saving')

                    cron = croniter(schedule.cron, update_time)

                    schedule.date_next = cron.get_next(datetime)
                    schedule.save()

                    self.logger.info('Updated next schedule to %s' % schedule.date_next)
                else:
                    self.logger.warn('Failed to set value of node %s' % node.uuid)

    def get_node(self, uuid):
        try:
            return models.Node.objects.get(uuid=uuid)
        except:
            self.logger.error('Could not find node with uuid %s' % uuid)
        return None

    def normalize_value(self, value):
        if isinstance(value, bool):
            return bool(value)

        return value