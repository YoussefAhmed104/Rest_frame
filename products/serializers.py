from rest_framework import serializers 
from .models import Product  

class ProductSerializers(serializers.ModelSerializer):  
    discount = serializers.SerializerMethodField(read_only=True)  
    # إنشاء حقل `discount` يُملأ بواسطة دالة مخصصة وليس من قاعدة البيانات مباشرة

    class Meta:  
        model = Product 
        fields = [ 
            'id',  
            'title',  
            'content',
            'price', 
            'sel_price',  
            'discount',  
        ]

    def get_discount(self, obj):  
        return obj.get_discount()  # استدعاء دالة `get_discount` من كلاس Product لحساب الخصم
