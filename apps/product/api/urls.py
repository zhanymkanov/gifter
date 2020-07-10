from django.urls import path

from . import views

urlpatterns = [
    path("", views.CategoriesList.as_view()),
    path("<str:category>", views.CategoryProductsList.as_view()),
]
