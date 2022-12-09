from django.urls import path
from balance.views import *

app_name = "balance"

urlpatterns = [
   path('create_wallet/', WalletViewSet.as_view({'post':'create'}) ),
   path('balance/<str:pk>', WalletViewSet.as_view({'get':'retrieve'})),
   path('wallets/', WalletViewSet.as_view({'get':'wallet_by_user'})),
   path('wallets/<str:pk>',WalletViewSet.as_view({'delete':'destroy'})),
]