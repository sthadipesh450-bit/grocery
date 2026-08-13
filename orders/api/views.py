from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from orders.models import Order
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderSerializer


class OrderListAPIView(ListCreateAPIView):
    queryset = Order.objects.all().order_by("-order_date", "-order_id")
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

class OrderDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    lookup_field = "order_id"
    permission_classes = [IsAuthenticated]
