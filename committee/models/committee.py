from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from conference.models.event import Event


class Committee(models.Model):
    title = models.CharField(
        max_length=1024,
        help_text=_("Review Committee"),
        verbose_name=_("Review Committee"),
        null=True,
    )

    event = models.ForeignKey(
        "conference.Event",
        on_delete=models.PROTECT,
        verbose_name=_("Event"),
    )

    @property
    def get_event_name(self):
        event = Event.objects.filter(year=settings.CURRENT_EVENT).only("name").first()
        if event.name:
            return event.name
        return "Untitled Event"

    def __str__(self):
        return f"Review Committee of {self.get_event_name}"
