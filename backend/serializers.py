from rest_framework import serializers
from .models import PriceEntry, StockEntry, DateEntry

class PriceEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceEntry
        fields = ['open', 'high', 'low', 'close', 'adj_close']

class StockEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = StockEntry
        fields = ['type', 'price']

class DateEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = DateEntry
        fields = ['date', 'stock']