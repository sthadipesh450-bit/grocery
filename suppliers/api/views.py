from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from suppliers.models import Suppliers
from .serializers import SupplierSerializer


class SupplierListCreateAPIView(ListCreateAPIView):
    queryset = Suppliers.objects.all().order_by("id")
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]


class SupplierDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Suppliers.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]
