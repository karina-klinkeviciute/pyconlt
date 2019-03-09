from django.contrib import admin

from .models.committee_member import CommitteeMember


class CommitteeMemberAdmin(admin.ModelAdmin):
    list_display = ()
    list_filter = ()


admin.site.register(CommitteeMember, CommitteeMemberAdmin)
