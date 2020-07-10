from rest_framework import serializers

from .models import Category, Gift


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "slug"]


class GiftListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gift
        exclude = ["id"]
