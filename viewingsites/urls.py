from django.conf.urls import include, url


urlpatterns = [
    url(r'^.*$', 'viewingsites.views.index', name='index'),
]
