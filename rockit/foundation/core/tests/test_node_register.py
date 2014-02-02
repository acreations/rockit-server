from django.test import TestCase

from rockit.foundation.core.tasks import register

from rockit.foundation.core.models import Node
from rockit.foundation.core.models import Association

class NodeRegisterTestCase(TestCase):

    def setUp(self):
        self.association = Association.objects.create(name = 'my_node')

    def test_it_should_not_add_if_association_is_empty(self):
        aid = 'node_empty_association'

        r = register(None, aid)
        
        self.assertEqual(r, False)
        self.assertEqual(Node.objects.filter(aid=aid).count(), 0)

    def test_it_should_not_add_if_aid_is_empty(self):
        r = register(self.association, None)
        
        self.assertEqual(r, False)
        self.assertEqual(Node.objects.filter(association=self.association).count(), 0)

    def test_it_should_not_add_if_aid_and_association_is_empty(self):
        self.assertEqual(register(None, None), False)


    def test_it_should_successfully_register_node(self):
        aid = 'node_success'

        r = register(self.association, aid)

        self.assertEqual(r, True)
        self.assertEqual(Node.objects.filter(aid=aid).count(), 1)

    def test_it_should_not_register_same_node_twice(self):
        aid = 'node_success'

        r = register(self.association, aid)

        self.assertEqual(r, True)
        self.assertEqual(Node.objects.filter(aid=aid).count(), 1)

        r = register(self.association, aid)

        self.assertEqual(r, False)
        self.assertEqual(Node.objects.filter(aid=aid).count(), 1)

    def test_it_should_generate_unique_uuid(self):
        size = 10

        for i in range(size):
            self.assertEqual(register(self.association, 'node_%s' % i), True)

        nodes = Node.objects.all()

        self.assertEqual(nodes.count(), size)

        unique = dict()

        for node in nodes:
            self.assertEqual(node.uuid in unique, False)
            unique[node.uuid] = node.uuid
