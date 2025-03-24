from rest_framework import generics  # استيراد generics من rest_framework لتوفير واجهات API جاهزة
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer


class ProductListAPIview(generics.ListAPIView):  # عرض تفاصيل منتج واحد
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_detail_view = ProductListAPIview.as_view()  # تحويل الكلاس إلى دالة عرض


class ProductListCreateAPIview(generics.ListCreateAPIView):  # إضافة منتج جديد
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):  # هذه الدالة يجب أن تكون داخل CreateAPIView فقط!
        # serializer.save(user=self.request.user)  # ربط المنتج بالمستخدم الحالي

        print(serializer.is_valid())
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or title  # إذا لم يكن هناك محتوى، استخدم العنوان
        serializer.save(content=content) # حفظ المحتوى


product_create_view = ProductListCreateAPIview.as_view()  # تحويل الكلاس إلى دالة عرض


@api_view(['GET' , 'POST'])
def product_alt_view(request ,pk = None , *args , **kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:
            # detail view
            obj = get_object_or_404(Product ,pk=pk)
            data = ProductSerializer(obj , many = False).data
            return Response(data)
        # list view
        queryset = Product.objects.all()
        data = ProductSerializer(queryset , many=True).data
        return Response(data)
    elif method == "POST":
        """
        DRF API View
        """
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get("title")
            content = serializer.validated_data.get("content") or title  # إذا لم يكن هناك محتوى، استخدم العنوان
            serializer.save(content=content) # حفظ المحتوى
            return Response(serializer.data)
        return Response({"invalid": "not good data"}, status=400)
