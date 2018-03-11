# -*- coding: utf-8 -*-
from django.db.models import Q
from django.views.generic import TemplateView, ListView

from program.models import Slot, Track


class ProgramView(ListView):
    """
    A view for a program of a conference.
    """
    model = Track
    template_name = 'program/program.html'

    def get_context_data(self, **kwargs):
        """
        Overrides context_data to help organize data by tracks
        """
        context_data = super().get_context_data()
        tracks = Track.objects.all()

        # slots spanning all tracks, like introduction or lunch break
        slots_q = Q(track_span=Slot.SpanTypes.ALL_TRACKS)

        tracks_data = list()

        for track in tracks:
            track_slots_q = Q(track=track)

            track_slots = Slot.objects.filter(
                slots_q | track_slots_q
            ).order_by('start_time')

            tracks_data.append({"track": track, "slots": track_slots})

        context_data["tracks"] = tracks_data

        return context_data
