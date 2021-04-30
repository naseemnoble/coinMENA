from django.db import models

# Create your models here.
class PriceRequest(models.Model):
    #userid = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    api_key = models.CharField(max_length=200)
    from_currency = models.CharField(max_length=200, default="BTC")
    to_currency = models.CharField(max_length=200, default="USD")
    interval_min = models.IntegerField(default=60)
    is_requested = models.BooleanField(default=False)

class ExchangeRate(models.Model):
    from_currency_code = models.CharField(max_length=200)
    from_currency_name = models.CharField(max_length=200)
    to_currency_code = models.CharField(max_length=200)
    to_currency_name = models.CharField(max_length=200)
    exchange_rate = models.FloatField(default=0.0)
    last_refreshed = models.DateTimeField()
    time_zone = models.CharField(max_length=200)
    bid_price = models.FloatField(default=0.0)
    ask_price = models.FloatField(default=0.0)

