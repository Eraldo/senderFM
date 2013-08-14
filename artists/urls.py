#!/usr/bin/env python
"""
Contains the artist related url mappings.
"""

from django.conf.urls import patterns, url
from django.shortcuts import redirect
from artists.views import ArtistListView, ArtistDetailView
from pages.views import ProfileView

__author__ = "Eraldo Helal"

urlpatterns = patterns('',
    # ex: ../
    url(r'^$',
        ArtistListView.as_view(),
        name='artist_list'),

    # ex: ../4/
    url(r'^(?P<pk>\d+)/$',
        ArtistDetailView.as_view(),
        name='artist_detail'),
)
