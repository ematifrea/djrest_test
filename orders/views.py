from django.core.urlresolvers import reverse
from django.views import generic
from rest_framework import viewsets
from rest_framework import filters

from orders.models import Order
from orders.serializers import OrderSerializer


class ListView(generic.ListView):
    template_name = 'list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        query_params = dict(self.request.GET.items())

        field_names = [f.name for f in Order._meta.get_fields()]
        missing_fields = set(query_params.keys()).difference(set(field_names))
        if missing_fields:
            raise Exception("The following fields are missing from db: %s"
                            % missing_fields)

        query_set = Order.objects.all()
        if query_params:
            filter_key = {"%s__icontains" % query_field: value
                          for query_field, value in query_params.items()}
            query_set = query_set.filter(**filter_key)

        return query_set.order_by('-purchase_date')


class DetailView(generic.DetailView):
    model = Order
    template_name = 'detail.html'


class CreateView(generic.CreateView):
    model = Order
    fields = [f.name for f in Order._meta.get_fields() if f.name != 'id']
    template_name_suffix = '_create_form'

    def get_success_url(self):
        return reverse('orders:list')


class UpdateView(generic.UpdateView):
    model = Order
    fields = [f.name for f in Order._meta.get_fields() if f.name != 'id']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('orders:detail', kwargs={'pk': self.object.id})


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-purchase_date')
    serializer_class = OrderSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('order_id', 'marketplace', 'purchase_date',
                     'items', 'amount', 'currency', 'shipping')