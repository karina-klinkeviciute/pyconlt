from django.db import models
from django.utils.translation import ugettext_lazy as _


class Comment(models.Model):

    author = models.ForeignKey(
        "committee_member.CommitteeMember",
        on_delete=models.PROTECT,
        verbose_name=_("Author"),
        related_name="comments",
    )

    proposal = models.ForeignKey("proposals.Proposal", on_delete=models.PROTECT, verbose_name=_("Proposal"))

    created_at = models.DateTimeField(_("Date created"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Date updated"), auto_now=True)

    text = models.TextField()

    def __str__(self):
        return self.text
