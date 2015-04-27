from rest_framework import serializers
from facilities.models import *


class FacilitySerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer class for facilities """

    class Meta:
        model = Facility
        fields = ('id', 'url', 'name', 'icon')
