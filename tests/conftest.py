import pytest
from rest_framework.test import APIClient

from .factories import CategoryFactory, ProductFactory


@pytest.fixture()
def client():
    return APIClient()


@pytest.fixture()
def category():
    return CategoryFactory.create()


@pytest.fixture()
def product():
    return ProductFactory.create()
