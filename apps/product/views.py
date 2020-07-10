from rest_framework import permissions
from rest_framework.generics import ListAPIView

from apps.product.models import Category, Product
from .serializers import CategoryListSerializer, ProductListSerializer


class CategoriesList(ListAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategoryListSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CategoryProductsList(ListAPIView):
    serializer_class = ProductListSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        category = Category.objects.get(slug=self.kwargs["category"])
        return Product.objects.filter(categories__id=category.id, is_active=True)
