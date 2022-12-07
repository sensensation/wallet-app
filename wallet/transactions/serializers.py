from rest_framework import serializers


class TransactionSerializer(serializers.Serializer):

    sender = serializers.CharField(max_length=8)
    reciever = serializers.CharField(max_length=8)
    transfer_amount = serializers.DecimalField(max_digits=12, decimal_places=2)
    commission = serializers.DecimalField(max_digits=9, decimal_places=2, required=False)
    status = serializers.CharField(max_length=10, required=False)
    timestamp = serializers.DateTimeField(required=False)
    id = serializers.IntegerField(required=False)
