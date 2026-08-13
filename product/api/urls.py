from django.urls import path

from .views import (
    CategoryDetailAPIView,
    CategoryListCreateAPIView,
    ProductDetailAPIView,
    ProductListCreateAPIView,
)

urlpatterns = [
    path("", ProductListCreateAPIView.as_view(), name="product-list-create"),
    path("<int:pk>/", ProductDetailAPIView.as_view(), name="product-detail"),
    path("categories/", CategoryListCreateAPIView.as_view(), name="category-list-create"),
    path("categories/<int:pk>/", CategoryDetailAPIView.as_view(), name="category-detail"),
]
