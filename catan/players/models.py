from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager


AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'users.User')


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField("Email Address", max_length=255, blank=True, null=True, unique=True)
    username = models.CharField(max_length=100, blank=False, null=False, unique=True)
    is_staff = models.BooleanField("Staff Status", default=False)
    is_active = models.BooleanField("Active", default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    power_index = models.FloatField(blank=False, null=False, default=0)
    avatar = models.ImageField(upload_to="avatars")

    objects = UserManager()

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return {self.first_name}

    def __repr__(self):
        return self.username

    def __str__(self):
        return self.username

