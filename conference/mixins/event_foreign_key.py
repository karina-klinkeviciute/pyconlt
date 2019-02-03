# -*- coding: utf-8 -*-
"""
Conference relation mixin, to be used in models that are pointing to the
conference.
"""
from django.db import models

from conference.models import Event
from conference.models.event import get_current_event


class EventFKMixin(models.Model):
    """
    A mixin to add to a model which points to a conference.
    """
    class Meta:
        abstract = True

    event = models.ForeignKey(
        Event,
        help_text="Event to which this belongs. e.g. PyCon 2018.",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        default=get_current_event
    )
