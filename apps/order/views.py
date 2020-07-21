from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .serializers import OrderCreateSerializer


class OrderCreate(CreateAPIView):
    serializer_class = OrderCreateSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = OrderCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if request.user.is_authenticated:
            serializer.save(user=request.user)
        else:
            serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
