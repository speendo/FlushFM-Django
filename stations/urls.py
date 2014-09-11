from django.conf.urls import patterns, url

from stations import views
# from django.conf.urls.i18n import urlpatterns

urlpatterns = patterns('',
	url(r'^$', views.StationList.as_view(), name='list'),
	url(r'^create/$', views.StationCreate.as_view(), name='create'),
	url(r'^create_genre/$', views.GenreCreate.as_view(), name='genre_create'),
)