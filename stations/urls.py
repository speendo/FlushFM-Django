from django.conf.urls import patterns, url

from stations.views import StationList, StationCreate, GenreCreate
from django.conf.urls.i18n import urlpatterns

urlpatterns=patterns('',
	url(r'^$', StationList.as_view(), name='list'),
	url(r'^create/$', StationCreate.as_view(), name='create'),
	url(r'^create_genre/$', GenreCreate.as_view(), name='genre_create'),
)