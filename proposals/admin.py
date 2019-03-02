from django.contrib import admin
from proposals.models.proposal import Proposal
from proposals.models.attachment import Attachment


class ProposalAdmin(admin.ModelAdmin):
    list_display = ('title', 'presenter', 'event', 'state', 'type')
    list_filter = ('event', 'state', 'type')


admin.site.register(Proposal, ProposalAdmin)
admin.site.register(Attachment)
