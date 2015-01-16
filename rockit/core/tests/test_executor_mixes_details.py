from django.test import TestCase

from rockit.core import executors
from rockit.core import models
from rockit.core import holders

class MixesExecutorTestCase(TestCase):

    def setUp(self):
        self.holder = holders.MixesDetailsHolder()
        self.executor = executors.MixesExecutor()

    def test_it_should_collect_details_about_when_schedule(self):
        self.executor.collect_details('when-schedule', self.holder)
        self._has_following_in_response('rockit-schedule', 'schedule', 'schedule')

    def test_it_should_collect_details_about_when_alarm(self):
        self.executor.collect_details('when-alarm', self.holder)
        self._has_following_in_response('rockit-alarm', 'alarm', 'alarm')

    def test_it_should_return_empty_action_when_trying_to_get_invalid(self):
        self.executor.collect_details('CRAPPY-FUNCTION', self.holder)

        self.assertEquals(0, len(self.holder.get_content()['actions']))

    def _has_following_in_response(self, identifier, typed, label, required=True, max_length=False):
        data = self.holder.get_content()['actions']['POST']

        self.assertEquals(1, len(data))
        self.assertTrue(identifier in data)

        container = data[identifier]

        self.assertEquals(typed, container['type'])
        self.assertEquals(label, container['label'])
        self.assertEquals(required, container['required'])

        if max_length:
            self.assertEquals(max_length, container['max_length'])



