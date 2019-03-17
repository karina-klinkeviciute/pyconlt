from django.forms import ModelForm

from committee_member.models.committee_member import CommitteeMember


class CommitteeMemberForm(ModelForm):

    class Meta:
        model = CommitteeMember
        fields = ("bio", "committee", "user",)
