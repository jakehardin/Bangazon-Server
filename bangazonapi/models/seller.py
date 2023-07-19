from django.db import models

class Seller(models.Model):
    uid = models.CharField(max_length=50)
    seller_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    profile_image_url = models.URLField()
    email = models.EmailField()
