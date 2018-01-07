# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField


class Presenter(models.Model):
    """
    A class for conference presenters info
    """
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        help_text=_('If a presenter is also a user in the system, '
                    'we connect it that user'),
        on_delete=models.SET_NULL
    )
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
        app_label = 'presenters'
