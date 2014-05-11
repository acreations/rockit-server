from django.test import TestCase

from rockit.plugins.razberry import executors
from rockit.plugins.razberry import models


class MixesExecutorTestCase(TestCase):

    def setUp(self):
        self.executor = executors.MixesExecutor()
        self.holder = StubMixesHolder()

        models.Node.objects.create(device_id=1, device_type="PC Static Controller")
        models.Node.objects.create(device_id=2, device_type="Slave 1")
        models.Node.objects.create(device_id=3, device_type="Slave 2")

    def test_it_should_contains_correct_items_when_collecting(self):
        holder = self.executor.collect(self.holder)

        self.assertEquals(2, len(self.holder.get_then()))


class StubMixesHolder(object):

    then = list()

    def add_then(self, **kwargs):
        self.then.append(kwargs.get('identifier', 'NOT_SET'))

    def get_then(self):
        return self.then

    def mark_resolve_names(self):
        pass