from rest_framework import serializers


class BuyItemSerializer(serializers.Serializer):
    item = serializers.IntegerField()
    count = serializers.IntegerField()
    price = serializers.IntegerField()
