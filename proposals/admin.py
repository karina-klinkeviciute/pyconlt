from django.contrib import admin

from proposals.models.attachment import Attachment
from proposals.models.proposal import Proposal
from proposals.models.review import Review


class ProposalAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'presenter', 'event', 'state', 'type')
    list_filter = ('event', 'state', 'type')


admin.site.register(Proposal, ProposalAdmin)
admin.site.register(Attachment)
admin.site.register(Review)
