from django.shortcuts import render
from photos.serializers import *
from photos.models import *
from rest_framework import viewsets


# Create your views here.
class PhotoViewSet(viewsets.ReadOnlyModelViewSet):
    """ Default Viewset for photos """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
