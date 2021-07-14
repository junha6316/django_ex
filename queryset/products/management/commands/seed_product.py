import random
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone
from sys import stdout

from products.models import Product

class Command(BaseCommand):

    def handle(self, *args, **options):
        
        dates = [timezone.now()-timedelta(days=i) for i in range(3)]
        prices = {'카카오':16000, '네이버':44000, '쿠팡':7000, '배민':15000, '라인':20000, '당근':22000}
        names = list(prices.keys())
        for name in names:    
            Product.objects.create(
                name = name,
                price = prices[name]
            )
            
        self.stdout.write(self.style.SUCCESS("Product가 생성되었습니다."))

           

