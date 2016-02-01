from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Order(models.Model):
    order_id = models.TextField(primary_key=True, unique=True)
    marketplace = models.TextField(null=True, blank=True)
    purchase_date = models.DateField(null=True, blank=True)
    items = models.IntegerField(null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2,
                                 null=True, blank=True)
    currency = models.TextField(null=True, blank=True)
    shipping = models.DecimalField(max_digits=10, decimal_places=2,
                                   null=True, blank=True)
