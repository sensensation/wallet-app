from django.urls import path
from balance.views import *

app_name = "balance"

urlpatterns = [
   path('create_wallet/', WalletViewSet.as_view({'post':'create'}) ),
]