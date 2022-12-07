from rest_framework import serializers
from .models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    card_type = serializers.CharField(max_length=20, required=False)

    class Meta:
        model = Wallet
        fields = "__all__"
        read_only_fields = ("card_type",)
