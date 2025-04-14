from rest_framework import generics,mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer


#######################################################################
"""
# Show all products Apiview
class ProductListAPIview(generics.ListAPIView): 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
product_detail_view = ProductListAPIview.as_view()  # تحويل الكلاس إلى دالة عرض

"""
# Do the same work of the below code
# Product list view using mixins

class ProductMixinView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):  # Http => GET
        return self.list(request, *args, **kwargs)

product_mixin_view = ProductMixinView.as_view()
######################################################################
"""
# create new product Apiview
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
"""
# Do the same work of the below code
# Product create view using mixins

class ProductCreateMixinView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):  # POST method
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):  # تخصيص الحفظ
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or title
        serializer.save(content=content)


product_create_mixin_view = ProductCreateMixinView.as_view()
######################################################################
"""
# Show one Porduct Apiview by Id
class ProductDetailGenericView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_detail_view = ProductDetailGenericView.as_view() 
"""
class ProductDetailMixinView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):  # GET method
        return self.retrieve(request, *args, **kwargs)


product_detail_mixin_view = ProductDetailMixinView.as_view()
######################################################################
# Updata the product Apiview
class ProductUpdateAPIview(generics.UpdateAPIView):  # عرض تفاصيل منتج واحد
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    def perform_update(self, serializer):  # هذه الدالة يجب أن تكون داخل CreateAPIView فقط!
        instance = serializer.save()
        if instance.content:
            instance.content = instance.title

product_update_view = ProductUpdateAPIview.as_view()  # تحويل الكلاس إلى دالة عرض


class ProductDestroyAPIView(generics.DestroyAPIView):  # عرض تفاصيل منتج واحد
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    def perform_update(self, instance):  # هذه الدالة يجب أن تكون داخل CreateAPIView فقط!
        super().preform_destroy(instance)

product_delete_view = ProductDestroyAPIView.as_view()  # تحويل الكلاس إلى دالة عرض


# Compo view
"""
if method => GET and pk return product detail view
if method => GET and no pk return product list view
if method => POST return product create view
"""
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
