from django.db import models

# Create your models here.


class Historical_Crypto(models.Model):
    begins_at = models.CharField(max_length=200)
    open_price = models.DateTimeField('date published')
    close_price = models.CharField(max_length=200)
    high_price = models.CharField(max_length=200)
    low_price = models.CharField(max_length=200)
    volume = models.CharField(max_length=200)
    session = models.CharField(max_length=200)
    interpolated = models.CharField(max_length=200)
    symbol =  models.CharField(max_length=200)

class AboutInfo_Crypto(models.Model):
    asset_currency = models.CharField(max_length=200)
    display_only = models.CharField(max_length=200)
    max_order_size = models.CharField(max_length=200)
    min_order_size = models.CharField(max_length=200)
    min_order_price_increment = models.CharField(max_length=200)
    min_order_quantity_increment = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    quote_currency = models.CharField(max_length=200)
    symbol = models.CharField(max_length=200)
    tradability = models.CharField(max_length=200)    
