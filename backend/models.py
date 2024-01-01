from django.db import models

class DateEntry(models.Model):
    date = models.DateField()

class StockEntry(models.Model):
    type = models.CharField(max_length = 10, null = False)
    date = models.ForeignKey(DateEntry, on_delete = models.CASCADE, related_name = 'stocks', null = True,  default = None)

class PriceEntry(models.Model):
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    adj_close = models.FloatField()
    stock = models.ForeignKey(StockEntry, on_delete = models.CASCADE, related_name = 'price', null = True, default = None)