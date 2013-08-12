#!/usr/bin/env python
"""
Contains the web pages related url mappings.
"""

from django.conf.urls import patterns, url
from django.shortcuts import redirect
from pages.views import HomeView, TestView, ChatView, AboutView, ProfileView, MediaView, BoardView

__author__ = "Eraldo Helal"

urlpatterns = patterns('',
    # ex: ../
    url(r'^$',
        lambda x: redirect('home/'),
        name='redirect'),

    # ex: ../home/
    url(r'^home/$',
        HomeView.as_view(),
        name='home'),
    # ex: ../profile/
    url(r'^profile/$',
        ProfileView.as_view(),
        name='profile'),
    # ex: ../media/
    url(r'^media/$',
        MediaView.as_view(),
        name='media'),
    # ex: ../board/
    url(r'^board/$',
        BoardView.as_view(),
        name='board'),
    # ex: ../about/
    url(r'^about/$',
        AboutView.as_view(),
        name='about'),

    # ex: ../chat/
    url(r'^chat/$',
        ChatView.as_view(),
        name='chat'),
    # ex: ../test/
    url(r'^test/$',
        TestView.as_view(),
        name='test'),
)
