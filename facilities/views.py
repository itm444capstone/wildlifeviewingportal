from django.shortcuts import render
from rest_framework import viewsets
from facilities.models import *
from facilities.serializers import *


# Create your views here.
class FacilityViewSet(viewsets.ReadOnlyModelViewSet):
    """ Facility view set for displaying the facilities in the api """
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
