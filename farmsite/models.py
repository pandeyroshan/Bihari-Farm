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
    nutFacts = models.TextField()
    prime = models.BooleanField()

    def __str__(self):
        return self.name

class couponCode(models.Model):
    code = models.CharField(max_length=15,blank=False)
    products = models.ManyToManyField(Product)
    validity = models.DateTimeField(blank=False)
    limit = models.IntegerField(blank=False)


    def __str__(self):
        return self.code
    class Meta:
        verbose_name = 'Coupon Codes'
        verbose_name_plural = 'Coupon Code'

class NewsLetters(models.Model):
    email = models.EmailField(blank=False)

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'Newsletters'
        verbose_name_plural = 'NewsLetters'

class Blogs(models.Model):
    topic = models.CharField(max_length=500,blank=False)
    image = models.ImageField(upload_to='blogs')
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    content = models.TextField(blank=False)

    def __str__(self):
        return self.topic
    class Meta:
        verbose_name = 'Blogs'
        verbose_name_plural = 'Blogs'

class address(models.Model):
    hofc = models.TextField(max_length=1000,blank=False)
    cofc = models.TextField(max_length=1000,blank=False)
    phNo = models.TextField(max_length=20,blank=False)
    email = models.EmailField(blank=False)
    gmap = models.EmailField(blank=False)

    def __str__(self):
        return "Address"
    
    class Meta:
        verbose_name_plural = 'Address'
        verbose_name = 'Address'

class Contact(models.Model):
    name = models.TextField(max_length=200,blank=False)
    email = models.EmailField(blank=False)
    message = models.TextField(blank=False)

    def __str__(self):
        return 'Message from '+self.name
    
    class Meta:
        verbose_name = 'Messages'
        verbose_name_plural = 'Messages'

class testimonial(models.Model):
    image = models.ImageField(upload_to='Testimonial')
    name= models.CharField(max_length=100,blank=False)
    text = models.TextField(max_length=500)
    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Testimonial'
        verbose_name = 'Testimonial'