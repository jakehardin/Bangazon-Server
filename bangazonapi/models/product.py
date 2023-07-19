from django.db import models
from .seller import Seller

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=100)
    image = models.URLField()
    uid = models.CharField(max_length=100)
    
