from django.db import models, transaction
from django.utils.translation import gettext_lazy as _
from accounts.models import CustomUser

import uuid

class Wallet(models.Model):

   CARDS_TYPE_CHOICE = (
      (1, 'VISA'),
      (2, 'MasterCard'),
   )
   
   CURRENCY_CHOICE = (
      (1, 'RUB'),
      (2, 'USD'),
      (3, 'EUR'),
   )

   uid = models.UUIDField(primary_key=True,max_length=8, default=uuid.uuid4, editable=False)
   card_type = models.IntegerField(choices=CARDS_TYPE_CHOICE, default=1)
   currency = models.IntegerField(choices=CURRENCY_CHOICE, default=1)
   balance = models.DecimalField(max_digits=20, decimal_places=2)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)


   user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)