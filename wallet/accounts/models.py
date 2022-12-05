from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager



# import uuid #unique ID`es
   # uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


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
   wallets_amount = models.IntegerField(_("wallets_amount"), default=0)

   objects = CustomUserManager()

   is_staff = models.BooleanField(default=False)
   is_active = models.BooleanField(default=True)

   def __str__(self):
        return f"{self.email} - {self.first_name} {self.last_name}"