from django.conf.urls import patterns, url

from stations.views import StationList, StationCreate
from django.conf.urls.i18n import urlpatterns

urlpatterns = patterns('',
    url(r'^$', StationList.as_view()),
    url(r'^create/$', StationCreate.as_view()),
)