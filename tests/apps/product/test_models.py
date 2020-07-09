import pytest

from apps.product.models import Category


@pytest.mark.django_db
def test_model_category():
    category = Category(
        name="test", slug="test", seo_title="test", seo_description="test"
    )
    assert str(category) == "test"
