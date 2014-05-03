from django.core.management.base import BaseCommand

from croniter import croniter

from rockit.core import models

class Command(BaseCommand):
    '''
    Rockit scheduler checks for actions to be triggered based on current time
    '''
    help = 'Run action based on current time'

    def handle(self, *args, **options):
        '''
        Handle it
        '''




        #print 'Check in database if some date has been passed'
        #print 'Get the action from db'
        #print 'Get the association for action'
        #print 'Trigger a celery task with action data'