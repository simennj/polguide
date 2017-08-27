import csv
from contextlib import closing
from django.db import transaction

import requests

from django.core.management.base import BaseCommand, CommandError
from guide.models import Product, Category, ProductHistory


class Command(BaseCommand):
    help = 'Retrieve updated data from vinmonopolet'

    URL = "https://www.vinmonopolet.no/medias/sys_master/products/products/hbc/hb0/8834253127710/produkter.csv"

    def handle(self, *args, **options):
        with closing(requests.get(self.URL)) as download:
            reader = csv.DictReader(download.content.decode('iso-8859-1').splitlines(), delimiter=';')
            self.stdout.write('File downloaded, {} items'.format(reader.line_num))
            with transaction.atomic():
                for row in reader:
                    if len(row) != 36:
                        self.stdout.write('{} has incorrect amount of fields and is skipped'.format(row['Varenavn']))
                        continue
                    volume = float(row['Volum'].replace(',', '.'))
                    alcohol = float(row['Alkohol'].replace(',', '.'))
                    price = float(row['Pris'].replace(',', '.'))
                    alcohol_price = price / (volume * alcohol if alcohol else 0.01)
                    category, _ = Category.objects.get_or_create(name=row['Varetype'])
                    product, _ = Product.objects.update_or_create(
                        id=row['Varenummer'],
                        defaults={
                            'name': row['Varenavn'],
                            'category': category,
                            'volume': volume,
                            'alcohol': alcohol,
                            'price': price,
                            'alcohol_price': alcohol_price
                        }
                    )
                    timestamp = row['Datotid']
                    ProductHistory.objects.update_or_create(
                        product=product,
                        timestamp=timestamp,
                        defaults={
                            'price': price,
                            'alcohol_price': alcohol_price
                        }
                    )
