from django.test import TestCase

from rockit.foundation.core.models import Association

class AssociationTestCase(TestCase):

	def setUp(self):
		Association.objects.create(name='a', description='rockit description')

	def test_it_should_not_be_addable_by_default(self):
		"""An association should not be addable by default"""
		association = Association.objects.get(name='a')
		self.assertEqual(association.addable, False)