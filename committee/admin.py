from django.contrib import admin

from .models.committee import Committee


class CommitteeAdmin(admin.ModelAdmin):
    list_display = ()
    list_filter = ()


admin.site.register(Committee, CommitteeAdmin)
