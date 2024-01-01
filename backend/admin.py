from django.contrib import admin
from .models import PriceEntry, StockEntry, DateEntry

admin.site.register(PriceEntry)
admin.site.register(StockEntry)
admin.site.register(DateEntry)