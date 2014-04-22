from django.test import TestCase

from rockit.core.models import NodeCategory

class NodeCategoryTestCase(TestCase):

    def setUp(self):
        NodeCategory.objects.create(name='test')

    def test_it_should_have_black_as_default_color(self):
        result = NodeCategory.objects.get(name='test')
        self.assertEqual(result.color, "#000000")