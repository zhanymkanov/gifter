from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.gift.models import Gift

from .constants import ErrorMessage
from .models import Order


class OrderCreateSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(
        queryset=Gift.objects.filter(is_active=True).all(), many=True
    )
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Order
        fields = (
            "contact_name",
            "contact_phone",
            "city",
            "shipping_address",
            "email",
            "user",
            "products",
        )

    def validate_products(self, products):
        if not products:
            raise ValidationError(detail=ErrorMessage.ORDER_PRODUCTS_ARE_REQUIRED)

        return products

    def create(self, validated_data):
        order = Order(
            contact_name=validated_data["contact_name"],
            contact_phone=validated_data["contact_phone"],
            city=validated_data["city"],
            email=validated_data["email"],
            user=validated_data.get("user"),
            shipping_address=validated_data.get("shipping_address", ""),
            number=Order.generate_number(),
            total=sum(p.price for p in validated_data["products"]),
        )
        order.save()
        order.products.set(validated_data["products"])
        return order
