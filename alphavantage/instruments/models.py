from django.db import models

# Create your models here.
class PriceRequest(models.Model):
    #userid = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    api_key = models.CharField(max_length=200)
    from_currency = models.CharField(max_length=200, default="BTC")
    to_currency = models.CharField(max_length=200, default="USD")
    interval_min = models.IntegerField(default=1)
    is_requested = models.BooleanField(default=False)
