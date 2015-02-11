from django.test import TestCase

from rockit.core.tasks.association import register
from rockit.core.models import Association

class AssociationRegisterTestCase(TestCase):

    def test_it_should_register_association(self):

        data = {
            'name': 'test',
            #'namespace': 'rockit.test',
            #'entry': 'test'
        }

        register(**data);

        association = Association.objects.filter(**data)

        for a in Association.objects.all():
            print a.namespace

        self.assertEqual(len(association), 1)