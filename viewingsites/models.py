from django.db import models
from animals.models import Animal
from facilities.models import Facility
from photos.models import Photo
from alerts.models import Alert


# Create your models here.
class ViewSite(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField(null=True)
    ada = models.BooleanField(default=False,
            help_text="Is the site ADA compliant?",
            verbose_name="American Disabilities Act Compliant?")
    fee = models.BooleanField(default=False,
            help_text="Does the site have a fee?",
            verbose_name="Entry Fee?")
    publish = models.BooleanField(default=False,
            help_text="Do you want to publish the site?",
            verbose_name="Publish?")
    owner = models.CharField(max_length=100, null=True, blank=True)
    owner_link = models.CharField(max_length=500,
            help_text="Link to viewing site website",
            verbose_name="Viewing Site Website",
            null=True, blank=True)

    telephone = models.CharField(max_length=10, null=True, blank=True)

    animals = models.ManyToManyField(Animal, blank=True)
    facilities = models.ManyToManyField(Facility, blank=True)
    photos = models.ManyToManyField(Photo, blank=True)
    alerts = models.ManyToManyField(Alert, blank=True)

    class Meta:
        verbose_name = "Viewing Site"
        verbose_name_plural = "Viewing Sites"

    @property
    def coordinates(self):
        return [self.longitude, self.latitude]

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
