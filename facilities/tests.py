import json
from django.test import TestCase, Client
from facilities.models import *


# Create your tests here.
class TestFacilities(TestCase):
    def setUp(self):
        self.facility = Facility(name="Test Facility",
                icon="facilites/icons/8_24x24.png")
        self.facility.save()

    def test_facility_api(self):
        """ Test Facility API """
        client = Client()
        response = client.get("/api/facilities/")

        content = json.loads(response.content.decode('utf-8'))
        self.assertEqual(content[0]['id'], 1)
