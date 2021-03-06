from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Review(models.Model):

    LOW = 1
    ABOVE_LOW = 2
    AVERAGE = 3
    ABOVE_AVERAGE = 4
    HIGH = 5

    PENDING = 0
    DONE = 1

    STATUS_CHOICES = (
        (PENDING, _("Pending")),
        (DONE, _("Done")),
    )

    RATING_CHOICES = (
        (LOW, _("1")),
        (ABOVE_LOW, _("2")),
        (AVERAGE, _("3")),
        (ABOVE_AVERAGE, _("4")),
        (HIGH, _("5")),
    )

    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name=_("Author"),
        related_name="comments",
        null=True
    )

    proposal = models.ForeignKey(
        "proposals.Proposal",
        on_delete=models.CASCADE,
        verbose_name=_("Proposal"),
        related_name="comments",
    )

    rating = models.IntegerField(
        choices=RATING_CHOICES,
        verbose_name=_("Rating"),
        null=True,
        blank=True
    )

    status = models.IntegerField(
        choices=STATUS_CHOICES,
        verbose_name=_("Status"),
        default=0,
    )

    created_at = models.DateTimeField(_("Date created"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Date updated"), auto_now=True)

    text = models.TextField(
        verbose_name=_("Please leave your review here"),
        null=True,
        blank=True
    )

    def get_status(self):
        for status_value in self.STATUS_CHOICES:
            if self.status in status_value:
                return status_value[1]

    def __str__(self):
        return f"Review from {self.author.first_name} {self.author.last_name} of {self.proposal.title} proposal"
