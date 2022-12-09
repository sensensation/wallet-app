from rest_framework import serializers
from .models import Wallet
from rest_framework import status
from rest_framework.response import Response


class WalletSerializer(serializers.ModelSerializer):
    card_type = serializers.CharField(max_length=20, required=False)
    
    class Meta:
        model = Wallet
        fields = "__all__"
        read_only_fields = ("card_type",)

    def create(self, validated_data):
        request = self.context.get("request")
        
        current_user = request.user
        self.validate_wallets_amount(current_user)
        
        wallet = Wallet.objects.create(
            currency = validated_data['currency'],
        )
        wallet.user = current_user
        wallet.save()
        self.validate_gift(wallet)
    
        return wallet

    def validate_gift(self, wallet) -> None:
        """
        Checking currency type of created new wallet and charging a gift
        """
        print(wallet.currency)
        if wallet.currency == "RUB":
            wallet.balance = 100
            wallet.save()
        else:
            wallet.balance = 3
            wallet.save()


    def validate_wallets_amount(self, current_user) -> None:
        """
        Checking amount of wallets of concrete user
        """
        wallets = Wallet.objects.filter(user=current_user)
        if wallets.count() >= 5:
             raise serializers.ValidationError("Too much wallets you have!")
