from django.test import TestCase

from rockit.core import holders
from rockit.core import tasks

class TaskSettingsTestCase(TestCase):

    def test_it_should_be_able_to_call_task(self):
        holder = holders.SettingsHolder()
        holder = tasks.settings(holder)

        self.assertNotEqual(0, len(holder.get_content()))
