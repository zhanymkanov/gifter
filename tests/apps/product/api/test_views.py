import pytest
from rest_framework.test import APIClient

from tests.factories import CategoryFactory, ProductFactory


@pytest.mark.django_db
def test_categories_list(client: APIClient) -> None:
    resp = client.get("/categories/")
    assert resp.status_code == 200


@pytest.mark.django_db
def test_category_products_list(client: APIClient) -> None:
    category = CategoryFactory.create()
    ProductFactory.create_batch(3, categories=(category,))

    resp = client.get(f"/categories/{category.slug}")

    assert resp.status_code == 200
    assert len(resp.data) == 3
