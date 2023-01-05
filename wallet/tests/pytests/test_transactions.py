import pytest
from rest_framework.test import APIClient
from decimal import Decimal

client = APIClient()


@pytest.mark.django_db
def test_make_transaction(make_transaction_fixture):
    assert make_transaction_fixture.status_code == 201
    assert make_transaction_fixture.data["Transaction status is:"] == "SUCCESS"


@pytest.mark.parametrize("transfer_amount", [Decimal(10000.0), Decimal(-1.0)])
@pytest.mark.django_db
def test_make_invalid_transaction(
    transfer_amount, create_wallet_fixture, user_login, create_visa_wallet_fixture
):
    token = user_login.data["access"]
    sender = create_wallet_fixture.data["uid"]
    reciever = create_visa_wallet_fixture.data["uid"]

    transaction_data = {
        "sender": sender,
        "reciever": reciever,
        "transfer_amount": transfer_amount,
    }
    url = "http://127.0.0.1:8000/make_transaction/"
    try:
        client.post(url, transaction_data, HTTP_AUTHORIZATION="JWT {}".format(token))
    except ValueError:
        assert True


@pytest.mark.django_db
def test_make_transaction_between_users(user_login, reg_user, create_wallet_fixture):
   """
   Checking comission
   """
   user2 = {'password':'bebrauser',
         'email':reg_user.data['email'],}

   user_login2 = client.post('http://127.0.0.1:8000/api/token/', 
                            dict(email = user2['email'],
                                password = user2['password']))
   
   token_user2 = user_login2.data["access"]
   token_user1 = user_login.data["access"]
   wallet_data = {
        "currency":"RUB",
        "card_type":"VISA"
        }
  
   url_create_wallet = 'http://127.0.0.1:8000/create_wallet/'
   user_wallet2 = (client.post(url_create_wallet, wallet_data, HTTP_AUTHORIZATION='JWT {}'.format(token_user2))).data['uid']
   user_wallet1 = create_wallet_fixture.data['uid']
   
   transaction_data = {
      "sender":user_wallet1,
      "reciever":user_wallet2,
      "transfer_amount":10.0 
   }
   
   url_transaction = 'http://127.0.0.1:8000/make_transaction/'
   response = client.post(url_transaction, transaction_data, HTTP_AUTHORIZATION='JWT {}'.format(token_user1))
   print(response.data['Commission cost:'])
   assert response.data['Commission cost:'] > 0.0
   


@pytest.mark.django_db
def test_get_transactions_by_user(user_login, make_transaction_fixture):
    """
    Getting concrete user`s transactions
    """
    token = user_login.data["access"]
    url = "http://127.0.0.1:8000/make_transaction/"

    response = client.get(url, HTTP_AUTHORIZATION="JWT {}".format(token))

    assert response.status_code == 200
    assert "All user`s transactions" in response.data
    assert make_transaction_fixture.status_code == 201


@pytest.mark.django_db
def test_get_transactions_by_wallet(create_wallet_fixture, make_transaction_fixture):
    """
    Getting concrete wallet`s transactions
    """
    wallet = create_wallet_fixture.data["uid"]
    url = f"http://127.0.0.1:8000/wallets/transactions/{wallet}"

    response = client.get(url)
    assert "All wallet`s transactions" in response.data
    assert response.status_code == 200
