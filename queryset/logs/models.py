from products.models import Product
from django.db import models
from core.models import TimeStampedModel

class OrderLog(models.Model):
    
    created = models.DateTimeField()
    is_cancel = models.BooleanField(default=False)
    product = models.ForeignKey('products.Product', related_name='order_log', on_delete=models.CASCADE)

