from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView

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
        category = Category.objects.get(slug=self.kwargs["slug"])
        return Product.objects.filter(categories__id=category.id, is_active=True)


class ProductDetails(RetrieveAPIView):
    lookup_field = "slug"
    serializer_class = ProductListSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return Product.objects.filter(slug=self.kwargs["slug"], is_active=True)
