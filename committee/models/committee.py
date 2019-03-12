from django.db import models
from django.utils.translation import ugettext_lazy as _

from proposals.models.proposal import Proposal


class Committee(models.Model):
    title = models.CharField(
        max_length=1024,
        help_text=_("Reviewing Committee"),
        verbose_name=_("Reviewing Committee"),
        blank=False,
        null=False,
    )
    proposal = models.ForeignKey("proposals.Proposal", on_delete=models.PROTECT, verbose_name=_("Proposal"))

    def get_proposal(self, pk):
        proposal = Proposal.objects.filter(id=pk).first()
        if proposal and proposal.title:
            return proposal.title
        return "Untitled event"

    def __repr__(self):
        return f"Review Committee of {self.get_proposal(self.proposal)}"
