from unicodedata import category
from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField()
    category=models.CharField(max_length=20)
    company=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.name

