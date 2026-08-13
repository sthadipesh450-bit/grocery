from rest_framework import serializers

from suppliers.models import Suppliers


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suppliers
        fields = ["id", "name", "email", "phone_number", "address", "is_active", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
