from django.urls import path

from apps.product import views

urlpatterns = [
    path("categories/", views.CategoriesList.as_view()),
    path("categories/<slug:category>/", views.CategoryProductsList.as_view()),
]