from django.test import TestCase

from rockit.core import holders
from rockit.core import models
from rockit.core import tasks

class TaskMixesTestCase(TestCase):

    def test_it_should_be_able_to_call_task(self):
        holder = holders.MixesHolder(models.Association.objects.create(name = 'my_node', namespace='test'))
        holder = tasks.mixes(holder)

        self.assertNotEqual(0, len(holder.get_content()))

    def test_it_should_be_able_to_call_mixes_detail_task(self):
        holder = holders.MixesDetailsHolder()
        holder = tasks.mixes_details('when-button', holder)

        self.assertTrue('POST' in holder.get_content()['actions'])