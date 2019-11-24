from django.contrib import admin
from users import models
# Register your models here.

admin.site.register(models.Profile)
admin.site.register(models.cart)
admin.site.register(models.History)
admin.site.register(models.Payments)