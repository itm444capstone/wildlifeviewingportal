from django.shortcuts import render
from rest_framework import viewsets
from viewingsites.models import ViewSite
from viewingsites.serializers import *


# Create your views here.
class ViewSiteViewSet(viewsets.ReadOnlyModelViewSet):
    """ Viewset for the ViewSite model """
    queryset = ViewSite.objects.filter(publish=True)
    serializer_class = ViewSiteSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return ViewSiteSerializer
        return ViewSiteDetailSerializer

    def get_queryset(self):
        queryset = ViewSite.objects.filter(publish=True);

        facilities = self.request.QUERY_PARAMS.get('facilities', None);
        animals = self.request.QUERY_PARAMS.get('animals', None);

        if facilities is not None:
            facilities = facilities.split(',')
            queryset = queryset.filter(facilities__in=facilities).distinct()

        if animals is not None:
            animals = animals.split(',')
            queryset = queryset.filter(animals__in=animals).distinct()

        return queryset


def index(request):
    """ Index """

    return render(request, "viewingsites/index.html")
