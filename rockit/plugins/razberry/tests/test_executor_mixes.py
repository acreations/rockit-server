from django.test import TestCase

from rockit.plugins.razberry import executors
from rockit.plugins.razberry import models

class MixesExecutorTestCase(TestCase):

    def setUp(self):
        self.executor = executors.MixesExecutor()

        models.Node.objects.create(device_id=1, device_type="PC Static Controller")
        models.Node.objects.create(device_id=2, device_type="Slave 1")
        models.Node.objects.create(device_id=3, device_type="Slave 2")
