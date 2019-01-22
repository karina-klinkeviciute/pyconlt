# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from program.models.tracks import Track
from proposals.models.proposal import Proposal


class Slot(models.Model):
    """
    A slot for a talk or a few talks, or another slot,
    or for a general activity (lunch, coffee break)
    """
    class SpanTypes:
        """
        Span types for slots - single track versus all tracks.
        """
        SINGLE_TRACK = 1
        ALL_TRACKS = 2
        SPAN_CHOICES = (
            (SINGLE_TRACK, _("Single track")),
            (ALL_TRACKS, _("All tracks"))
        )

    track_span = models.IntegerField(
        choices=SpanTypes.SPAN_CHOICES,
        help_text=_("Does the slot span one track or all tracks "
                    "(like keynote talks and breaks)")
    )
    track = models.ForeignKey(
        Track,
        help_text=_("The track to which the slot belongs"),
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING
    )
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text=_("The name of the slot. Only necessary if it's a generic "
                    "slot and no talks are asigned to it. If a slot is "
                    "associated with a talk, a talk info will be shown")
    )
    start_time = models.DateTimeField(
        help_text=_("The start time of the slot")
    )
    length = models.IntegerField(
        help_text=_("Length of the slot in minutes")
    )
    parent_slot = models.ForeignKey(
        'program.Slot',
        on_delete=models.SET_NULL,
        help_text=_("A slot can be nested inside another slot. "
                    "If this is the case, connect it here"),
        null=True,
        blank=True
    )
    talk = models.OneToOneField(
        Proposal,
        null=True,
        blank=True,
        help_text=_("If it's a slot for a talk, select your talk here."),
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        """
        Returns info about itself and associated talk.
        """
        if self.talk:
            return "{} {}".format(self.name, self.talk.title)
        else:
            return "{}".format(self.name)
