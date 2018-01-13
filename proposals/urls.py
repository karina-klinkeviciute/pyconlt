from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from proposals.views.cfp import CFPView

urlpatterns = [
    url(r'^call_for_proposal$', CFPView.as_view()),
]
