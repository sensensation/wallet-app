from rest_framework import serializers
from .models import CustomUser, Wallet



class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('__all__')
        read_only_fields = ('card_type', )
