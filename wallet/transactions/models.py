# from django.db import models
# from django.conf import settings
# import uuid
# import os
# from django.db import transaction
# from accounts.models import CustomUser
# from balance.models import Wallet
# from shortuuid.django_fields import ShortUUIDField
# from django.utils.translation import gettext_lazy as _
# # Create your models here.

# class Transaction(models.Model):
#    amount = models.DecimalField(max_digits=12, decimal_places=2)
#    date = models.DateTimeField(auto_now_add=True)
#    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
#    merchant = models.CharField(max_length=255)

# class Transfer(models.Model):
#     from_wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='from_wallet')
#     to_wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='to_wallet')
#     amount = models.DecimalField(max_digits=12, decimal_places=2)