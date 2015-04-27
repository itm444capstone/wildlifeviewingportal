from rest_framework import serializers
from alerts.models import Alert


class AlertSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer class for the Alert class """

    class Meta:
        model = Alert
        fields = ('id', 'url', 'title', 'description', 'level', 'publish',
                'publish_start_date', 'publish_end_date')
