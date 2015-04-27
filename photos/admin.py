from django.contrib import admin
from photos.models import Photo


# Register your models here.
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    search_fields = ['title',]