from django.contrib import admin

from program.models import Slot, Track


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    """
    Admin for slots.
    """
    date_hierarchy = 'start_time'
    list_display = (
        'name', 'track', 'start_time'
    )


admin.site.register(Track)
