from django.db import models
from core.models import TimeStampedModel

class Product(TimeStampedModel):

    name = models.CharField("이름", max_length=150, unique=True)
    price = models.IntegerField("가격")

    def __str__(self):
        return self.name
