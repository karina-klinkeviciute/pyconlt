import logging

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.generic import View

from ..forms import CFPForm
from ..models.attachment import Attachment
from ..models.proposal import Proposal

logger = logging.getLogger(__name__)


class CFPView(View):
    template_name = 'proposals/cfp.html'
    form_class = CFPForm

    @transaction.atomic
    def _save(self, user, form):
        data = form.cleaned_data
        proposal = Proposal(
            user=user,
            title=data['title'],
            type=data['type'],
            duration=data['duration'],
            short_description=data['short_description'],
            extra_info=data['extra_info'],
            audience_experience=data['audience_experience'],
            target_audience=data['target_audience'],
            speaker_grant=data['speaker_grant'],
            grant_description=data['grant_description']
        )
        proposal.save()
        if data['attachment'] is not None:
            attachment = Attachment(
                proposal=proposal,
                upload=data['attachment']
            )
            attachment.save()

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            try:
                self._save(request.user, form)
            except Exception as ex:
                form.add_error(None, _(
                        'Unable to store CFP. '
                        'Please report this to site administrator'
                ))
                logger.exception(ex)
            else:
                return redirect('proposal_list')

        return render(request, self.template_name, {'form': form})
