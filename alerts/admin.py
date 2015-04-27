from django.contrib import admin
from alerts.models import Alert


# Register your models here.
@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description', ]
    list_filter = ('publish', 'level',)