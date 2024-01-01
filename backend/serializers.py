from rest_framework import serializers
from .models import PriceEntry, StockEntry, DateEntry

class PriceEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceEntry
        fields = ['open', 'high', 'low', 'close', 'adj_close']

class StockEntrySerializer(serializers.ModelSerializer):
    price = PriceEntrySerializer(many = True)
    class Meta:
        model = StockEntry
        fields = ['type', 'price']

class DateEntrySerializer(serializers.ModelSerializer):
    stocks = StockEntrySerializer(many = True)
    class Meta:
        model = DateEntry
        fields = ['date', 'stocks']