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

PROPOSAL_TYPE_WORKSHOP = 0
PROPOSAL_TYPE_PRESENTATION = 1

PROPOSAL_TYPE = (
    (PROPOSAL_TYPE_WORKSHOP, _('Workshop')),
    (PROPOSAL_TYPE_PRESENTATION, _('Presentation'))
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
        default=PROPOSAL_PENDING,
        help_text=_('Current state of proposal')
    )

    type = models.IntegerField(
        choices=PROPOSAL_TYPE,
        help_text=_('Type of proposal')
    )

    duration = models.IntegerField(
        help_text=_('Estimated duration (minutes)')
    )

    short_description = RichTextField(
        help_text=_('Short information about proposal')
    )

    extra_info = RichTextField(
        help_text=_('Extra information'),
        blank=True,
        null=True
    )

    def __repr__(self):
        return '<Proposal type: {0} state: {1} by: {2}>'.format(
                    self.type,
                    self.state,
                    self.user
                )

    class Meta:
        app_label = 'proposals'


class Attachment(models.Model):
    proposal = models.ForeignKey(
        Proposal,
        help_text=_('Attachment of proposal'),
        on_delete=models.CASCADE
    )

    upload = models.FileField(
        upload_to='proposal_data/'
    )
