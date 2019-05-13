# -*- coding: utf-8 -*-
import re
from django.db.models import Q
from django.http import HttpResponse
from django.views.generic import DetailView, ListView

from conference.models import Event
from proposals.models.proposal import Proposal
from pyconlt.settings.base import CURRENT_EVENT
from proposals.forms import TalksFilterForm


class TalkView(DetailView):
    """
    Presenter Detail View.
    """
    model = Proposal
    template_name = 'proposals/talk.html'


class TalksListView(ListView):
    """
    List View of Presenters
    """
    model = Proposal
    template_name = 'proposals/talk_list.html'
    context_object_name = 'talks'

    def get_queryset(self):
        """
        Order queryset by id. This way presenters that were entered first,
        will stay on top. Just a temporary measure.
        :return: ordered queryset
        """
        return super().get_queryset().filter(
            state=Proposal.PROPOSAL_ACCEPTED).order_by('?')


    def get_tags(self, talks):
        tags = talks.filter(tags__isnull=False).values_list('tags', flat=True).distinct().order_by()

        tag_list = [tag for sublist in tags for tag in sublist]
        tag_options = [(tag, tag) for tag in set(tag_list)]
        return tag_options

    def get_talks(self, year):
        event = Event.objects.get(year=year)
        query = self.get_queryset().filter(event=event)
        return query

    def get(self, request, *args, **kwargs):
        """
        Returns presenters for this year.
        """
        input_values = request.GET.get('input')
        query = self.get_queryset()
        year = kwargs.get('year', CURRENT_EVENT)
        talks = self.get_talks(year)
        if input_values:
            values = input_values.split()
            query_list = [Q(tags__contains=[option]) for option in values]
            query_chain = query_list.pop()
            for option in query_list:
                query_chain |= option
            talks = query.filter(query_chain)
            print("talks %s " % talks)

        tag_list = self.get_tags(talks)
        # form = TalksFilterForm(choices=tag_list)

        self.object_list = talks
        context = {'talks': talks, 'tags': list(set(tag_list))}
        return self.render_to_response(context)

    # def post(self, request, *args, **kwargs):
    #     query = self.get_queryset()
    #     year = kwargs.get('year', CURRENT_EVENT)
    #     talks = self.get_talks(year)
    #
    #     tag_list = self.get_tags(talks)
    #
    #     form = TalksFilterForm(request.POST, choices=tag_list)
    #
    #     if form.is_valid():
    #         data = form.cleaned_data
    #         options = data.get('option')
    #         if options:
    #             query_list = [Q(tags__contains=[option]) for option in options]
    #             query_chain = query_list.pop()
    #             for option in query_list:
    #                 query_chain |= option
    #             talks = query.filter(query_chain)
    #         else:
    #             talks = query
    #
    #     tags = talks.filter(tags__isnull=False).values_list('tags', flat=True)
    #
    #     self.object_list = talks
    #     context = {'talks': talks, 'form': form, 'tags': tags}
    #     return self.render_to_response(context)
