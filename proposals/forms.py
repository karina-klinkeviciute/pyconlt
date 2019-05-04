from django import forms
from django.utils.translation import ugettext_lazy as _

from .models.proposal import Proposal
from .models.review import Review


class CFPForm(forms.Form):
    title = forms.CharField(
        label=_('Title'),
        required=True,
    )
    duration = forms.IntegerField(
        label=_('Estimated duration (minutes)'),
        initial=30,
    )

    type = forms.ChoiceField(
        label=_('Type of proposal'),
        choices=Proposal.PROPOSAL_TYPE,
        required=True,
    )

    short_description = forms.CharField(
        label=_('Short description (1000-2000 characters)'),
        required=True,
        widget=forms.Textarea
    )

    audience_experience = forms.ChoiceField(
        label=_('Audience level'),
        choices=Proposal.AUDIENCE_EXPERIENCE,
        required=True,
    )

    target_audience = forms.CharField(
        label=_('Target Audience'),
        required=False,
        widget=forms.Textarea
    )

    extra_info = forms.CharField(
        label=_('Extra info'),
        required=False,
        widget=forms.Textarea
    )

    speaker_grant = forms.BooleanField(
        required=False,
    )

    grant_description = forms.CharField(
        label=_('Grant description'),
        required=False,
    )

    attachment = forms.FileField(
        label=_(
            'Attachments (optional). '
            'Can be anything you would like us to see.'),
        required=False,
    )

    agreement = forms.BooleanField(
        required=True,
    )

    def is_valid(self):
        valid = super(CFPForm, self).is_valid()
        if not valid:
            return False

        data = self.cleaned_data

        if data['speaker_grant'] and not data['grant_description']:
            self._errors['grant_description'] = _(
                'You must provide more information about expected grant'
            )
            return False

        if not data['agreement']:
            self._errors['agreement'] = _(
                    'Code of Conduct needs to be accepted'
            )
            return False

        return True


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ("text", "rating", "status")


class TalksFilterForm(forms.Form):

    def __init__(self, *args, **kwargs):
        choices = kwargs.pop('choices')
        super().__init__(*args, **kwargs)
        self.fields['option'].choices = choices

    option = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
        required=False)
