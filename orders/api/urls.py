from django.urls import path

from .views import OrderDetailAPIView, OrderListAPIView

urlpatterns = [
    path("create/", OrderListAPIView.as_view(), name="order-list"),
    path(
        "edit-delete-get-order/<int:order_id>/",
        OrderDetailAPIView.as_view(),
        name="order-detail",
    ),
]

