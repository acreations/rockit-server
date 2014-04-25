from django.core.management.base import BaseCommand

class Command(BaseCommand):
    '''
    Rockit scheduler checks for actions to be triggered based on current time
    '''
    help = 'Run action based on current time'

    def handle(self, *args, **options):
        print 'works'