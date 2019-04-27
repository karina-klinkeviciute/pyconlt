# -*- coding: utf-8 -*-
import bleach
from ckeditor.fields import RichTextField
from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import ugettext_lazy as _

from conference.models import Event


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
            help_text=_("Your twitter handle")
    )

    github_handle = models.CharField(
            max_length=39,
            null=True,
            blank=True,
            help_text=_("Your github handle")
    )

    linkedin_handle = models.CharField(
            max_length=30,  # As of 2017
            null=True,
            blank=True,
            help_text=_("Your linkedin handle")
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
        verbose_name=_('Full name'),
        help_text=_("Full name to display in the list of speakers")
    )

    image = models.ImageField(
        blank=True,
        null=True,
        help_text=_('Your photo')
    )

    bio = RichTextField(
        blank=True,
        null=True,
        verbose_name=_('Short biography'),
        help_text=_(
            'Short description about yourself and your experience with Python')
    )

    expertise = ArrayField(
        models.CharField(
            max_length=50,
            blank=True,
            null=True
        ),
        help_text=_("Your skills and areas of expertise"),
        blank=True,
        null=True
    )

    speaking_experience = models.CharField(
        max_length=1024,
        null=True,
        blank=True,
        verbose_name=_('Public speaking experience'),
        help_text=_('Short description about your public speaking experience')
    )

    class Meta:
        abstract = True

    def clean(self):
        super(ProfileMixin, self).clean()

        self.bio = bleach.clean(self.bio)


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

    active = models.BooleanField(
        help_text=_('If active, it will appear on speakers page'),
        default=False
    )

    event = models.ManyToManyField(
        Event,
        help_text="Event to which this belongs. e.g. PyCon 2018.",
        blank=True,
    )

    class Meta:
        app_label = 'presenters'

    def __str__(self):
        return self.name or "No name"
