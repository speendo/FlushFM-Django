from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^player/', include('players.urls', namespace="players")),
    url(r'^stations/', include('stations.urls', namespace="stations")),
    url(r'^admin/', include(admin.site.urls)),
)
