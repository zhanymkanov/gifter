from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView, RetrieveAPIView

from ..constants import ErrorMessage
from .filters import GiftFilter
from .models import Category, Gift
from .serializers import CategorySerializer, GiftSerializer


class CategoriesList(ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Category.objects.filter(is_active=True)


class CategoryGiftsList(ListAPIView):
    serializer_class = GiftSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    filter_backends = (
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    )
    filterset_class = GiftFilter
    ordering_fields = ("price",)
    search_fields = (
        "name",
        "description",
    )

    def get_queryset(self):
        try:
            category = Category.objects.get(slug=self.kwargs["slug"])
        except Category.DoesNotExist:
            raise NotFound(detail=ErrorMessage.CATEGORY_DOES_NOT_EXIST)

        return Gift.objects.filter(categories__id=category.id, is_active=True)


class GiftDetails(RetrieveAPIView):
    serializer_class = GiftSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Gift.objects.filter(is_active=True)

    def get_object(self):
        try:
            gift = self.queryset.get(slug=self.kwargs["slug"])
        except Gift.DoesNotExist:
            raise NotFound(detail=ErrorMessage.GIFT_DOES_NOT_EXIST)

        return gift
