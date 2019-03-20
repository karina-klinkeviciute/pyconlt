from django.contrib import admin

from .models.committee_member import CommitteeMember


class CommitteeMemberAdmin(admin.ModelAdmin):
    list_display = ("user",)
    list_filter = ("committee",)


admin.site.register(CommitteeMember, CommitteeMemberAdmin)
