from django.db import models
from rest_framework import serializers

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(null=True , blank= True)
    price = models.DecimalField( max_digits=15, decimal_places=2 , default= 99.99)

    def __str__(self):
        return self.title
    @property
    def sel_price(self):
        return "%.2f" %(float(self.price) *0.8) #حساب سعر المنتج بعد الخصم 20%
    
    def get_discount(self):
        return "20%"