import logging
import json
import os
import requests

from django.test import TestCase

from mock import patch

from rockit.plugins.razberry import constants
from rockit.plugins.razberry import models
from rockit.plugins.razberry.services import RazberryService

class ParsingTestCase(TestCase):

    logger = logging.getLogger(__name__)

    def setUp(self):
        self.service = RazberryService()

        models.Setting.objects.create(name=constants.SETTING_SERVER_ADDRRESS, value='localhost')

    def test_it_should_normalize_namespace_correctly(self):
        namespace = 'devices.3.instances.0.commandClasses.37.data'
        normalize = self.service.normalize(namespace)

        self.assertEqual('devices[3].instances[0].commandClasses[0x25].data', normalize)

    def test_it_should_normalize_even_when_no_index_are_provided(self):
        namespace = 'devices.instances.commandClasses.data'
        self.assertEqual(namespace, self.service.normalize(namespace))

        namespace = 'test'
        self.assertEqual(namespace, self.service.normalize(namespace))

    def test_it_should_return_none_if_namespace_is_empty(self):
        self.assertEqual(None, self.service.normalize(None))

    def test_it_should_return_none_if_server_not_set(self):
        models.Setting.objects.all().delete()

        self.assertEqual(None, self.service.data())
        self.assertEqual(None, self.service.retrieve(None))
        self.assertEqual(None, self.service.update(None, None))
        self.assertEqual(None, self.service.update(None, ""))
        self.assertEqual(None, self.service.update("", None))

    '''
    @patch('requests.get')
    def test_it_should_be_able_to_send_requests(self, get):
        self.assertNotEqual(None, self.service.data())

        self.assertNotEqual(None, self.service.retrieve_instances("TEST"))
        self.assertNotEqual(None, self.service.update("TEST_NS", "TRUE"))
        self.assertNotEqual(None, self.service.update("TEST_NS", True))
    '''