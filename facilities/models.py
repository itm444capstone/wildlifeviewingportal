from django.db import models


# Create your models here.
class Facility(models.Model):
    """ Represents a facility that can be found at a viewing site """
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to="facilities/icons/", null=True, blank=True)

    class Meta:
        verbose_name = "Facility"
        verbose_name_plural = "Facilities"

