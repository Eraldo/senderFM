from django.db import models
from django.contrib.auth.models import AbstractUser

__author__ = "Eraldo Helal"


class Artist(AbstractUser):
    pass

    class Meta:
        verbose_name = "artist"
