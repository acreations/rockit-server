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

        #self.set_action()

        for schedule in schedules:
            self.logger.debug('Run then actions for this schedule %s' % schedule.id)

            actions = models.ActionThen.objects.filter(holder=schedule.action)

            # Get then actions associated with this action
            for action in actions:

                if action.target:

                    update_time = datetime.now()
                    update = send_task("%s.node.command.update.value" % action.target.association.entry, kwargs={
                        'identifier': action.target.aid,
                        'command_id': action.command,
                        'value': self.normalize_value(action.value)
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

    def set_action(self):
        action = models.Action.objects.get(pk=2)

        action.name = "test2"
        action.description = "test description2"

        action.save()

        node = models.Node.objects.get(pk=2)

        then, create = models.ActionThen.objects.get_or_create(target=node, holder=action)
        then.command = "devices.3.instances.0.commandClasses.37"
        then.value = "true"

        then.save()

