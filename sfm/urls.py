from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

__author__ = "Eraldo Helal"

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sfm.views.home', name='home'),
    # url(r'^sfm/', include('sfm.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^pages/', include('pages.urls', namespace="pages")),

    url("^track", include("audiotracks.urls")),
    url("^(?P<username>[\w\._-]+)/track", include("audiotracks.urls")),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
