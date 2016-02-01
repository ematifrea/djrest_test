from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from orders.models import Order
from orders.serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-purchase_date')
    serializer_class = OrderSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('order_id', 'marketplace', 'purchase_date',
                     'items', 'amount', 'currency', 'shipping')