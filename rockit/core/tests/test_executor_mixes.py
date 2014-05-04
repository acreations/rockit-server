from django.test import TestCase

from rockit.core import executors 
from rockit.core import models
from rockit.core import holders

class MixesExecutorTestCase(TestCase):

    def setUp(self):
        self.holder = holders.MixesHolder(models.Association.objects.create(name = 'my_node', namespace='test'))
        self.executor = executors.MixesExecutor()

    def test_it_should_be_able_to_collect_when(self):
        self.executor.collect(self.holder)

        when = self.holder.get_content()['data']['when'][0]

        self.assertEqual('my_node', when['association']['name'])

        self.assertEqual(1001, when['items'][0]['identifier'])
        self.assertEqual('button', when['items'][0]['name'])
        self.assertEqual(1002, when['items'][1]['identifier'])
        self.assertEqual('schedule', when['items'][1]['name'])