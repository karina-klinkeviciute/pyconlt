# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Presenter(models.Model):
    """
    A class for conference presenters info
    """
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        help_text=_('If a presenters is also a user in the system, '
                    'we connect it that user'),
        on_delete=models.SET_NULL
    )
    name = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        help_text=_("Presenter's full "
                    "name, if presenters not connected to a user")
    )
    image = models.ImageField(
        blank=True,
        null=True,
        help_text=_('A photo of a presenters')
    )
    bio = models.TextField(
        blank=True,
        null=True,
        help_text=_('Short description about the presenters')
    )
