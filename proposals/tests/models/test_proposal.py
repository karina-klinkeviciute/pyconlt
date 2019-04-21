import pytest

from ...models.proposal import Proposal


@pytest.mark.django_db()
class TestProposal:

    def test_proposal_can_be_created(self):
        proposal = Proposal.objects.create(
            type=1,
            duration=30,
        )
        assert proposal is not None
        assert proposal.type == Proposal.PROPOSAL_TYPE_PRESENTATION
        assert proposal.duration == 30
