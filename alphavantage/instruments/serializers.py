from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import PriceRequest


class PriceRequestSerializer(serializers.ModelSerializer):
    #userid = serializers.CharField(required=False)
    class Meta:
        model = PriceRequest
        fields = ['from_currency', 'to_currency']