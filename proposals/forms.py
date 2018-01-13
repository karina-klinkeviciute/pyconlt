from django import forms
from django.utils.translation import ugettext_lazy as _

from .models.proposal import Proposal, PROPOSAL_TYPE


class CFPForm(forms.Form):
    type = forms.ChoiceField(
        label=_('Type of proposal'),
        choices=PROPOSAL_TYPE,
        widget=forms.RadioSelect
    )
    # duration = forms.IntegerField()

    agreement = forms.BooleanField(
        label=_('I agree with Code of Conduct'),
        required=True,
    )
