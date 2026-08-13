from django.urls import path

from .views import OrderDetailAPIView, OrderListAPIView

urlpatterns = [
    path("", OrderListAPIView.as_view(), name="order-list-create"),
    path("<int:order_id>/", OrderDetailAPIView.as_view(), name="order-detail"),
]
