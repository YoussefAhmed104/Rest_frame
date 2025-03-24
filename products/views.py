from rest_framework import generics  # استيراد generics من rest_framework لتوفير واجهات API جاهزة
from .models import Product
from .serializers import ProductSerializer


class ProductDetailAPIview(generics.RetrieveAPIView):  # عرض تفاصيل منتج واحد
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_detail_view = ProductDetailAPIview.as_view()  # تحويل الكلاس إلى دالة عرض


class ProductCreateAPIview(generics.CreateAPIView):  # إضافة منتج جديد
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):  # هذه الدالة يجب أن تكون داخل CreateAPIView فقط!
        # serializer.save(user=self.request.user)  # ربط المنتج بالمستخدم الحالي
        
        print(serializer.is_valid())
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or title  # إذا لم يكن هناك محتوى، استخدم العنوان
        serializer.save(content=content) # حفظ المحتوى


product_create_view = ProductCreateAPIview.as_view()  # تحويل الكلاس إلى دالة عرض
