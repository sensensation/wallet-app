from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser, PermissionsMixin):
    """
    Creates a new users
    """

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    username = None

    id = models.AutoField(primary_key=True)
    email = models.EmailField(_("email address"), blank=False, unique=True)
    first_name = models.CharField(_("first name"), max_length=150, blank=False)
    last_name = models.CharField(_("last name"), max_length=150, blank=False)
    date_of_birth = models.DateField(_("date of birth"), max_length=150, blank=False)

    objects = CustomUserManager()

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "accounts"
    
    def __str__(self):
        return f"{self.email} - {self.first_name} {self.last_name}"
