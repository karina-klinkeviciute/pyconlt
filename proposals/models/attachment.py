from django.db import models
from django.utils.translation import ugettext_lazy as _

from .proposal import Proposal


class Attachment(models.Model):
    proposal = models.ForeignKey(
        Proposal,
        help_text=_('Attachment of proposal'),
        on_delete=models.CASCADE,
        related_name='attachments'
    )

    upload = models.FileField(
        upload_to='proposal_data/'
    )
