import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_categories_list(client: APIClient) -> None:
    resp = client.get("/categories/")
    assert resp.status_code == 200
