from django.db import models
from django.utils.translation import ugettext_lazy as _

from proposals.models.proposal import Proposal


class Committee(models.Model):
    title = models.CharField(
        max_length=1024,
        help_text=_('Title of Proposal'),
        verbose_name=_("Title"),
    )
    event = models.ForeignKey(
        "proposals.Proposal",
        on_delete=models.PROTECT,
        blank=False,
        null=False,
        verbose_name=_("Event"),
    )

    def get_event(self, pk):
        event = Proposal.objects.filter(id=pk).first()
        if event and event.titile:
            return event.title
        return "Untitled event"

    def __repr__(self):
        return f"Committee of {self.get_event(self.event)}"
