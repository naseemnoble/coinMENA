from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import PriceRequest, ExchangeRate


class PriceRequestSerializer(serializers.ModelSerializer):
    #userid = serializers.CharField(required=False)
    class Meta:
        model = PriceRequest
        fields = ['from_currency', 'to_currency', 'interval_min']
'''
class ExchangeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRate
        #fields = ['from_currency_code', 'from_currency_name', 'to_currency_code', 'to_currency_name', 'exchange_rate',
        #          'last_refreshed', 'time_zone', 'bid_price', 'ask_price']
        fields = ['from_currency', 'to_currency']'''