import json
from decouple import config
from django.contrib.auth.models import User
from .serializers import PriceRequestSerializer#, ExchangeRateSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
#from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework_api_key.models import APIKey
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from .models import PriceRequest, ExchangeRate

ALPHA_API_KEY = config('ALPHA_API_KEY')
print(ALPHA_API_KEY)

class RequestpriceView(APIView):
    def post(self, request):
        print("RequestpriceView Post")
        print(dir(request))
        #print(request.conte)
        print(request.data)
        key = request.META["HTTP_AUTHORIZATION"].split()[1]
        print(key)
        serializer = PriceRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request_exist = PriceRequest.objects.filter(from_currency=request.data['from_currency'],
                                                    to_currency=request.data['to_currency'],
                                                    is_requested=True)
        if len(request_exist) == 0:
            save_status = serializer.save(api_key=key,
                                          from_currency=request.data['from_currency'],
                                          to_currency=request.data['to_currency'],
                                          interval_min=int(request.data['interval_min']), is_requested=True)
            content = {'message': "Instrument {0}/{1} successfully accepted for price".format(request.data['from_currency'], request.data['to_currency'])}
        else:
            content = {'message': "Instrument {0}/{1} Already requested".format(request.data['from_currency'], request.data['to_currency'])}
        return Response(content, status=status.HTTP_201_CREATED)

    def get(self, request):
        print("RequestpriceView Get")
        print(dir(request))
        print(request.data)
        key = request.META["HTTP_AUTHORIZATION"].split()[1]
        #serializer = PriceRequestSerializer(data=request.data)
        #serializer.is_valid(raise_exception=True)
        request_exist = PriceRequest.objects.filter(from_currency=request.data['from_currency'],
                                                    to_currency=request.data['to_currency'],
                                                    is_requested=True)
        if request_exist:
            print("Exist")
            import requests
            alphavantage_request = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={0}&to_currency={1}&apikey={2}'.format(request.data['from_currency'], request.data['to_currency'], ALPHA_API_KEY))
            alphavantage_rec = json.loads(alphavantage_request.text)
            real_curr_ex_rate = alphavantage_rec["Realtime Currency Exchange Rate"]

            from_currency_code = real_curr_ex_rate['1. From_Currency Code']
            from_currency_name = real_curr_ex_rate['2. From_Currency Name']
            to_currency_code = real_curr_ex_rate['3. To_Currency Code']
            to_currency_name = real_curr_ex_rate['4. To_Currency Name']
            exchange_rate = real_curr_ex_rate['5. Exchange Rate']
            last_refreshed = real_curr_ex_rate['6. Last Refreshed']
            time_zone = real_curr_ex_rate['7. Time Zone']
            bid_price = real_curr_ex_rate['8. Bid Price']
            ask_price = real_curr_ex_rate['9. Ask Price']
            save_exchange_rate = ExchangeRate(from_currency_code=from_currency_code, from_currency_name=from_currency_name,
                                          to_currency_code=to_currency_code, to_currency_name=to_currency_name,
                                          exchange_rate=exchange_rate, last_refreshed=last_refreshed, time_zone=time_zone,
                                          bid_price=bid_price, ask_price=ask_price)
            save_exchange_rate.save()
            msg = "Fetched"
        else:
            print("Not Exist")
            msg = "No Request exist for instrument {0}/{1}".format(request.data['from_currency'], request.data['to_currency'])
        return Response({'message' : msg}, status=status.HTTP_201_CREATED)