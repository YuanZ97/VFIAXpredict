from django.shortcuts import render
from .models import PriceEntry, StockEntry, DateEntry
from .serializers import PriceEntrySerializer, StockEntrySerializer, DateEntrySerializer
from rest_framework import viewsets

class ValuesViewSet(viewsets.ModelViewSet):
    queryset = DateEntry.objects.all()
    serializer_class = DateEntrySerializer

def first_temp(request):
    #values = Price.objects.all()
    return render(request, 'frontend.html', {'test'})
