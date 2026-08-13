from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from customer.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    """Customer representation that never returns the stored password."""

    password = serializers.CharField(write_only=True, required=False, min_length=8)

    class Meta:
        model = Customer
        fields = [
            "id",
            "username",
            "email",
            "phone_number",
            "address",
            "password",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        customer = Customer(**validated_data)
        if password:
            customer.password = make_password(password)
        customer.save()
        return customer

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for attribute, value in validated_data.items():
            setattr(instance, attribute, value)
        if password:
            instance.password = make_password(password)
        instance.save()
        return instance
