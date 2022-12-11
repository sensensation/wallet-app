import pytest
from accounts.models import CustomUser
from rest_framework.test import APIClient

client = APIClient()

@pytest.fixture
def reg_user_fixture():
   """
   Это говно не работает хз почему
   """
   return CustomUser.objects.create(email='test_email@gmail.com', 
                                    password='bebrauser', 
                                    first_name='test', 
                                    last_name='user', 
                                    date_of_birth='2000-01-01')
   
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