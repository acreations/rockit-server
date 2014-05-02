from django.test import TestCase

from rockit.core.executors import SettingsExecutor
from rockit.core.holders import SettingsHolder
from rockit.core.models import Setting

class SettingsExecutorTestCase(TestCase):

    def setUp(self):
        self.holder = SettingsHolder()
        self.executor = SettingsExecutor()

    def test_it_should_be_able_to_collect(self):
        Setting.objects.create(name='S01', value='VALUE_01')
        Setting.objects.create(name='S02', value='VALUE_02')

        self.executor.collect(self.holder)

        data = self.holder.get_content()

        self.assertEqual(True, 'S01' in str(data))
        self.assertEqual(True, 'VALUE_01' in str(data))
        self.assertEqual(True, 'S02' in str(data))
        self.assertEqual(True, 'VALUE_02' in str(data))