from django.urls import path
from instruments.views import RequestpriceView, ProjectListView


urlpatterns = [
    path('requestprice/', RequestpriceView.as_view(), name='request_price'),
    path('getkey/', ProjectListView.as_view(), name='get_key'),
]
