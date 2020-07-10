from rest_framework import serializers

from ..models import Category, Product


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "slug"]


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ["id"]
