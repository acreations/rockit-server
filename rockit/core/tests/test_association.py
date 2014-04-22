from django.test import TestCase

from rockit.core.models import Association

class AssociationTestCase(TestCase):

    def setUp(self):
        Association.objects.create(name='a', description='rockit description')

    def test_it_should_not_set_when_criteria_by_default(self):
        association = Association.objects.get(name='a')
        self.assertEqual(association.when_addable, False)

    def test_it_should_not_set_then_criteria_by_default(self):
        association = Association.objects.get(name='a')
        self.assertEqual(association.then_addable, False)