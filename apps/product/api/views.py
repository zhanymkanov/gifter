from rest_framework import permissions
from rest_framework.generics import ListAPIView

from ..models import Category
from .serializers import CategoryListSerializer


class CategoriesList(ListAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategoryListSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
