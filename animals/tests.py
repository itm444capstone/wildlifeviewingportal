import json
from django.test import TestCase, Client
from animals.models import *


# Create your tests here.
class TestAnimal(TestCase):
    def setUp(self):
        self.animal = Animal.objects.create(name="Test Animal",
                icon="animals/icons/17_24x24.png", description="Blah blah")

    def test_api_endpoint(self):
        client = Client()
        response = client.get("/api/animals/")
        content = json.loads(response.content.decode("utf-8"))

        self.assertEqual(content[0]['id'], 1)
