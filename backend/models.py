from django.db import models

class PriceEntry(models.Model):
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    adj_close = models.FloatField()

class StockEntry(models.Model):
    type = models.CharField(max_length = 10)
    price= models.OneToOneField(PriceEntry, null = False, blank = False, on_delete = models.CASCADE)
    

class DateEntry(models.Model):
    date = models.DateField()
    stock = models.OneToOneField(StockEntry, null = False, blank = False, on_delete = models.CASCADE)