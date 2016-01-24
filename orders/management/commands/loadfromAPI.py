from django.core.management.base import BaseCommand, CommandError

import requests
import xmltodict
from orders.models import Order

class Command(BaseCommand):
    help = 'Loads data into the db from http://test.lengow.io/orders-test.xml'

    def handle(self, *args, **options):
        response = requests.get('http://test.lengow.io/orders-test.xml')
        orders_dict = xmltodict.parse(response.content)
        for o in orders_dict['statistics']['orders']['order']:
            order, created = Order.objects.\
                get_or_create(order_id=o['order_id'],
                              defaults={'marketplace': o['marketplace'],
                                        'purchase_date': o['order_purchase_date'],
                                        'items': o['order_items'],
                                        'amount': o['order_amount'],
                                        'currency': o['order_currency'],
                                        'shipping': o['order_shipping']
                                        })
            if created:
                self.stdout.write(self.style.SUCCESS('Successfully wrote order with id "%s"' % o['order_id']))
            else:
                self.stdout.write(self.style.NOTICE('Order with id "%s" already exists' % o['order_id']))