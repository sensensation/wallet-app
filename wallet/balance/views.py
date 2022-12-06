from rest_framework import viewsets
from .models import CustomUser, Wallet
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from balance.serializers import WalletSerializer
from rest_framework.serializers import ValidationError
from accounts.serializers import UserRegistrationSerializer


class WalletViewSet(viewsets.ModelViewSet):
    serializer_class = WalletSerializer
    permission_classes = [IsAuthenticated]

    # print(getattr(CustomUser.objects.get(id=3), "wallets_amount")) #Так, вот эта вот хуйня она работает так:
                                                                #Дает значение атрибута wallets_amount. Проблема: как теперь передавать туда постоянно текущего пользователя?

    # print(getattr(CustomUser.objects.get(id=serializer.data['user']), "wallets_amount")) #как взять wallets amount 
    #                                                                                       у  конкретного юзера
    #теперь нахуй новая проблема: почему этот кал request.data дает кортеж блядь и сравнивает его с интовым числом wallets_amount? как сука из кортежа вытащить значения???? 

    def get_queryset(self):
        if self.request.method == 'GET':
            return Wallet.objects.all()
        else:
            return Wallet.objects.filter(user=self.request.user)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer) #SAVE METHOD

        validate_gift(serializer)
    
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        
    def perform_create(self, serializer):
        serializer.save()

def validate_gift(serializer):
    if  serializer.validated_data['currency'] == "RUB":
        serializer.validated_data['balance'] = 100
        serializer.save()
    else:
        serializer.validated_data['balance'] = 3
        serializer.save() 