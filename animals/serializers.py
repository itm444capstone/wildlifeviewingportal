from rest_framework import serializers
from animals.models import *


class AnimalSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializers for the Animal class """

    class Meta:
        model = Animal
        fields = ('id', 'url', 'name', 'icon', 'description')
