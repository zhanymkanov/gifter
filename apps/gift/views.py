from rest_framework import permissions
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView, RetrieveAPIView

from ..constants import ErrorMessage
from .models import Category, Gift
from .serializers import CategoryListSerializer, GiftListSerializer


class CategoriesList(ListAPIView):
    serializer_class = CategoryListSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Category.objects.filter(is_active=True)


class CategoryGiftsList(ListAPIView):
    serializer_class = GiftListSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        try:
            category = Category.objects.get(slug=self.kwargs["slug"])
        except Category.DoesNotExist:
            raise NotFound(detail=ErrorMessage.CATEGORY_DOES_NOT_EXIST)

        return Gift.objects.filter(categories__id=category.id, is_active=True)


class GiftDetails(RetrieveAPIView):
    serializer_class = GiftListSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Gift.objects.filter(is_active=True)
    lookup_field = "slug"

    def get_object(self):
        try:
            gift = self.queryset.get(slug=self.kwargs["slug"])
        except Gift.DoesNotExist:
            raise NotFound(detail=ErrorMessage.GIFT_DOES_NOT_EXIST)

        return gift
