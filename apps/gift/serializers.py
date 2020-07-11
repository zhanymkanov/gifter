from rest_framework import serializers

from .models import Category, Gift


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "slug"]


class GiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gift
        exclude = ["id"]
