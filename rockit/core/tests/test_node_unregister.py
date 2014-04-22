from django.test import TestCase

from rockit.core.tasks import unregister

from rockit.core.models import Node
from rockit.core.models import Association

class NodeRegisterTestCase(TestCase):

    def setUp(self):
        self.association = Association.objects.create(name = 'my_node')

        self.node = Node.objects.get_or_create(uuid='my_uuid', association=self.association, aid='my_aid')

    def test_it_should_not_be_able_to_unregister_invalid_uuid(self):
        self.assertEqual(unregister('invalid_uuid'), False)

    def test_it_should_not_be_able_to_unregister_empty_uuid(self):
        self.assertEqual(unregister(None), False)

    def test_it_should_successfully_unregister_valid_uuid(self):
        self.assertEqual(unregister('my_uuid'), True)
        self.assertEqual(Node.objects.filter(uuid='my_uuid').count(), 0)