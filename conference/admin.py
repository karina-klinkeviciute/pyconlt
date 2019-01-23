from django.contrib import admin

# Register your models here.
from conference.models import Event

admin.site.register(Event)
