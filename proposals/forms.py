from django import forms

from .models.proposal import Proposal


class CFPForm(forms.ModelForm):
    class Meta:
        model = Proposal
        fields = ('type', 'duration', 'short_description', 'extra_info')
