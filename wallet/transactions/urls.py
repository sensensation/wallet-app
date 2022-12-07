from django.urls import path
from transactions.views import *

app_name = "transactions"

urlpatterns = [
   path('make_transaction/', TransactionAPIView.as_view()),
   path('wallets/transactions/<str:wallet_adress>', transactions_by_wallet, name='transactions_by_wallet'),
   path('transactions/<str:id>', transaction_by_id, name='transaction_by_id'),
]