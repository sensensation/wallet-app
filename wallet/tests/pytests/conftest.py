import pytest
from accounts.models import CustomUser
from rest_framework.test import APIClient
from decimal import Decimal

client = APIClient()
   
@pytest.fixture
def user_data_fixture():
   """
   Gives data to continues registration
   """
   reg_data = {
            'password':'bebrauser',
            'email':'test_email@gmail.com',
            'first_name':'test',
            'last_name':'user',
            'date_of_birth':'2000-01-01'
         }
   return reg_data

@pytest.fixture
def reg_user():
   """
   Create a new user
   """
   user = {
        'password':'bebrauser',
         'email':'test_email2@gmail.com',
         'first_name':'test2',
         'last_name':'user2',
         'date_of_birth':'2002-02-02'
    }
   response = client.post('http://127.0.0.1:8000/register/', user)

   return response


@pytest.fixture
def user_login():
   """
   Creates and logining new user
   """
   user = {
        'password':'bebrauser',
         'email':'test_email@gmail.com',
         'first_name':'test',
         'last_name':'user',
         'date_of_birth':'2000-01-01'
    }
   client.post('http://127.0.0.1:8000/register/', user)

   response = client.post('http://127.0.0.1:8000/api/token/', 
                            dict(email = user['email'],
                                password = user['password']))

   return response
 
@pytest.fixture
def create_wallet_fixture(user_login):
   """
   Creates a new wallet
   """
   wallet_data = {
        "currency":"RUB",
        "card_type":"MasterCard"
        }
   token = user_login.data['access'] 
   url = 'http://127.0.0.1:8000/create_wallet/'
   response = client.post(url, wallet_data, HTTP_AUTHORIZATION='JWT {}'.format(token))
   return response

@pytest.fixture
def wallet_data_fixture():
   """
   Gives data to continues wallet creation
   """
   wallet_data = {
        "currency":"RUB",
        "card_type":"MasterCard"
        }
   return wallet_data

@pytest.fixture
def create_visa_wallet_fixture(user_login):
   """
   Creates a new wallet
   """
   wallet_data = {
        "currency":"RUB",
        "card_type":"VISA"
        }
   token = user_login.data['access'] 
   url = 'http://127.0.0.1:8000/create_wallet/'
   response = client.post(url, wallet_data, HTTP_AUTHORIZATION='JWT {}'.format(token))
   return response

@pytest.fixture
def make_transaction_fixture(create_wallet_fixture, user_login, create_visa_wallet_fixture):
   token = user_login.data['access']
   sender = create_wallet_fixture.data["uid"]
   reciever = create_visa_wallet_fixture.data["uid"]
   transfer_amount = Decimal(1.00)
   
   transaction_data = {
      "sender":sender,
      "reciever":reciever,
      "transfer_amount":transfer_amount 
   }
   
   url = 'http://127.0.0.1:8000/make_transaction/'
   
   response = client.post(url, transaction_data, HTTP_AUTHORIZATION='JWT {}'.format(token))
   
   return response

