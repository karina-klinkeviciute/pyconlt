# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from conference.mixins.event_foreign_key import EventFKMixin
from presenters.models import Presenter


class Workshop(EventFKMixin, models.Model):
    """
    Model for workshop
    """
    title = models.CharField(
        max_length=255,
        help_text=_('Workshop title')
    )
    abstract = models.TextField(
        help_text=_('Describe shortly what this course is about.')
    )
    takeaway = models.TextField(
        help_text=_('What will people learn and take with them '
                    'after this workshop')
    )
    agenda = models.TextField(
        help_text=_('Steps of the workshop, each after another.')
    )
    target_audience = models.TextField(
        help_text=_('What audience you are targeting - beginners, '
                    'intermediate or advanced users.')
    )
    prerequisites = models.TextField(
        help_text='What you should already know before coming to this workshop'
    )
    coach = models.ForeignKey(
        Presenter,
        help_text='A coach of a workshop',
        on_delete=models.SET_NULL
    )
