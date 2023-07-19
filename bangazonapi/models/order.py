from django.db import models
from .customer import Customer
from .seller import Seller

class Order(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    completed = models.BooleanField(null=True, blank=True)
    date = models.DateField()
