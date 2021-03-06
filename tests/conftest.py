from typing import List

import pytest
from rest_framework.test import APIClient

from .factories import CategoryFactory, Gift, GiftFactory, OrderFactory, UserFactory


@pytest.fixture()
def client():
    return APIClient()


@pytest.fixture()
def category():
    return CategoryFactory.create()


@pytest.fixture()
def gift():
    return GiftFactory.create()


@pytest.fixture()
def gifts_list():
    return GiftFactory.create_batch(5)


@pytest.fixture()
def user():
    return UserFactory.create()


@pytest.fixture()
def order():
    return OrderFactory.create()


@pytest.fixture()
def order_payload(gifts_list: List[Gift]):
    return {
        "contact_name": "Bob",
        "contact_phone": "+77071234567",
        "city": "Нур-Султан",
        "shipping_address": "ул. Тестовая 404",
        "email": "fake@mail.com",
        "products": [gift.slug for gift in gifts_list],
    }
