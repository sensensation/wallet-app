from rest_framework import serializers
from .models import CustomUser, Wallet, Transaction, Transfer

class TransactionSerializer(serializers.ModelSerializer):
   class Meta:
        model = Transaction
        fields = ('id', 'wallet', 'date', 'merchant', 'amount', 'user')
        read_only_fields = ('id', )

class TransferSerializer(serializers.ModelSerializer):

    to_wallet = serializers.CharField()

    def validate(self, data):
        try:
            data['to_wallet'] = Wallet.objects.get(pk=data['to_wallet'])
        except Exception as problem:
            print(problem)
            raise serializers.ValidationError("No such account from serializer")
        return data

    class Meta:
        model = Transfer
        fields = ('id', 'from_wallet', 'to_wallet', 'amount')
        read_only_fields = ('id', )