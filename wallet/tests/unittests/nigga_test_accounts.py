from rest_framework.test import APITestCase
from accounts.models import CustomUser
from accounts.serializers import UserRegistrationSerializer, UserListSerializer
from rest_framework import status


class UserApiTestCase(APITestCase):
    def test_get(self):
        """
        Check GET request to see all users
        """
        url = "http://127.0.0.1:8000/api/userlist/"
        print("URL on which the GET test is being conducted:", url)
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        print("Response that came out:", response)


class UserSerializerTestCase(APITestCase):
    def test_ok(self):
        """
        Check GET gives us a serialized data
        """
        user_1 = CustomUser.objects.create(
            email="test_email@gmail.com",
            password="bebrauser",
            first_name="test",
            last_name="user",
            date_of_birth="2000-01-01",
        )
        data = UserListSerializer(user_1).data
        expected_data = {
            # 'id':1,
            # 'password':'bebrauser',
            "email": "test_email@gmail.com",
            "first_name": "test",
            "last_name": "user",
            # 'date_of_birth':'2000-01-01'
        }
        self.assertEqual(expected_data, data)
