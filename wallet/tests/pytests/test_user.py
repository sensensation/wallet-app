import pytest
from rest_framework.test import APIClient


client = APIClient()


@pytest.mark.django_db
def test_register_user():
   """
   User registration behavior verification
   """
   payload = {
            # 'id':1,
            'password':'bebrauser',
            'email':'test_email@gmail.com',
            'first_name':'test',
            'last_name':'user',
            'date_of_birth':'2000-01-01'
         }
   url = 'http://127.0.0.1:8000/register/'
   
   response = client.post(url, payload)
   
   data = response.data 
   
   assert data['first_name'] == payload['first_name']
   assert data['email'] == payload['email']
   assert data['last_name'] == payload['last_name']
   assert data['date_of_birth'] == payload['date_of_birth']
   assert "password" in data
   
@pytest.mark.django_db
def test_jwt_login_user(user_data_fixture):
   """
   Checking back response for JWT sucsess logining
   """
   reg_url = 'http://127.0.0.1:8000/register/'
   client.post(reg_url, user_data_fixture)
   
   login_url = 'http://127.0.0.1:8000/api/token/'
   response = client.post(login_url, 
                          dict(email=user_data_fixture['email'], 
                               password=user_data_fixture['password']))
   
   assert response.status_code == 200
   
@pytest.mark.django_db
def test_jwt_login_user_fail():
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
   
   