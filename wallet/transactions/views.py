
from rest_framework.permissions import IsAuthenticated
from transactions.serializers import TransactionSerializer 
from balance.models import Wallet
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from decimal import Decimal
from rest_framework.response import Response
from rest_framework import views
from transactions.models import Transaction
from typing import OrderedDict
from rest_framework.decorators import api_view
from django.db.models import Q

class TransactionAPIView(views.APIView):
   permission_classes = [IsAuthenticated]

   @transaction.atomic
   def post(self, request):
      """
      Summing up banch of methods to create a transaction
      http://127.0.0.1:8000/make_transaction [POST]
      """
      serializer = TransactionSerializer(data=request.data)
      
      if serializer.is_valid() == False:
         raise ValueError('Problem with data')
      print(serializer.data)
      data = serializer.validated_data
      print(type(data))
      wallets = _get_wallet(data)
      commission = _validate_commission(wallets)

      transaction = Transaction.objects.create(
            sender = wallets['wallet_sender'],
            reciever = wallets['wallet_reciever'],
            transfer_amount = data['transfer_amount'],
            commission = Decimal(commission),
        )
      
      transaction.save()

      _validate_wallets_currency(wallets)
      _validate_sender_balance(wallets['wallet_sender'], data['transfer_amount'])
   
      _make_transaction(wallets, data['transfer_amount'], commission)

      transaction.status = 'SUCCESS'
      transaction.save()

      return Response ({'Transaction created at': transaction.timestamp,
                        'Transaction ID:':transaction.id, 
                        'Transaction status is:': transaction.status, 
                        'Money transferd':transaction.transfer_amount, 
                        'Commission cost:':transaction.transfer_amount-(transaction.commission*transaction.transfer_amount)})

   def get(self, request):
      """
      Allows to see all current user`s transactions
      http://127.0.0.1:8000/make_transaction [GET]
      """
      wallets = Wallet.objects.filter(user=request.user)
      queryset = Q()
      for i in range(0, len(wallets)):
         queryset.add(Q(sender=wallets[i]), Q.OR)
         
      transactions = Transaction.objects.filter(queryset)
      serializer = TransactionSerializer(transactions, many=True)
      return Response({'All user`s transactions':serializer.data})

      

def _get_wallet(data: OrderedDict):
   """
   Gets two wallets from request.data: sender wallet and reciever wallet
   """
   sender = data['sender']
   reciever = data['reciever']
   print('Sender adress:', sender)
   try:
      wallet_sender = Wallet.objects.get(uid=sender)
      wallet_reciever = Wallet.objects.get(uid=reciever)
      return {'wallet_sender': wallet_sender, 'wallet_reciever': wallet_reciever}
   except ObjectDoesNotExist:
      raise ObjectDoesNotExist('Wallet doesnt exist')

def _validate_wallets_currency(wallets):
   """
   Checking two wallets for currency
   """
   sender = wallets['wallet_sender']
   reciever = wallets['wallet_reciever']

   if sender.currency != reciever.currency:
      raise ValueError('Cannot to send money, check currency wallets type before sending')

def _validate_sender_balance(wallet, transfer_amount):
   """
   Validate balance, need to be more than you want to send
   """
   sender = wallet
   if sender.balance < transfer_amount:
      raise ValueError('Not enough money!!!!!!!!!')


def _validate_commission(wallets):
   """
   Checking owner of sender and reciever wallets: 
   if wallet owner = reciever -> 0% commission
   else: 10% commisssion
   """
   sender = wallets['wallet_sender']
   reciever = wallets['wallet_reciever']
   if sender.user == reciever.user:
      return Decimal(1.00)
   else:
      return Decimal(0.90)


def _make_transaction(wallets, transfer_amount, commission):
   """
   Makes transaction with info about:
   - wallets adresses(uid of each wallet),
   - amount of money you want to send,
   - commission (0% or 10%),
   """
   sender = wallets['wallet_sender']
   reciever = wallets['wallet_reciever']
   print(type(commission))
   print(type(transfer_amount))
   new_sender_balance = sender.balance - transfer_amount
   new_reciever_balance = reciever.balance + Decimal(transfer_amount*commission)

   sender.balance = new_sender_balance
   reciever.balance = new_reciever_balance

   sender.save()
   reciever.save()

@api_view(['GET'])
def transactions_by_wallet(request, wallet_adress):
    """
    http://127.0.0.1:8000/wallets/transactions/(wallet_adress) to see all wallet`s transactions
    """
    wallet = Wallet.objects.get(uid=wallet_adress)
    transactions = Transaction.objects.filter(Q(sender=wallet) | Q(reciever=wallet))
    serializer = TransactionSerializer(transactions, many=True)
    return Response({'All wallet`s transactions':serializer.data})

@api_view(['GET'])
def transaction_by_id(request, id):
   """
   http://127.0.0.1:8000/transactions/(id transaction) to see data of transaction
   """
   transaction = Transaction.objects.filter(id=id)
   serializer =  TransactionSerializer(transaction, many=True)
   return Response({'Transaction':serializer.data})
   

