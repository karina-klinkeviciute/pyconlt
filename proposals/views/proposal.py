import csv

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.views.generic import View

from conference.models.event import Event
from pyconlt.settings.base import CURRENT_EVENT
from ..models.proposal import Proposal
from ..models.review import Review


class ProposalReviewView(View):
    """Displaying all reviews for single Proposal for presenters."""
    template = "proposals/proposal_detail.html"

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        if not request.user.has_perm("auth.is_committee_member"):
            return HttpResponseForbidden()

        proposal_id = self.kwargs.get("pk")

        proposal = get_object_or_404(Proposal, pk=proposal_id)
        reviews = Review.objects.filter(proposal=proposal_id)

        context = {"proposal": proposal, "reviews": reviews}

        return render(request, self.template, context)


class ProposalsView(View):
    """Displaying proposals that are ready to be reviewed."""
    template = "proposals/proposals_to_review.html"

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        if not request.user.has_perm("auth.is_committee_member"):
            return HttpResponseForbidden()

        event = Event.objects.filter(year=CURRENT_EVENT).first()

        if event:
            # Filtering finished reviews to display only those proposals that are still waiting for a review to be done.
            finished_reviews = Review.objects.filter(
                author=request.user,
                status=1,
            ).values_list("proposal", flat=True)
            proposals = Proposal.objects.filter(event=event.pk, state=0).exclude(id__in=finished_reviews)

        context = {"proposals": proposals if event else None}

        return render(request, self.template, context)


class ProposalsInfoView(View):
    """Displaying proposals that are ready to be reviewed."""
    template = "proposals/proposals_info.html"

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseForbidden()

        event = Event.objects.filter(year=CURRENT_EVENT).first()

        if event:
            # Filtering finished reviews to display only those proposals that are still waiting for a review to be done.
            finished_reviews = Review.objects.filter(
                author=request.user,
                status=1,
            ).values_list("proposal", flat=True)
            proposals = Proposal.objects.filter(event=event.pk, state=1, speaker_grant=True)

        context = {"proposals": proposals if event else None}

        return render(request, self.template, context)


class ProposalsCSVView(View):
    """CSV view for proposals and presenters"""
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

        writer = csv.writer(response)
        event = Event.objects.filter(year=CURRENT_EVENT).first()

        writer.writerow([
            'Email',
            'Name',
            'Title',
            'Duration',
            'Type',
            'Short description',
            'Extra info',
            'Audience experience',
            'Target audience',
            'Grant description',
            'Tags',
            'Presenter expertise'

        ])
        proposals = Proposal.objects.filter(event=event.pk, state=1)
        for proposal in proposals:
            writer.writerow([
                proposal.presenter.user.email,
                proposal.presenter.name,
                proposal.title,
                proposal.duration,
                proposal.type,
                proposal.short_description,
                proposal.extra_info,
                proposal.audience_experience,
                proposal.target_audience,
                proposal.grant_description,
                proposal.tags,
                proposal.presenter.expertise])

        return response
