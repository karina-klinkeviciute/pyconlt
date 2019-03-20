from django import forms
from django.utils.translation import ugettext_lazy as _

from .models.proposal import Proposal
from .models.comment import Comment


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
        label=_('Short description'),
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
        label=_('Attachments'),
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


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ("author", "text",)
