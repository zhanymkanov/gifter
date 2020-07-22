import pytest
from django.conf import settings
from rest_framework.test import APIClient

from apps.order.constants import ErrorMessage

User = settings.AUTH_USER_MODEL


@pytest.mark.django_db
def test_order_create(
        client: APIClient, order_dict_in: dict, order_dict_out: dict
) -> None:
    resp = client.post("/orders/", data=order_dict_in)
    resp_json = resp.json()

    assert resp.status_code == 201
    assert resp_json == order_dict_out


@pytest.mark.django_db
def test_order_create_fail_products(client: APIClient) -> None:
    data = {
        "contact_name": "Bob",
        "contact_phone": "+7 (707) 123 45 67",
        "city": "Нур-Султан",
        "email": "fake@mail.com",
    }
    resp = client.post("/orders/", data=data)
    resp_json = resp.json()

    assert resp.status_code == 400
    assert resp_json["products"] == [ErrorMessage.ORDER_PRODUCTS_ARE_REQUIRED]
