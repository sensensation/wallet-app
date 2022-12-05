from rest_framework import serializers
from .models import CustomUser, Wallet



class WalletSerializer(serializers.ModelSerializer):
    
    user_count = serializers.SerializerMethodField()
    print(user_count)

    class Meta:
        model = Wallet
        fields = ('__all__')
        read_only_fields = ('card_type', )
    
    def get_user_count(self, obj):
        return obj.wallets_amount.count()
    print(user_count)