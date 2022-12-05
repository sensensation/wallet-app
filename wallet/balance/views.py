from rest_framework import viewsets
from .models import CustomUser, Wallet
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from balance.serializers import WalletSerializer
# Create your views here.

# class IsAuthorOrReadOnly(permissions.BasePermission):

#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return obj.author == request.user


class WalletViewSet(viewsets.ModelViewSet):
    serializer_class = WalletSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.method == 'GET':
            return Wallet.objects.all()
        else:
            return Wallet.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save()