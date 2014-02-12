import requests

from celery.execute import send_task

from django.core.management.base import BaseCommand

from rockit.plugins.razberry import models
from rockit.plugins.razberry.parser import RazberryParser

class Command(BaseCommand):
    args = 'timestamp'
    help = 'Get data from razberry server'

    def handle(self, *args, **options):
        assert (len(args) == 1 or len(args) == 0)

        parser = RazberryParser()

        t = 0

        if args:
            t = args[0]

        r = requests.get('http://192.168.1.203:8083/ZWaveAPI/data/%s' % t)

        ids = parser.parseDevices(r.json()['devices'])

        for device_id in ids:
            node = models.Node.objects.get(device_id=device_id)

            create = send_task("rockit.register.node", args=['rockit.plugins.razberry', node.device_id])
            result = create.wait()