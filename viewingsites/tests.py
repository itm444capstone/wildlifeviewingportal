import json
from django.test import TestCase, Client
from viewingsites.models import *
from alerts.models import *
from facilities.models import *
from animals.models import *
from photos.models import *


# Create your tests here.
class TestViewSite(TestCase):
    def setUp(self):
        self.site = ViewSite.objects.create(name="test", latitude=88.0,
                longitude=99.0, publish=True)
        alert = Alert.objects.create(title="Test", level=0)
        facility = Facility.objects.create(name="test",
                icon="facilities/icons/8_24x24.png")
        animal = Animal.objects.create(name="test",
                icon="aniamls/icons/17_24x24.png")
        photo = Photo.objects.create(title="test",
                image="sites/images/MLMBWAf.png")

        self.site2 = ViewSite.objects.create(name="test2", latitude="88",
                longitude="99", publish=False, fee=False, ada=False,
                owner="Test", owner_link="http://test.com")
        self.site2.animals.add(animal)
        self.site2.photos.add(photo)
        self.site2.facilities.add(facility)
        self.site2.alerts.add(alert)

    def test_name(self):
        self.assertEqual(self.site.__str__(), "test")

    def test_unicode(self):
        self.assertEqual(self.site.__unicode__(), "test")

    def test_coordinates(self):
        coordinates = self.site.coordinates

        self.assertEqual(len(coordinates), 2)
        self.assertEqual(coordinates[0], 99.0)
        self.assertEqual(coordinates[1], 88.0)

    def test_apiendpoint(self):
        client = Client()
        response = client.get('/api/sites/')
        content = json.loads(response.content.decode('utf-8'))
        self.assertEqual(content[0]['id'], 1)
        self.assertEqual(content[0]['name'], "test")
        self.assertEqual(len(content), 1)

    def test_apiendpoint_unpublish(self):
        self.site.publish = False
        self.site.save()

        client = Client()
        response = client.get('/api/sites/')
        content = json.loads(response.content.decode('utf-8'))

        self.assertEqual(len(content), 0)

    def test_api_endpoint_manytomany(self):
        self.site.publish = False
        self.site.save()

        self.site2.publish = True
        self.site2.save()

        client = Client()
        response = client.get('/api/sites/')
        content = json.loads(response.content.decode('utf-8'))

        self.assertEqual(content[0]['facilities'][0], 1)
        self.assertEqual(content[0]['animals'][0], 1)
        self.assertEqual(content[0]['alerts'][0], 1)
        self.assertEqual(content[0]['photos'][0], 1)

