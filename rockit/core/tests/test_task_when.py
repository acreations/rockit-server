from django.test import TestCase

from rockit.core import holders
from rockit.core import models
from rockit.core import tasks

class TaskWhenTestCase(TestCase):

    def test_it_should_be_able_to_call_task(self):
        holder = holders.WhenHolder(models.Association.objects.create(name = 'my_node', namespace='test'))
        holder = tasks.when(holder)

        self.assertNotEqual(0, len(holder.get_content()))
