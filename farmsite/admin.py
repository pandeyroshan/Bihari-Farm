from django.contrib import admin
from farmsite import models
# Register your models here.

admin.site.register(models.ProductType)
admin.site.register(models.Product)
admin.site.register(models.couponCode)
admin.site.register(models.NewsLetters)
admin.site.register(models.Blogs)
admin.site.register(models.address)
admin.site.register(models.Contact)
admin.site.register(models.testimonial)