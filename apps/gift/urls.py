from django.urls import path

from . import views

urlpatterns = [
    path("categories/", views.CategoriesList.as_view()),
    path("categories/<slug:slug>/", views.CategoryGiftsList.as_view()),
    path("gifts/<slug:slug>/", views.GiftDetails.as_view()),
]
