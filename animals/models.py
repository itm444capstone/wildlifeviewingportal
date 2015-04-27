from django.db import models


# Create your models here.
class Animal(models.Model):
    """ This represents the possible animal categories that
    can be within a viewing site """

    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to="animals/icons/", null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animals"
        ordering = ['name',]

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
