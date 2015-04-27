from rest_framework import serializers
from photos.models import *


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer class for photos """

    class Meta:
        model = Photo
        fields = ('id', 'url', 'link', 'image')
