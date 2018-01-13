from django import forms
from django.utils.translation import ugettext_lazy as _

from .models.proposal import Proposal, PROPOSAL_TYPE


class CFPForm(forms.ModelForm):
    type = forms.ChoiceField(
        label=_('Type of proposal'),
        choices=PROPOSAL_TYPE,
        required=True,
    )

    short_description = forms.CharField(
        label=_('Short description'),
        required=True,
    )

    extra_info = forms.CharField(
        label=_('Extra info'),
        required=False,
    )

    attachment = forms.FileField(
        label=_('Attachments'),
        required=False,
    )

    agreement = forms.BooleanField(
        label=_('I agree with Code of Conduct'),
        required=True,
    )

    class Meta:
        model = Proposal
        fields = ('duration',)
