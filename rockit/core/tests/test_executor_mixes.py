from django.test import TestCase

from rockit.core import executors 
from rockit.core import models
from rockit.core import holders

class MixesExecutorTestCase(TestCase):

    def setUp(self):
        self.holder = holders.MixesHolder(models.Association.objects.create(name = 'my_node', namespace='test'))
        self.executor = executors.MixesExecutor()

        self.executor.collect(self.holder)

    def test_it_should_be_able_to_collect_when(self):
        when = self.holder.get_content()['when'][0]

        self.assertEqual('my_node', when['association']['name'])

        self.assertEqual('when-button', when['items'][0]['identifier'])
        self.assertEqual('button', when['items'][0]['name'])
        self.assertEqual('when-schedule', when['items'][1]['identifier'])
        self.assertEqual('schedule', when['items'][1]['name'])

    def test_it_should_be_able_to_collect_then(self):
        then = self.holder.get_content()['then']
        self.assertEqual(0, len(then))

    def test_it_should_be_able_to_collect_final(self):
        final = self.holder.get_content()['final']
        self.assertEqual(0, len(final))