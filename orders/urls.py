from django.conf.urls import url

from orders.views import ListView,DetailView, SearchView

urlpatterns = [
    url(r'^$', ListView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$', DetailView.as_view(), name='detail'),
    url(r'^(?P<search>\w+)$', SearchView.as_view(), name='search')
]