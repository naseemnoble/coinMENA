from django.urls import path
from instruments.views import RequestpriceView


urlpatterns = [
    #path('getkey/', ProjectListView.as_view(), name='get_key'),
    path('exchangerate/', RequestpriceView.as_view(), name='exchange_rate'),
    #path('fetcheprice/', FetchepriceView.as_view(), name='fetche_price'),
]
