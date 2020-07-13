import pytest

from tests.factories import CategoryFactory, GiftFactory, ImageFactory, VendorFactory


@pytest.mark.django_db
@pytest.mark.parametrize(
    "model_factory", (CategoryFactory, ImageFactory, VendorFactory, GiftFactory),
)
def test_models_str(model_factory):
    model_obj = model_factory.create()
    assert str(model_obj) == model_obj.name
