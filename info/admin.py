from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
# Note: we are renaming the original Admin and Form as we import them!
from django.contrib.flatpages.admin import FlatPageAdmin as FlatPageAdminOld, FlatpageForm as FlatpageFormOld
from django.contrib.flatpages.models import FlatPage


class FlatpageForm(FlatpageFormOld):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = FlatPage # this is not automatically inherited from FlatpageFormOld
        fields = '__all__'


class FlatPageAdmin(FlatPageAdminOld):
    form = FlatpageForm


# We have to unregister the normal admin, and then reregister ours
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)