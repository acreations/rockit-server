from django.test import TestCase

from rockit.core import executors 
from rockit.core import models
from rockit.core import holders

class MixesExecutorTestCase(TestCase):

    def setUp(self):
        self.holder = holders.MixesDetailsHolder()
        self.executor = executors.MixesExecutor()

    def test_it_should_collect_details_about_when_button(self):
        self.executor.collect_details('when-button', self.holder)

        data = self.holder.get_content()['actions']['POST']

        self.assertEquals(1, len(data))
        self.assertTrue('name' in data)

        name = data['name']

        self.assertEquals('string', name['type'])
        self.assertEquals('name', name['label'])
        self.assertEquals(True, name['required'])
    
    def test_it_should_return_empty_action_when_trying_to_get_invalid(self):
        self.executor.collect_details('CRAPPY-FUNCTION', self.holder)

        self.assertEquals(0, len(self.holder.get_content()['actions']))