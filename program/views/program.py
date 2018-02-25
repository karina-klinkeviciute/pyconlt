# -*- coding: utf-8 -*-
from django.views.generic import TemplateView, ListView

from program.models import Slot


class ProgramView(ListView):
    """
    A view for a program of a conference.
    """
    model = Slot
    template_name = 'program/program.html'
    context_object_name = 'slots'

    def get_queryset(self):
        """
        Return a queryset for slots.
        :return: QuerySet
        """
        queryset = Slot.objects.filter(parent_slot=None).order_by('start_time')
        # slots = list(queryset)
        # for slot in slots:
        #     children = list(slot.slot_set())
        #     child = children[0]
        return queryset
