# -*- coding: utf-8 -*-
from django.views.generic import DetailView, ListView, UpdateView
from presenters.models.presenter import Presenter


class PresenterUpdateView(UpdateView):
    model = Presenter
    template_name = 'presenters/presenter_update.html'


class PresenterView(DetailView):
    """
    Presenter Detail View.
    """
    model = Presenter
    template_name = 'presenters/presenter.html'


class PresentersView(ListView):
    """
    List View of Presenters
    """
    model = Presenter
    template_name = 'presenters/presenters_list.html'
    context_object_name = 'presenters'

    def get_queryset(self):
        """
        Order queryset by id. This way presenters that were entered first,
        will stay on top. Just a temporary measure.
        :return: ordered queryset
        """
        return super().get_queryset().order_by('id')
