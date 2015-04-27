from django.contrib import admin
from viewingsites.models import ViewSite


def make_published(modeladmin, request, queryset):
    queryset.update(publish=True)
make_published.short_description = "Publish selected sites"

def make_unpublished(modeladmin, request, queryset):
    queryset.update(publish=False)
make_unpublished.short_description = "Unpublish selected sites"

# Register your models here.
@admin.register(ViewSite)
class ViewSiteAdmin(admin.ModelAdmin):
    search_fields = ['name', 'description', 'owner']
    list_filter = ('ada', 'fee', 'publish')
    list_display = ('name', 'owner', 'telephone', 'coordinates', 'ada', 'fee', 'publish')
    actions = [make_published, make_unpublished]

    fieldsets = (
        ("Site Information", {
            'fields': ('name', 'description', "ada", "fee", "animals", "facilities")
        }),
        ("Location Information", {
            "fields": (("latitude", "longitude"),)
        }),
        ("Owner Information", {
            "fields": ("owner", "owner_link", "telephone")
        }),
        ("Alerts", {
            "fields": ("alerts",)
        }),
        ("Photos", {
            "fields": ("photos",)
        })
    )
    filter_horizontal = ("alerts", "photos", "animals", "facilities")
    list_editable = ("ada", "fee", "publish")
    list_per_page = 20