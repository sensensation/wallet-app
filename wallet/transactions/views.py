# from django.db import transaction, IntegrityError
# from rest_framework import generics, viewsets, mixins
# from .models import CustomUser, Wallet
# from rest_framework import permissions, status
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from .models import CustomUser, Wallet, Transaction
# from .serializers import TransactionSerializer
# # Create your views here.
# class TransactionViewSet(viewsets.GenericViewSet,
#                          mixins.ListModelMixin,
#                          mixins.CreateModelMixin,
#                          mixins.RetrieveModelMixin):
#    serializer_class = TransactionSerializer
#    queryset = Transaction.objects.all()
   