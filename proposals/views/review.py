import logging

from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.generic import View

from ..forms import ReviewForm
from ..models.proposal import Proposal
from ..models.review import Review

logger = logging.getLogger(__name__)


class ReviewView(View):
    template = "reviews/review_form.html"
    form_class = ReviewForm

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        if not request.user.has_perm("auth.is_committee_member"):
            return HttpResponseForbidden()

        id = kwargs.get('pk')
        proposal = get_object_or_404(Proposal, id=id)

        # Checking if this user has already made a pending review, if yes then prepopulate the form else blank form.
        review = Review.objects.filter(author=request.user, proposal=proposal.pk, status=0).first()
        if review:
            form = self.form_class(initial=model_to_dict(review))
        else:
            form = self.form_class()

        return render(request, self.template, {'form': form, 'proposal': proposal})

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        if not request.user.has_perm("auth.is_committee_member"):
            return HttpResponseForbidden()

        form = self.form_class(request.POST)
        pk = kwargs.get('pk')

        if form.is_valid():
            data = form.cleaned_data
            try:
                review, created = Review.objects.get_or_create(
                    author=request.user,
                    proposal_id=pk,
                )
                # review.proposal = Proposal.objects.get(id=pk)
                review.rating = data["rating"]
                review.text = data["text"]
                review.status = data["status"]
                review.save()
                return redirect('review_list')
            except Exception as ex:
                form.add_error(None, _(
                    'Unable to store Review. '
                    'Please report this to site administrator'
                    ))
                logger.exception(ex)
        else:
            return redirect('review_list')
