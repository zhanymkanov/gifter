from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .filters import GiftFilter
from .models import Category, Gift
from .serializers import CategorySerializer, GiftSerializer


class CategoriesList(ListAPIView):
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Category.objects.active()


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
        category = Category.objects.get_by_slug(self.kwargs["slug"])
        return Gift.objects.active().filter(categories=category)


class GiftDetails(RetrieveAPIView):
    serializer_class = GiftSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_object(self):
        return Gift.objects.active().get_by_slug(self.kwargs["slug"])
