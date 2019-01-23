from django.contrib import admin
from presenters.models.presenter import Presenter


class PresenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'active')
    fieldsets = (
        (None, {
            'fields': ('user', 'active', 'event'),
        }),
        ('Personal Info', {
            'fields': ('name', 'image', 'bio', 'expertise')
        }),
        ('Social links', {
            'fields': ('linkedin_handle', 'twitter_handle', 'github_handle')
        })
    )


admin.site.register(Presenter, PresenterAdmin)
