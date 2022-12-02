from django.urls import path
from accounts.views import *

app_name = "accounts"

urlpatterns = [
    path('register/', register, name="register"),
    path('api/userlist/', UserAPIList.as_view()),
]