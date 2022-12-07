from django.urls import path
from transactions.views import *

app_name = "transactions"

urlpatterns = [
   path('make_transaction/', TransactionAPIView.as_view()),
]