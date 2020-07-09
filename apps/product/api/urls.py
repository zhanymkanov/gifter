from django.urls import path

from . import views

urlpatterns = [
    path("", views.CategoriesList.as_view()),
]
