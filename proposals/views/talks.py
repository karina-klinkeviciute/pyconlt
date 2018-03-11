# -*- coding: utf-8 -*-
from django.views.generic import DetailView, ListView
from proposals.models.proposal import Proposal


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
