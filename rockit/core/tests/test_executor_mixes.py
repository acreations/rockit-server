from django.test import TestCase

from rockit.core import executors 
from rockit.core import models
from rockit.core import holders

class MixesExecutorTestCase(TestCase):

    def setUp(self):
        self.holder = holders.MixesHolder(models.Association.objects.create(name = 'my_node', namespace='test'))
        self.executor = executors.MixesExecutor()

    def test_it_should_be_able_to_collect(self):
        self.executor.collect(self.holder)

        data = self.holder.get_content()['data']

        self.assertEqual(1001, data[0]['identifier'])
        self.assertEqual('button', data[0]['name'])
        self.assertEqual(1002, data[1]['identifier'])
        self.assertEqual('schedule', data[1]['name'])