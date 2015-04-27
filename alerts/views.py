from django.shortcuts import render
from rest_framework import viewsets
from alerts.models import *
from alerts.serializers import *


# Create your views here.
class AlertViewSet(viewsets.ReadOnlyModelViewSet):
    """ Viewset for Alerts """
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
