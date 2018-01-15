import hashlib

from django.db import models
from django.utils.translation import ugettext_lazy as _

from .proposal import Proposal


def unique_dir_path(instance, filename):
    h = hashlib.sha1(str(instance.proposal).encode('UTF-8')).hexdigest()
    return ('proposal_data/{username}/{proposal_hash}/{filename}'.format(
                username=instance.proposal.user.username,
                proposal_hash=h,
                filename=filename
            ))


class Attachment(models.Model):
    proposal = models.ForeignKey(
        Proposal,
        help_text=_('Attachment of proposal'),
        on_delete=models.CASCADE,
        related_name='attachments'
    )

    upload = models.FileField(
        upload_to=unique_dir_path
    )
