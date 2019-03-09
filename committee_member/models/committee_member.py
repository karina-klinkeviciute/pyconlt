from django.contrib.auth.models import User
from django.db import models


class CommitteeMember(models.Model):
    """Extended basic django user model."""

    # This field is required
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    committee = models.ForeignKey(
        "committee.Committee",
        on_delete=models.PROTECT,
        blank=False,
        null=False,
    )

    # permissions = what?
    # TODO  -> make a validation if when creating committee member a user is already created. If not, Base user has to
    #  be created, but on what basis? (email?)
