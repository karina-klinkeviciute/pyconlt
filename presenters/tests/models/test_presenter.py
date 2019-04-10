import pytest

from ...models.presenter import Presenter


@pytest.mark.django_db()
class TestPresenter:

    def test_presenter_can_be_created_with_no_values(self):
        presenter = Presenter.objects.create()
        assert presenter is not None
        assert presenter.user is None
        assert presenter.name is None
        assert not presenter.event.exists()
