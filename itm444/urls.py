from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles import views
from rest_framework import routers

from photos.views import PhotoViewSet
from facilities.views import FacilityViewSet
from animals.views import AnimalViewSet
from alerts.views import AlertViewSet
from viewingsites.views import ViewSiteViewSet


router = routers.DefaultRouter()
router.register(r'photos', PhotoViewSet)
router.register(r'facilities', FacilityViewSet)
router.register(r'animals', AnimalViewSet)
router.register(r'alerts', AlertViewSet)
router.register(r'sites', ViewSiteViewSet)

urlpatterns = []

if settings.DEBUG:
    urlpatterns = [
        # Examples:
        # url(r'^$', 'itm444.views.home', name='home'),
        # url(r'^blog/', include('blog.urls')),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^api/', include(router.urls)),
        url(r'^static/(?P<path>.*)$', views.serve),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        url(r'^.*$', include('viewingsites.urls')),
    ]
else:
    urlpatterns = [
        # Examples:
        # url(r'^$', 'itm444.views.home', name='home'),
        # url(r'^blog/', include('blog.urls')),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^api/', include(router.urls)),
        url(r'^.*$', include('viewingsites.urls')),
    ]
