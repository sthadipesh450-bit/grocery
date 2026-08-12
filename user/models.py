from django.db import models
from django.contrib.auth.hashers import check_password, make_password
from django.core.mail import send_mail
from django.utils.crypto import salted_hmac


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = "roles"
        verbose_name = "Role"
        verbose_name_plural = "Roles"

    def __str__(self):
        return self.name


# Create your models here.
class User(models.Model):
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

    id = models.AutoField(primary_key=True)
    profilePicture = models.ImageField(
        upload_to="user_images",
        null=True,
        blank=True,
    )
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=100)
    last_login = models.DateTimeField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    role = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )

    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def get_username(self):
        """Return the identifier Django uses for authentication displays."""
        return getattr(self, self.USERNAME_FIELD)

    def get_session_auth_hash(self):
        """Invalidate login sessions when this user's password changes."""
        return salted_hmac(
            "django.contrib.auth.models.AbstractBaseUser.get_session_auth_hash",
            self.password,
        ).hexdigest()

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def is_authenticated(self):
        """Allow this custom model to be used by Django's auth middleware."""
        return True

    @property
    def is_anonymous(self):
        return False

    @property
    def is_active(self):
        return True

    def has_perm(self, perm, obj=None):
        """Grant all Django permissions to designated superusers."""
        return self.is_active and self.is_superuser

    def has_module_perms(self, app_label):
        """Allow designated superusers to see app modules in Django admin."""
        return self.is_active and self.is_superuser
