from rest_framework import serializers
from viewingsites.models import *
from alerts.serializers import *
from photos.serializers import *
from facilities.serializers import *
from animals.serializers import *


class ViewSiteSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for the Viewing Site Class """
    coordinates = serializers.ReadOnlyField()
    facilities = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    photos = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    alerts = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    animals = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = ViewSite
        fields = ('id', 'url', 'name', 'latitude', 'longitude', 'description',
                'ada', 'fee', 'publish', 'owner', 'owner_link',
                'animals', 'facilities', 'photos', 'alerts', 'coordinates')


class ViewSiteDetailSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for the Viewing Site Class """
    coordinates = serializers.ReadOnlyField()
    facilities = FacilitySerializer(read_only=True, many=True)
    photos = PhotoSerializer(read_only=True, many=True)
    alerts = AlertSerializer(read_only=True, many=True)
    animals = AnimalSerializer(read_only=True, many=True)

    class Meta:
        model = ViewSite
        fields = ('id', 'url', 'name', 'latitude', 'longitude', 'description',
                'ada', 'fee', 'publish', 'owner', 'owner_link',
                'animals', 'facilities', 'photos', 'alerts', 'coordinates')