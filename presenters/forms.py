from django import forms
from django.utils.translation import ugettext_lazy as _

from presenters.models.presenter import Presenter


class PresenterInfoForm(forms.ModelForm):

    class Meta:
        model = Presenter
        personal_fields = ('name', 'image', 'bio', 'expertise',
                           'speaking_experience')
        social_fields = ('twitter_handle', 'linkedin_handle', 'github_handle')
        fields = personal_fields + social_fields
