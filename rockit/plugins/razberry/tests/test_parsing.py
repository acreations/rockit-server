import logging
import json
import os

from django.test import TestCase

from rockit.plugins.razberry.parser import RazberryParser

class ParsingTestCase(TestCase):

    def setUp(self):
        self.logger  = logging.getLogger(__name__)
        self.basedir = os.path.dirname(__file__)
        self.parser  = RazberryParser()

        f = open(self.basedir + '/resources/initial_data.json')
        self.j = json.load(f)

        f.close()

    def test_it_should_not_parse_node_if_no_response(self):
        self.assertEqual(None, self.parser.parseDevices(None))

    def test_it_should_parse_devices_correctly(self):
        """
        Test
        """
        devices = self.j['devices']

        self.assertNotEqual(None, self.parser.parseDevices(devices))