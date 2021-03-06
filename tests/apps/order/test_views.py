import pytest
from django.conf import settings
from rest_framework.test import APIClient

from apps.order.constants import ErrorMessage
from apps.order.models import Order

User = settings.AUTH_USER_MODEL


@pytest.mark.django_db
def test_order_create(client: APIClient, order_payload: dict) -> None:
    resp = client.post("/orders/", data=order_payload)

    assert resp.status_code == 201


@pytest.mark.django_db
def test_order_create_fail_products(client: APIClient) -> None:
    missing_products_payload = {
        "contact_name": "Bob",
        "contact_phone": "+7 (707) 123 45 67",
        "city": "Нур-Султан",
        "email": "fake@mail.com",
    }
    resp = client.post("/orders/", data=missing_products_payload)
    resp_json = resp.json()

    assert resp.status_code == 400
    assert resp_json["products"] == [ErrorMessage.ORDER_PRODUCTS_ARE_REQUIRED]


@pytest.mark.django_db
def test_order_retrieve(client: APIClient, order: Order):
    resp = client.get(f"/orders/{order.uuid}")

    assert resp.status_code == 200
