from django.db import models
from django.contrib.auth.models import User
from farmsite import models as farm_model
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,blank=True)
    phoneNumber = models.CharField(max_length=50,blank=True)
    Add1 = models.CharField(max_length=300,blank=True)
    Add2 = models.CharField(max_length=200,blank=True)
    Add3 = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.user.username

class cart(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    productID = models.ManyToManyField(farm_model.Product,blank=True)

    def __str__(self):
        return self.user.username+' Cart'
    
    class Meta:
        verbose_name = 'Carts'
        verbose_name_plural = 'Carts'

class wishList(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    productID = models.ManyToManyField(farm_model.Product,blank=True)

    def __str__(self):
        return self.user.username+' Wishlist'
    
    class Meta:
        verbose_name = 'Wishlists'
        verbose_name_plural = 'Wishlists'


class History(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    products = models.ManyToManyField(farm_model.Product,blank=True)

    def __str__(self):
        return self.user.username+' History'
    
    class Meta:
        verbose_name = 'Order History'
        verbose_name_plural = 'Order History'


class Payments(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    payment = models.IntegerField("Money Paid")
    TimeOfCheckout = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username+' Payment'
    
    class Meta:
        verbose_name = 'Payment History'
        verbose_name_plural = 'Payment History'