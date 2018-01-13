from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from ..models.proposal import Proposal
from ..security import OwnerRequiredMixin


class ProposalListView(ListView):
    model = Proposal
    template_name = 'proposals/proposal_list.html'
    context_object_name = 'proposals'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class ProposalDeleteView(DeleteView, OwnerRequiredMixin):
    model = Proposal
    success_url = reverse_lazy('proposal_list')


class ProposalUpdateView(OwnerRequiredMixin, UpdateView):
    model = Proposal
    fields = ('title', 'type', 'short_description', 'extra_info')
    template_name_suffix = '_update'
    success_url = reverse_lazy('proposal_list')
