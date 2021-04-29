from django.urls import path
from instruments.views import RequestpriceView


urlpatterns = [
    path('requestprice/', RequestpriceView.as_view(), name='request_price'),
]
