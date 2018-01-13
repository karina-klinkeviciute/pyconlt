from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from ..forms import CFPForm
from ..models.proposal import Proposal
from ..models.attachment import Attachment


class CFPView(View):
    template_name = 'proposals/cfp.html'
    form_class = CFPForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            proposal = Proposal(
                user=request.user,
                type=data['type'],
                duration=data['duration'],
                short_description=data['short_description'],
                extra_info=data['extra_info']
            )
            proposal.save()
            return redirect('proposal_list')

        return render(request, self.template_name, {'form': form})
