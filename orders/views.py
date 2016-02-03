from django.views import generic
from rest_framework import viewsets
from rest_framework import filters

from orders.models import Order
from orders.serializers import OrderSerializer


class ListView(generic.ListView):
    template_name = 'list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.all().order_by('-purchase_date')


class DetailView(generic.DetailView):
    model = Order
    template_name = 'detail.html'


class SearchView(ListView):
    model = Order
    template_name = 'list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        try:

            name = self.request.GET['search']
            print name
        except:
            name = ''
        if (name != ''):
            object_list = self.model.objects.filter(id__icontains = name)
        else:
            object_list = self.model.objects.all()
        return object_list


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-purchase_date')
    serializer_class = OrderSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('order_id', 'marketplace', 'purchase_date',
                     'items', 'amount', 'currency', 'shipping')