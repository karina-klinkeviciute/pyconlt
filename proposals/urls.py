from django.conf.urls import url

from proposals.views.cfp import CFPView
from proposals.views.manage import (
        ProposalListView,
        ProposalDeleteView,
        ProposalUpdateView
)

urlpatterns = [
    url(r'(?P<pk>\d+)/cfp_form', CFPView.as_view()),
    url(r'^$', ProposalListView.as_view(), name='proposal_list'),
    url(
        r'(?P<pk>\d+)/delete',
        ProposalDeleteView.as_view(),
        name='proposal_delete'
    ),
    url(
        r'(?P<pk>\d+)/update',
        ProposalUpdateView.as_view(),
        name='proposal_update'
    )
]
