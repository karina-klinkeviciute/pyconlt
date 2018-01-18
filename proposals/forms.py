from django import forms
from django.utils.translation import ugettext_lazy as _

from .models.proposal import Proposal\
    # , PROPOSAL_TYPE


class CFPForm(forms.Form):
    title = forms.CharField(
        label=_('Title'),
        required=True,
    )
    duration = forms.IntegerField(
        label=_('Estimated duration (minutes)'),
        initial=45,
    )

    type = forms.ChoiceField(
        label=_('Type of proposal'),
        choices=Proposal.PROPOSAL_TYPE,
        required=True,
    )

    short_description = forms.CharField(
        label=_('Short description'),
        required=True,
        widget=forms.Textarea
    )

    extra_info = forms.CharField(
        label=_('Extra info'),
        required=False,
        widget=forms.Textarea
    )

    attachment = forms.FileField(
        label=_('Attachments'),
        required=False,
    )

    agreement = forms.BooleanField(
        label=_('I agree with Code of Conduct'),
        required=True,
    )

    def is_valid(self):
        valid = super(CFPForm, self).is_valid()
        if not valid:
            return False

        data = self.cleaned_data

        if not data['agreement']:
            self._errors['agreement'] = _(
                    'Code of Conduct needs to be accepted'
            )
            return False

        return True

