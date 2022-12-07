from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import CustomUser
from shortuuid.django_fields import ShortUUIDField


class Wallet(models.Model):
    """
    A class that implements the parameters corresponding to the wallet
    """

    CARDS_TYPE_CHOICE = (
        ("VISA", 1),
        ("MasterCard", 2),
    )

    CURRENCY_CHOICE = (
        ("RUB", 1),
        ("USD", 2),
        ("EUR", 3),
    )

    uid = ShortUUIDField(primary_key=True, length=8, max_length=8)
    card_type = models.CharField(choices=CARDS_TYPE_CHOICE, default="VISA", max_length=20)
    currency = models.CharField(choices=CURRENCY_CHOICE, max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    balance = models.DecimalField(max_digits=20, decimal_places=2, default=0)
