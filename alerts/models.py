from django.db import models
from django.utils import timezone


# Create your models here.
class Alert(models.Model):
    CHOICES = ((0, "Notice"),
               (1, "Warning"),
               (2, "Danger"))
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=50, null=True, blank=True)
    level = models.IntegerField(choices=CHOICES)
    publish = models.BooleanField(default=False,
            help_text="Publish this alert?",
            verbose_name="Publish?")
    publish_start_date = models.DateTimeField(auto_now_add=True,
            help_text="Publish Start Date",
            verbose_name="Publish Start Date")
    publish_end_date = models.DateTimeField(null=True, blank=True,
            help_text="Publish End Date",
            verbose_name="Publish End Date")

    class Meta:
        verbose_name = "Alert"
        verbose_name_plural = "Alerts"


    @property
    def published(self):
        today = timezone.now()

        if today > self.publish_start_date and (self.publish_end_date is None
                or today < self.publish_end_date):
            self.publish = True

        if self.publish_end_date and today > self.publish_end_date:
            self.publish = False

        return self.publish

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
