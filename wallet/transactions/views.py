from django.db import transaction, IntegrityError
from rest_framework import viewsets
from .models import CustomUser, Wallet
from rest_framework import permissions, status
from rest_framework.decorators import action

from rest_framework.response import Response

# Create your views here.
class PayViewSet(ModelViewSet):

   @action(methods=['PATCH'], detail=True)
   @transaction.atomic
   def payment_process(self, request, *args, **kwargs):
      try:
         with transaction.atomic():
            #че то тут подсчитать
            pass
      except IntegrityError:
         raise 
      
        