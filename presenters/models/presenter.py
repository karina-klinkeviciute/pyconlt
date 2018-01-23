# -*- coding: utf-8 -*-
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField

from pyconlt.proposals.models.proposals import Proposal


class SocialMixin(models.Model):
    """
    Additional fields intended to cover social links.

    Not technically mixin because Django forces us to inherit model class.
    """

    # Link length based on: https://gist.github.com/tonybruess/9405134
    # Maybe bit outdated.
    twitter_handle = models.CharField(
            max_length=15,
            null=True,
            blank=True,
            help_text=_("Presenter's twitter handle")
    )

    github_handle = models.CharField(
            max_length=39,
            null=True,
            blank=True,
            help_text=_("Presenter's github handle")
    )

    linkedin_handle = models.CharField(
            max_length=30,  # As of 2017
            null=True,
            blank=True,
            help_text=_("Presenter's linkedin handle")
    )

    def has_linkedin(self):
        return self.linkedin_handle is not None

    def has_twitter(self):
        return self.twitter_handle is not None

    def has_github(self):
        return self.github_handle is not None

    class Meta:
        abstract = True


class ProfileMixin(models.Model):
    """
    Covers personal information.

    Not technically mixin because Django forces us to inherit model class.
    """

    name = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        help_text=_("Presenter's full "
                    "name, if presenter is not connected to a user")
    )
    image = models.ImageField(
        blank=True,
        null=True,
        help_text=_('A photo of a presenter')
    )
    bio = RichTextField(
        blank=True,
        null=True,
        help_text=_('Short description about the presenter')
    )

    expertise = ArrayField(
        models.CharField(
            max_length=50,
            blank=True,
            null=True
        ),
        help_text=_("Speaker's skills and areas of expertise"),
        blank=True,
        null=True
    )

    class Meta:
        abstract = True


class Presenter(ProfileMixin, SocialMixin, models.Model):
    """
    A class to combine conference presenter's info.
    """

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        help_text=_('If a presenter is also a user in the system, '
                    'we connect it that user'),
        on_delete=models.SET_NULL
    )

    class Meta:
        app_label = 'presenters'

    def __str__(self):
        return self.name

    def is_active(self):
        """
        This state should be computed.
        Proposal - Presenter is active, if has at least one approved proposal 
        """
        proposals = Proposal.objects.filter(
                presenter=self,
                state=Proposal.PROPOSAL_ACCEPTED)
        return len(proposals) > 0
