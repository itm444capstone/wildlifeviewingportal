from django.db import models

# Create your models here.
class Photo(models.Model):
    """ This is a general purpose class for uploading photos for use
    on viewing sites """

    title = models.CharField(max_length=50)
    link = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='sites/images', null=True, blank=True)

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"
        ordering = ('title', )

    def get_image(self):
        """ Method for determing which method for uploading an image to
        select """
        if self.link:
            return self.link

        return self.image

    @property
    def img(self):
        """ Return the image as a property """
        return self.get_image()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
