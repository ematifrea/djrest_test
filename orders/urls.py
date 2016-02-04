from django.conf.urls import url

from orders.views import ListView, DetailView, CreateView, UpdateView

urlpatterns = [
    url(r'^list/$', ListView.as_view(), name='list'),
    url(r'^detail/(?P<pk>[0-9]+)/$', DetailView.as_view(), name='detail'),
    url(r'^create/$', CreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>[0-9]+)/$', UpdateView.as_view(), name='update'),
]