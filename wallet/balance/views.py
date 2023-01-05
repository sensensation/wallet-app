from rest_framework import viewsets
from .models import CustomUser, Wallet
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from balance.serializers import WalletSerializer
from rest_framework.decorators import api_view, action
from typing import OrderedDict, Dict


class WalletViewSet(viewsets.ModelViewSet):
    """
      Creates a new wallet while common value of wallets concrete user bellow 5
      Сделать здесь:
      - Вьюхи на миксинах перенести в класс [DONE]
      - кастомные методы написать [DONE]
      - удаление сделать через миксин [DONE]
      - удаление wallets_amount перенести в сериалайзер [DONE]
      - сериалайзер: использовать model serializer [DONE]
      - create в сериалайзере [DONE]
      - days left: +5
    """
    serializer_class = WalletSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self) -> Dict:
        if self.request.method == "GET":
            return Wallet.objects.all()
        else:
            return Wallet.objects.filter(user=self.request.user)
        
    @action(methods=['GET'], detail=True)
    def watch_balance(self, pk: str) -> Dict:
       """
       http://127.0.0.1:8000/balance/(uid wallet) to see certain wallet`s balance by uid
       """
       wallet = Wallet.objects.select_related(pk).get(pk=pk)
       serializer = WalletSerializer(wallet)
       return Response({"wallet": serializer.data}, status=status.HTTP_200_OK)
        
       
    @action(methods=['GET'], detail=True)
    def wallet_by_user(self, request) -> Dict:
       """
       http://127.0.0.1:8000/wallets/ to see all user`s wallets
       """
       wallets = Wallet.objects.filter(user=request.user)
       serializer = WalletSerializer(wallets, many=True)
       return Response({"wallets": serializer.data}, status=status.HTTP_200_OK)