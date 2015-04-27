import json
from photos.models import *
from django.test import TestCase, RequestFactory, Client

# Create your tests here.
class TestPhotos(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        self.photo = Photo(title="Test Photo", link="http://imgur.com/gallery/MLMBWAf")
        self.photo.save()

        self.photo2 = Photo(title="Test Photo 2", image="sites/images/MLMBWAf.jpg")
        self.photo2.save()

    def test_get_image(self):
        """
            Test the get_image method of Photo
        """
        link = self.photo.get_image()
        self.assertEqual(link, "http://imgur.com/gallery/MLMBWAf")

    def test_img_property(self):
        """
            Test the img property of Photo
        """
        link = self.photo.img
        self.assertEqual(link, "http://imgur.com/gallery/MLMBWAf")

    def test_get_image_with_photo(self):
        image = self.photo2.get_image()

        self.assertEqual("sites/images/MLMBWAf.jpg", image)

    def test_img_property_with_photo(self):
        image = self.photo2.img

        self.assertEqual("sites/images/MLMBWAf.jpg", image)

    def test_endpoint(self):
        client = Client()

        response = client.get("/api/photos/")
        content = json.loads(response.content.decode('utf-8'))

        self.assertEqual(content[0]['id'], 1)
        self.assertEqual(content[0]['link'], "http://imgur.com/gallery/MLMBWAf")
