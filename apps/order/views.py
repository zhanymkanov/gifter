from rest_framework import permissions
from rest_framework.generics import CreateAPIView

from .serializers import OrderCreateSerializer


class OrderCreate(CreateAPIView):
    serializer_class = OrderCreateSerializer
    permission_classes = (permissions.AllowAny,)
