#!/usr/bin/env python
"""
This module contains the web pages based views.
"""
from django.contrib import messages

from django.views.generic import TemplateView

__author__ = "Eraldo Helal"


class HomeView(TemplateView):
    template_name = "pages/home.html"


class ProfileView(TemplateView):
    template_name = "pages/profile.html"


class MediaView(TemplateView):
    template_name = "pages/media.html"


class BoardView(TemplateView):
    template_name = "pages/board.html"


class AboutView(TemplateView):
    template_name = "pages/about.html"


class ChatView(TemplateView):
    template_name = "pages/chat.html"


class TestView(TemplateView):
    template_name = "pages/test.html"
    def get(self, request, *args, **kwargs):
        messages.info(request, 'Welcome to the Legend of..')
        messages.success(request, 'AWESOME')
        messages.debug(request, 'debugging')
        messages.warning(request, 'Take care..')
        messages.error(request, 'This will change your life!')
        return super(TestView, self).get(request, *args, **kwargs)

