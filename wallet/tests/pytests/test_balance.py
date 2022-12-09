import pytest
from rest_framework.test import APIClient

client = APIClient()

@pytest.mark.django_db
def test_create_wallet(wallet_data_fixture, user_login):
   """
   Wallet creation behavior verification
   """
   url = 'http://127.0.0.1:8000/create_wallet/'
   
   token = user_login.data['access'] 
   
   response = client.post(url, wallet_data_fixture, HTTP_AUTHORIZATION='JWT {}'.format(token))
   
   data = response.data 

   assert user_login.status_code == 200
   assert 'access' in user_login.data 
   assert 'refresh' in user_login.data 
   
   assert "uid" in data
   assert "card_type" in data
   assert "currency" in data
   assert "created_at" in data
   assert "updated_at" in data
   assert "balance" in data
   assert "user" in data
   assert response.status_code == 201

@pytest.mark.django_db
def test_bad_create_wallet(wallet_data_fixture, user_login):
   pass

@pytest.mark.django_db
def test_get_wallet_balance(wallet_data_fixture, user_login):
   pass

@pytest.mark.django_db
def test_get_user_wallet(wallet_data_fixture, user_login):
   pass

@pytest.mark.django_db
def test_wallets_amount(wallet_data_fixture, user_login):
   pass

@pytest.mark.django_db
def test_wallets_currency(wallet_data_fixture, user_login):
   pass