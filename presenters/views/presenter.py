# -*- coding: utf-8 -*-
from django.views.generic import DetailView, ListView
from presenters.models.presenter import Presenter


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

