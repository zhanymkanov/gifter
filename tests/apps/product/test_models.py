import pytest

from apps.product.models import Category


@pytest.mark.django_db
def test_category():
    category = Category(
        name="test", slug="test", seo_title="test", seo_description="test"
    )
    category.save()
    assert category.id
