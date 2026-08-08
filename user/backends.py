from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password

from .models import User


class UserModelBackend(BaseBackend):
    """Authenticate accounts stored in this project's ``users`` table."""

    def authenticate(self, request, username=None, password=None, **kwargs):
        if not username or not password:
            return None

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        return user if check_password(password, user.password) else None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
