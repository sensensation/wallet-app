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

    def get_queryset(self):
        if self.request.method == 'GET':
            return Wallet.objects.all()
        else:
            return Wallet.objects.filter(user=self.request.user)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        
        self.perform_create(serializer) #SAVE METHOD
        self.validate_gift(request=)
        if serializer.validated_data['currency'] == "RUB":
            serializer.validated_data['balance'] = 100
            serializer.save()
        else:
            serializer.validated_data['balance'] = 3
            serializer.save()  
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        
    def perform_create(self, serializer):
        serializer.save()
