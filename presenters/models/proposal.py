# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField


PROPOSAL_PENDING = 0
PROPOSAL_ACCEPTED = 1
PROPOSAL_REJECTED = 2

PROPOSAL_STATE = (
    (PROPOSAL_PENDING, _('Pending for approval')),
    (PROPOSAL_ACCEPTED, _('Approved')),
    (PROPOSAL_REJECTED, _('Rejected'))
)



class Proposal(models.Model):
    user = models.ForeignKey(
        User,
        null=True,
        help_text=_('Issuer of the proposal'),
        on_delete=models.SET_NULL
    )

    state = models.IntegerField(
        choices=PROPOSAL_STATE,
        default=PROPOSAL_PENDING
    )

    class Meta:
        app_label = 'proposals'
