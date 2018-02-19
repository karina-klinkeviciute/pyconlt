# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Track(models.Model):
    """
    A track of a conference.
    """
    name = models.CharField(
        max_length=255,
        help_text=_("A name of a track."),
    )
    room = models.CharField(
        max_length=255,
        help_text=_("In which room the track will take place."),
        blank=True,
        null=True
    )
    moderator = models.CharField(
        max_length=255,
        help_text=_("Who will be a moderator of this track."),
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
