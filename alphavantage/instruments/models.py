from django.db import models

# Create your models here.
class PriceRequest(models.Model):
    #userid = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    api_key = models.CharField(max_length=200)
    from_currency = models.CharField(max_length=200)
    to_currency = models.CharField(max_length=200)
    is_requested = models.BooleanField()
