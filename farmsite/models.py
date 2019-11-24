from django.db import models
from django.contrib.auth.models import User
import random
# Create your models here.

class ProductType(models.Model):
    productType = models.CharField(max_length=300)

    def __str__(self):
        return self.productType

class Product(models.Model):
    productType = models.ForeignKey(ProductType,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image= models.ImageField(upload_to='Product Photo')
    weight = models.CharField(max_length=10)
    price = models.IntegerField()
    available = models.BooleanField()
    discount = models.IntegerField()
    discription = models.TextField()
    prime = models.BooleanField()

    def __str__(self):
        return self.name