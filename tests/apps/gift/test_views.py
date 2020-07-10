import pytest
from rest_framework.test import APIClient

from apps.gift.models import Category, Gift
from tests.factories import GiftFactory


@pytest.mark.django_db
def test_categories_list(client: APIClient) -> None:
    resp = client.get("/categories/")
    assert resp.status_code == 200


@pytest.mark.django_db
def test_category_products_list(client: APIClient, category: Category) -> None:
    batch_size = 3
    GiftFactory.create_batch(batch_size, categories=(category,))

    resp = client.get(f"/categories/{category.slug}/")

    assert resp.status_code == 200
    assert len(resp.data) == batch_size


@pytest.mark.django_db
def test_gift_details(client: APIClient, gift: Gift) -> None:
    resp = client.get(f"/gifts/{gift.slug}/")

    assert resp.status_code == 200
