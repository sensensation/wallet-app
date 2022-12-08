import pytest
from accounts.models import CustomUser
from rest_framework.test import APIClient


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