from django.db import models, transaction
from django.utils.translation import gettext_lazy as _
from accounts.models import CustomUser
from django.utils.crypto import get_random_string
import uuid
from shortuuid.django_fields import ShortUUIDField

class Wallet(models.Model):

   CARDS_TYPE_CHOICE = (
      (1, 'VISA'),
      (2, 'MasterCard'),
   )
   
   CURRENCY_CHOICE = (
      ('RUB', 1),
      ('USD', 2),
      ('EUR', 3),
   )

   uid = ShortUUIDField(primary_key=True, length=8, max_length=8)
   card_type = models.IntegerField(choices=CARDS_TYPE_CHOICE, default=1)
   currency = models.CharField(choices=CURRENCY_CHOICE, max_length=3)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
   user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

   balance = models.DecimalField(max_digits=20, decimal_places=2, default=0)
