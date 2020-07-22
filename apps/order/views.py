from rest_framework import permissions
from rest_framework.generics import CreateAPIView, RetrieveAPIView

from .models import Order
from .serializers import OrderCreateSerializer


class OrderCreate(CreateAPIView):
    serializer_class = OrderCreateSerializer
    permission_classes = (permissions.AllowAny,)


class OrderDetails(RetrieveAPIView):
    serializer_class = OrderCreateSerializer
    permission_classes = (permissions.AllowAny, )
    queryset = Order.objects.all()
    lookup_field = "uuid"
