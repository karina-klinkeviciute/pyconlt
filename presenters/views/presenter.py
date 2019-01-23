# -*- coding: utf-8 -*-
import random

from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

from conference.models import Event
from presenters.models.presenter import Presenter
from presenters.forms import PresenterInfoForm
from pyconlt.settings.base import CURRENT_EVENT


@method_decorator(login_required, name='dispatch')
class PresenterUpdateView(UpdateView):
    model = Presenter
    template_name = 'presenters/presenter_update.html'
    form_class = PresenterInfoForm

    success_url = reverse_lazy('presenter_update')

    def get_object(self):
        try:
            result = self.model.objects.get(user=self.request.user)
        except self.model.DoesNotExist:
            result = self.model(user=self.request.user)
        finally:
            return result



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
        queryset = super().get_queryset().filter(active=True).order_by('?')

        return queryset

    def get(self, request, *args, **kwargs):
        """
        Returns presenters for this year.
        """
        year = kwargs.get('year', CURRENT_EVENT)
        event = Event.objects.get(year=year)
        presenters = self.get_queryset().filter(event=event)
        self.object_list = presenters
        context = self.get_context_data()
        return self.render_to_response(context)
