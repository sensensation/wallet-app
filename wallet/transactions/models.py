from django.db import models

from django.db import transaction
from accounts.models import CustomUser
from balance.models import Wallet
from django.utils.translation import gettext_lazy as _

class Transaction(models.Model):
   class STATUS(models.TextChoices):
        PENDING = 'pending', _('Pending')
        SUCCESS = 'success', _('Success')
        FAIL = 'fail', _('Fail')

   id = models.AutoField(primary_key=True)
   sender = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='sender')
   reciever = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='reciever')
   transfer_amount = models.DecimalField(max_digits=12, decimal_places=2)
   timestamp = models.DateTimeField(auto_now_add=True)
   commission = models.DecimalField(max_digits=12, decimal_places=2)
   status = models.CharField(max_length=200, null=True, choices=STATUS.choices,default=STATUS.PENDING)