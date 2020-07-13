import pytest

from apps.order.models import Order


@pytest.mark.django_db
def test_model_str():
    order = Order(total=0, number=Order.generate_number())

    assert str(order) == f"Order: {order.number}"
