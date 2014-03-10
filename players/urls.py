from django.conf.urls import patterns, url

from players import views
from django.conf.urls.i18n import urlpatterns

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^play/$', views.play, name='play'),
    url(r'^currentsong.html$', views.currently_playing, name='currently_playing'),
    url(r'^status.html$', views.status, name='status'),
)