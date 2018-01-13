from django.contrib import admin
from presenters.models.presenter import Presenter
from presenters.models.proposal import Proposal, Attachment


class PresenterAdmin(admin.ModelAdmin):
    list_display = ('name', )
    fieldsets = (
        (None, {
            'fields': ('user',), 
        }),
        ('Personal Info', {
            'fields': ('name', 'image', 'bio', 'expertise')
        }),
        ('Social links', {
            'fields': ('linkedin_handle', 'twitter_handle', 'github_handle')
        })
    )


admin.site.register(Presenter, PresenterAdmin)
admin.site.register(Proposal)
admin.site.register(Attachment)
