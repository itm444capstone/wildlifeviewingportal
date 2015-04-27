from django.contrib import admin
from facilities.models import Facility


# Register your models here.
@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    search_fields = ['name', ]