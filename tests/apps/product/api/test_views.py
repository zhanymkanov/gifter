import pytest
from rest_framework.test import APIClient

from apps.product.models import Category, Product
from tests.factories import ProductFactory


@pytest.mark.django_db
def test_categories_list(client: APIClient) -> None:
    resp = client.get("/categories/")
    assert resp.status_code == 200


@pytest.mark.django_db
def test_category_products_list(client: APIClient, category: Category) -> None:
    batch_size = 3
    ProductFactory.create_batch(batch_size, categories=(category,))

    resp = client.get(f"/categories/{category.slug}/")

    assert resp.status_code == 200
    assert len(resp.data) == batch_size


@pytest.mark.django_db
def test_product_details(client: APIClient, product: Product) -> None:
    resp = client.get(f"/gift/{product.slug}/")

    assert resp.status_code == 200
