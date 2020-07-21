import pytest
from rest_framework.test import APIClient

from .factories import CategoryFactory, GiftFactory, UserFactory


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
def user():
    return UserFactory.create()
