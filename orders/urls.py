from django.conf.urls import url

import orders.views as views


urlpatterns = [
    url(r'^list/$', views.ListView.as_view(), name='list'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^create/$', views.CreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.UpdateView.as_view(), name='update'),
]