from django.shortcuts import render
from rest_framework import viewsets
from animals.models import *
from animals.serializers import *


# Create your views here.
class AnimalViewSet(viewsets.ReadOnlyModelViewSet):
    """ ViewSet for the Animal Class """

    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
