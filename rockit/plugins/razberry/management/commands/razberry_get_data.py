from celery.execute import send_task

from django.core.management.base import BaseCommand

from rockit.plugins.razberry import models
from rockit.plugins.razberry.parsers import RazberryParser
from rockit.plugins.razberry.services import RazberryService

class Command(BaseCommand):
    args = 'timestamp'
    help = 'Get data from razberry server'

    def handle(self, *args, **options):
        assert (len(args) == 1 or len(args) == 0)

        parser  = RazberryParser()
        service = RazberryService()

        if args:
            data = service.data(args[0])
        else:
            data = service.data()

        ids = parser.parseDevices(data['devices'])

        for device_id in ids:
            node = models.Node.objects.get(device_id=device_id)

            create = send_task("rockit.register.node", args=['rockit.plugins.razberry', node.device_id])
            result = create.wait()