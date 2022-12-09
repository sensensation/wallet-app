import pytest
from rest_framework.test import APIClient


client = APIClient()


@pytest.mark.django_db
def test_register_user(user_data_fixture):
   """
   User registration behavior verification
   """
   url = 'http://127.0.0.1:8000/register/'
   
   response = client.post(url, user_data_fixture)
   
   data = response.data 
   
   assert data['first_name'] == user_data_fixture['first_name']
   assert data['email'] == user_data_fixture['email']
   assert data['last_name'] == user_data_fixture['last_name']
   assert data['date_of_birth'] == user_data_fixture['date_of_birth']
   assert "password" in data
   
   
@pytest.mark.django_db
def test_jwt_login_user(user_login):
   """
   Checking back response for JWT sucsess logining
   """
   assert user_login.status_code == 200
   assert 'access' in user_login.data 
   assert 'refresh' in user_login.data 
   
@pytest.mark.django_db
def test_jwt_login_user_fail(user_data_fixture):
   """
   Checking reaction on incorrect login data
   """
   login_url = 'http://127.0.0.1:8000/api/token/'
   login_data = {
            'password':'sgddfghggfrg',
            'email':'bob_the_robber@gmail.com',
         }
   response = client.post(login_url, login_data)
   
   assert response.status_code == 401
   
@pytest.mark.django_db
def test_get_info_about_users():
   """
   Checking possibility to GET request about users
   """
   url = 'http://127.0.0.1:8000/api/userlist/'
   response = client.get(url)
   
   assert response.status_code == 200
   
   