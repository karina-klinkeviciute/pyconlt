# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from presenters.views.presenter import (
    PresenterView,
    PresentersView,
    PresenterUpdateView
)
from program.views.program import ProgramView

urlpatterns = [

    url(r'^program/', ProgramView.as_view()),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
