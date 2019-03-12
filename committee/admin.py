from django.contrib import admin

from .models.committee import Committee


class CommitteeAdmin(admin.ModelAdmin):
    list_display = ("title",)
    list_filter = ("proposal",)


admin.site.register(Committee, CommitteeAdmin)
