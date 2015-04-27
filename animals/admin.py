from django.contrib import admin
from animals.models import Animal


# Register your models here.
@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    search_fields = ['name', ]
