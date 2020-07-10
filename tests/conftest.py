import pytest
from rest_framework.test import APIClient

from .factories import CategoryFactory


@pytest.fixture()
def client():
    return APIClient()


@pytest.fixture()
def category():
    return CategoryFactory.create()
