from django.urls import path

from .views import SupplierDetailAPIView, SupplierListCreateAPIView

urlpatterns = [
    path("", SupplierListCreateAPIView.as_view(), name="supplier-list-create"),
    path("<int:pk>/", SupplierDetailAPIView.as_view(), name="supplier-detail"),
]
