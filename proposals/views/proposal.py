import logging

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import View

from conference.models.event import Event
from pyconlt.settings.base import CURRENT_EVENT
from ..forms import ReviewForm
from ..models.proposal import Proposal
from ..models.review import Review

logger = logging.getLogger(__name__)


class ProposalView(View):
    """Displaying single Proposal with reviews from reviewers."""
    template = "proposals/proposal_detail.html"
    form_class = ReviewForm

    @transaction.atomic
    def _save(self, user, form):
        data = form.cleaned_data
        review, created = Review.objects.get_or_create(
            author=user,
            proposal=data["proposal"],
        )
        review.rating = data["rating"]
        review.text = data["text"]
        review.status = data["status"]
        review.save()

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        if not request.user.has_perm("auth.is_committee_member"):
            return HttpResponseForbidden()

        proposal_id = self.kwargs.get("pk")

        proposal = get_object_or_404(Proposal, pk=proposal_id)
        reviews = Review.objects.filter(proposal=proposal_id)
        form = self.form_class()
        context = {"proposal": proposal, "reviews": reviews, "form": form}

        return render(request, self.template, context)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        user = request.user
        if not user.has_perm("auth.is_committee_member"):
            return HttpResponseForbidden()

        form = self.form_class(request.POST)

        if form.is_valid():
            try:
                self._save(user, form)
            except Exception as ex:
                form.add_error(None, _(
                        'Unable to update Review for this Proposal. '
                        'Please report this to site administrator'
                ))
                logger.exception(ex)
            else:
                return redirect('proposal_list')
        return render(request, self.template, {'form': form})


class ProposalsViews(View):
    """Displaying proposals that are ready to be reviewed."""
    template = "proposals/proposals_to_review.html"

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        if not request.user.has_perm("auth.is_committee_member"):
            return HttpResponseForbidden()

        event = Event.objects.filter(year=CURRENT_EVENT).first()

        if event:
            proposals = Proposal.objects.filter(event=event.pk, state=0)

        context = {"proposals": proposals if event else None}

        return render(request, self.template, context)
