from rest_framework import viewsets
from .models import CustomUser, Wallet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from balance.serializers import WalletSerializer
from rest_framework.decorators import api_view
from typing import OrderedDict, Dict


class WalletViewSet(viewsets.ModelViewSet):
    serializer_class = WalletSerializer
    permission_classes = [IsAuthenticated]
    
    # def get_serializer_class():
    #     if self.action == 'list':
    #         return 1 #вернуть сериалайзер для листа

    def get_queryset(self) -> Dict:
        if self.request.method == "GET":
            return Wallet.objects.all()
        else:
            return Wallet.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs) -> OrderedDict:
        """
        Creates a new wallet while common value of wallets concrete user bellow 5
        Сделать здесь:
        - Вьюхи на миксинах перенести в класс
        - кастомные методы написать 
        - удаление сделать через миксин 
        - удаление wallets_amount перенести в сериалайзер
        - сериалайзер: использовать model serializer
        - create в сериалайзере
        - days left: +5
        """
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save(
                user=request.user
            )  # помогает сразу указать юзера при создании кошелька

        validate_gift(serializer)
        validate_result = validate_wallets_amount(serializer)
        if validate_result == "too much wallets":
            return Response(
                "Too much wallets you have!", status=status.HTTP_400_BAD_REQUEST
            )
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


def validate_gift(serializer) -> None:
    """
    Checking currency type of created new wallet and charging a gift
    """
    if serializer.validated_data["currency"] == "RUB":
        serializer.validated_data["balance"] = 100
        serializer.save()
    else:
        serializer.validated_data["balance"] = 3
        serializer.save()


def validate_wallets_amount(serializer) -> None:
    """
    Checking amount of wallets of concrete user
    """
    print(type(serializer))
    user = serializer.data["user"]
    current_user = CustomUser.objects.get(id=user)
    quantity = current_user.wallets_amount
    print(current_user.wallets_amount)
    if quantity >= 5:
        return "too much wallets"
    else:
        quantity += 1
        print(current_user)
        current_user.wallets_amount = quantity
        current_user.save()


@api_view(["GET"])
def watch_balance(request, wallet_uid: str) -> Dict:
    """
    http://127.0.0.1:8000/balance/(uid wallet) to see certain wallet`s balance by uid
    """
    wallet = Wallet.objects.get(pk=wallet_uid)
    serializer = WalletSerializer(wallet)
    return Response({"wallet": serializer.data}, status=status.HTTP_200_OK)


@api_view(["GET"])
def wallet_by_user(request) -> Dict:
    """
    http://127.0.0.1:8000/wallets/ to see all user`s wallets
    """
    wallets = Wallet.objects.filter(user=request.user)
    serializer = WalletSerializer(wallets, many=True)
    return Response({"wallets": serializer.data}, status=status.HTTP_200_OK)


@api_view(["DELETE"])
def delete_user_wallet(request, wallet_uid: str) -> Dict:
    """
    http://127.0.0.1:8000/wallets/(uid wallet) to delete certain wallet
    """
    wallet = Wallet.objects.get(pk=wallet_uid)
    wallet_uid_to_delete = wallet_uid  # shows in response which wallet was deleted
    id_of_cur_user = (request.user)  # helps to identify ID of current user. 
                                    # Needs to reduce wallets amound in DB

    current_user = CustomUser.objects.get(id=id_of_cur_user.id)
    quantity = current_user.wallets_amount
    if wallet.user == request.user:
        wallet.delete()
        quantity -= 1
        current_user.wallets_amount = quantity
        current_user.save()
        return Response(
            {"Wallet UID:": wallet_uid_to_delete, "Status:": "DELETED"},
            status=status.HTTP_200_OK,
        )
    else:
        return Response("Not yours wallet")
