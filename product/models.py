from django.db import models
# Create your models here.
class Product(models.Model):
    product_name= models.CharField(max_length=255)
    product_description= models.CharField(max_length=1000)
    product_price= models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)