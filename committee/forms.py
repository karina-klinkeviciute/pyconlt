from django.forms import ModelForm

from committee.models.committee import Committee


class CommitteeForm(ModelForm):

    class Meta:
        model = Committee
        fields = ("event", "title",)
