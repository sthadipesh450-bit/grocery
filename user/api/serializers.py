from rest_framework import serializers

from user.models import Role, User


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ["id", "name"]
        read_only_fields = ["id"]


class UserSerializer(serializers.ModelSerializer):
    """User API serializer with write-only password support."""

    password = serializers.CharField(write_only=True, required=False, min_length=8)

    class Meta:
        model = User
        fields = [
            "id", "profilePicture", "username", "email", "phone_number", "address",
            "role", "password", "last_login", "is_staff", "is_superuser", "created_at", "updated_at",
        ]
        read_only_fields = ["id", "last_login", "created_at", "updated_at"]
        extra_kwargs = {"is_staff": {"read_only": True}, "is_superuser": {"read_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for attribute, value in validated_data.items():
            setattr(instance, attribute, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
