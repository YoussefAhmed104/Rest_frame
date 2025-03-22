from rest_framework import generics  # استيراد generics من rest_framework لتوفير واجهات API جاهزة
from .models import Product  
from .serializers import ProductSerializer 

class ProductDetailAPIview(generics.RetrieveAPIView):  # تعريف فئة API لعرض تفاصيل منتج واحد
    queryset = Product.objects.all()  # تحديد جميع كائنات Product كاستعلام أساسي
    serializer_class = ProductSerializer  # تحديد ProductSerializer كفئة التسلسل المستخدمة