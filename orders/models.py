from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Order(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, auto_created=True)
    order_id = models.CharField(unique=True, max_length=255)
    marketplace = models.CharField(null=True, blank=True, max_length=255)
    purchase_date = models.DateField(null=True, blank=True)
    items = models.IntegerField(null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2,
                                 null=True, blank=True)
    currency = models.CharField(null=True, blank=True, max_length=4)
    shipping = models.DecimalField(max_digits=10, decimal_places=2,
                                   null=True, blank=True)
