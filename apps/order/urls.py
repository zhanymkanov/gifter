from django.urls import path

from . import views

urlpatterns = [
    path("orders/", views.OrderCreate.as_view()),
]
