import json
from django.contrib.auth.models import User
from .serializers import PriceRequestSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
#from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework_api_key.models import APIKey
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from .models import PriceRequest

class RequestpriceView(APIView):
    def post(self, request):
        print(dir(request))
        #print(request.conte)
        print(request.data)
        key = request.META["HTTP_AUTHORIZATION"].split()[1]
        print(key)
        serializer = PriceRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        #save_status = serializer.save(userid=request.user, message=request.data['message'])
        return Response(status=status.HTTP_201_CREATED)

class ProjectListView(APIView):
    permission_classes = [HasAPIKey]

    def get(self, request):
        """Retrieve a project based on the request API key."""
        key = request.META["HTTP_AUTHORIZATION"].split()[1]
        api_key = APIKey.objects.get_from_key(key)
        print(key)
        print(api_key)