from django.test import TestCase

from rockit.core.tasks.association import register
from rockit.core.models import Association

class AssociationRegisterTestCase(TestCase):

    def setUp(self):

        self.data = {
            'name': 'test',
            'namespace': 'rockit.test',
            'entry': 'test'
        }

    def test_it_should_register_association(self):

        register(**self.data);

        association = Association.objects.filter(**self.data)

        self.assertEqual(len(association), 1)

    def test_it_should_not_get_any_registration_since_validation_fail_with_no_name(self):

        self.data.pop('name', None)

        register(**self.data)

        association = Association.objects.filter(**self.data)

        self.assertEqual(len(association), 0)

    def test_it_should_not_get_any_registration_since_validation_fail_with_no_namespace(self):

        self.data.pop('namespace', None)

        register(**self.data)

        association = Association.objects.filter(**self.data)

        self.assertEqual(len(association), 0)

    def test_it_should_not_get_any_registration_since_validation_fail_with_no_entry(self):

        self.data.pop('entry', None)

        register(**self.data)

        association = Association.objects.filter(**self.data)

        self.assertEqual(len(association), 0)