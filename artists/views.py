from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView
from artists.models import Artist

__author__ = "Eraldo Helal"


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class ArtistDetailView(LoginRequiredMixin, DetailView):
    model = Artist


class ArtistListView(LoginRequiredMixin, ListView):
    model = Artist