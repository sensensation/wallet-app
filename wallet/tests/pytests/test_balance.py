import pytest
from rest_framework.test import APIClient

client = APIClient()

@pytest.mark.django_db
def test_create_wallet(create_wallet_fixture, user_login):
   """
   Wallet creation behavior verification
   """
   data = create_wallet_fixture.data 
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
   assert create_wallet_fixture.status_code == 201

@pytest.mark.django_db
def test_bad_create_wallet(user_login):
   """
   Wallet invalid creation behavior verification
   """
   url = 'http://127.0.0.1:8000/create_wallet/'
   token = user_login.data['access'] 
   wallet_data = {
        "currency":"TUGRIKI",
        "card_type":"BebraCards"
        }
   response = client.post(url, wallet_data, HTTP_AUTHORIZATION='JWT {}'.format(token))
   assert response.status_code == 400

@pytest.mark.django_db
def test_get_user_wallet(user_login):
   """
   Getting concrete user`s wallets behavior verification
   """
   token = user_login.data['access'] 
   url = 'http://127.0.0.1:8000/wallets/'
   
   response = client.get(url, HTTP_AUTHORIZATION='JWT {}'.format(token))

   assert response.status_code == 200
   
@pytest.mark.django_db
def test_get_wallet_balance(create_wallet_fixture, user_login):
   """
   Getting concrete wallet`s balance
   """
   token = user_login.data['access'] 
   
   wallet = create_wallet_fixture.data['uid']
   url = f'http://127.0.0.1:8000/balance/{wallet}'

   response = client.get(url, HTTP_AUTHORIZATION='JWT {}'.format(token))

   assert response.status_code == 200

@pytest.mark.django_db
def test_wallets_amount(wallet_data_fixture, user_login):
   """
   Checking the possibility of creating no more than 5 wallets
   """
   token = user_login.data['access'] 
   url = 'http://127.0.0.1:8000/create_wallet/'
   for i in range (0,6):
      response = client.post(url, wallet_data_fixture, HTTP_AUTHORIZATION='JWT {}'.format(token))
   
   assert "Too much wallets you have!" in response.data

@pytest.mark.django_db
def test_wallets_currency(create_wallet_fixture):
   """
   Checking accruals in accordance with the currency
   """
   balance = create_wallet_fixture.data['balance']
   currency = create_wallet_fixture.data['currency']
   if currency == 'RUB':
      assert balance == '100.00'
   else:
      assert balance == '3.0'