from django.shortcuts import render
from .models import PriceEntry, StockEntry, DateEntry
from .serializers import PriceEntrySerializer, StockEntrySerializer, DateEntrySerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from backend import web_scraper


class ValuesViewSet(viewsets.ModelViewSet):
    queryset = DateEntry.objects.all()
    serializer_class = DateEntrySerializer
        

def frontend_temp(request):
    data = web_scraper.repeat_scrapping_VFIAX(60)
    #values = Price.objects.all()
    return render(request, 'frontend.html', {'test'})
