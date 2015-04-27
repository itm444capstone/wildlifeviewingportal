import datetime
import json
from django.test import TestCase, Client
from django.utils import timezone
from alerts.models import *


# Create your tests here.
class TestAlert(TestCase):
    def setUp(self):
        self.alert = Alert.objects.create(title="Test", level=0,
                publish_start_date=timezone.now())

        first = timezone.now()
        first = first.replace(year=2011, month=1)
        last = timezone.now()
        last = last.replace(year=2011, month=3)

        self.alert2 = Alert.objects.create(title="Test2", level=0,
                publish_start_date=first,
                publish_end_date=last,
                publish=True)


    def test_published(self):
        published = self.alert.published
        self.assertTrue(published)

    def test_unpublish(self):
        published = self.alert2.published
        self.assertFalse(published)

    def test_endpoint(self):
        client = Client()
        response = client.get('/api/alerts/')
        content = json.loads(response.content.decode("utf-8"))

        self.assertEqual(content[0]['id'], 1)
        self.assertEqual(content[0]['title'], 'Test')
