from django.contrib import admin
from proposals.models.proposal import Proposal
from proposals.models.attachment import Attachment


admin.site.register(Proposal)
admin.site.register(Attachment)
