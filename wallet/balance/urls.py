from django.urls import path
from balance.views import *

app_name = "balance"

urlpatterns = [
   path('create_wallet/', WalletViewSet.as_view({'post':'create'}) ),
   path('balance/<str:wallet_uid>', watch_balance, name='watch_balance'),
   path('wallets/', wallet_by_user, name='wallet_by_user'),
   path('wallets/<str:wallet_uid>',delete_user_wallet, name='delete_user_wallet'),
]