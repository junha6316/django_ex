import random
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone
from sys import stdout

from django.core.management.base import BaseCommand

from products.models import Product
from logs.models import OrderLog

class Command(BaseCommand):

    def handle(self, *args, **options):
        
        dates = [timezone.now()-timedelta(days=i) for i in range(3)]
        products = Product.objects.all()
        for _ in range(20):
            product = random.choice(products)
            created = random.choice(dates)    
            OrderLog.objects.create(
                created = created,
                product = product,
            )
            
        self.stdout.write(self.style.SUCCESS("Log가 생성되었습니다."))

           

