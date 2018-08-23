# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Event(models.Model):
    """
    A model for a separate Conference event.
    """
    name = models.CharField(
        max_length=255,
        help_text=_("A name of the event e.g. PyConLT 2019")
    )
    year = models.CharField(
        max_length=255,
        help_text=_("The url path for the main page of the conference. "
                    "e.g. '2018'")
    )
    date = models.DateField(
        help_text=_("A date of the event or the date of the first day if "
                    "the event spans more than one day."),
        blank=True,
        null=True
    )
    duration = models.IntegerField(
        help_text=_("How many days the event spans"),
        blank=True,
        null=True
    )

    def __str__(self):
        """
        Returns representation string for a model.
        :return: representation string
        """
        return self.name


def get_current_event():
    return Event.objects.get_or_create(year=settings.CURRENT_EVENT)
