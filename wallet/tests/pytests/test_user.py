import pytest
from rest_framework.test import APIClient


client = APIClient()


@pytest.mark.parametrize(
    "email, first_name, last_name, date_of_birth, password, response",
    [
        ("test_email@gmail.com", "Ivan", "Bebrov", "2000-01-01", "bebrauser", 201),
        ("", "Ivan", "Bebrov", "2000-01-01", "bebrauser", 400),
        ("test_email@gmail.com", "Ivan", "Bebrov", "2000-01-01", "", 400),
    ],
)
@pytest.mark.django_db
def test_register_user(email, first_name, last_name, date_of_birth, password, response):
    """
    User registration behavior verification by different data
    """
    url = "http://127.0.0.1:8000/register/"

    assert (
        client.post(
            url,
            {
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                "date_of_birth": date_of_birth,
                "password": password,
            },
        ).status_code
        == response
    )


@pytest.mark.django_db
def test_jwt_login_user(user_login):
    """
    Checking back response for JWT sucsess logining
    """
    assert user_login.status_code == 200
    assert "access" in user_login.data
    assert "refresh" in user_login.data

@pytest.mark.parametrize(
    "email, password, response",
    [
        ("test_email2@gmail.com", "bebrauser", 200),
        ("", "bebrauser", 400),
        ("test_email@gmail.com", "", 400),
        ("sflsdgdvrtavdf@gmail.com", "dsakfsihfgihreg", 401),
    ])
@pytest.mark.django_db
def test_jwt_login_user_fail(email, password, response, reg_user):
    """
    Checking reaction on incorrect login data
    """
    login_url = "http://127.0.0.1:8000/api/token/"
    assert client.post(login_url, {
               "email": email,
                "password": password,
    }).status_code == response

    
@pytest.mark.django_db
def test_get_info_about_users():
    """
    Checking possibility to GET request about users
    """
    url = "http://127.0.0.1:8000/api/userlist/"
    response = client.get(url)

    assert response.status_code == 200
