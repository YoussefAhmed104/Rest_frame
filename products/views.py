from rest_framework import generics,mixins,permissions,authentication
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsStaffEditorPermissions

"""
permission_classes = [permissions.] 
1 => IsAuthenticated => يجب أن يكون المستخدم مسجلاً للدخول
2 => IsAuthenticatedOrReadOnly => يجب على المستخدم انا يكون مسجل والا فلن يستطيع الا القرائة فثط
3 => DjangoModelPermissions => يجعل للمستخدم صلاحيات معينه انت تحددها
"""
#######################################################################
class ProductMixinView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser,IsStaffEditorPermissions]

    def get(self, request, *args, **kwargs):  # Http => GET
        return self.list(request, *args, **kwargs)

product_mixin_view = ProductMixinView.as_view()
######################################################################
class ProductCreateMixinView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermissions]

    def post(self, request, *args, **kwargs):  # POST method
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):  # تخصيص الحفظ
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or title
        serializer.save(content=content)


product_create_mixin_view = ProductCreateMixinView.as_view()
######################################################################
class ProductDetailMixinView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermissions]

    def get(self, request, *args, **kwargs):  # GET method
        return self.retrieve(request, *args, **kwargs)


product_detail_mixin_view = ProductDetailMixinView.as_view()
######################################################################
class ProductUpdateAPIview(generics.UpdateAPIView):  # عرض تفاصيل منتج واحد
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermissions]

    def perform_update(self, serializer):  # هذه الدالة يجب أن تكون داخل CreateAPIView فقط!
        instance = serializer.save()
        if instance.content:
            instance.content = instance.title

product_update_view = ProductUpdateAPIview.as_view()  # تحويل الكلاس إلى دالة عرض


class ProductDestroyAPIView(generics.DestroyAPIView):  # عرض تفاصيل منتج واحد
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermissions]

    def perform_update(self, instance):  # هذه الدالة يجب أن تكون داخل CreateAPIView فقط!
        super().preform_destroy(instance)

product_delete_view = ProductDestroyAPIView.as_view()  # تحويل الكلاس إلى دالة عرض
