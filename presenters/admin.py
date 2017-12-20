from django.contrib import admin
from presenters.models.presenter import Presenter


class PresenterAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Presenter, PresenterAdmin)
