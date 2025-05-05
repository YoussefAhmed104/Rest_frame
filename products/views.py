from rest_framework import generics, mixins, permissions, authentication
from .models import Product
from .serializers import ProductSerializer
from api.permissions import IsStaffEditorPermissions
from api.mixins import StaffEsitorPermissionsMixin
from api.authentication import TokenAuthentication
"""
permission_classes = [permissions.] 
1 => IsAuthenticated => يجب أن يكون المستخدم مسجلاً للدخول
2 => IsAuthenticatedOrReadOnly => يجب على المستخدم انا يكون مسجل والا فلن يستطيع الا القرائة فثط
3 => DjangoModelPermissions => يجعل للمستخدم صلاحيات معينه انت تحددها
"""


#######################################################################
class ProductListCreateAPIView(
    StaffEsitorPermissionsMixin,
    generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title
        serializer.save(content=content)
        # send a Django signal


product_list_create_view = ProductListCreateAPIView.as_view()


######################################################################
class ProductDetailAPIView(
    StaffEsitorPermissionsMixin,
    generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk' ??


product_detail_view = ProductDetailAPIView.as_view()


class ProductUpdateAPIView(
    StaffEsitorPermissionsMixin,
    generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            ##


product_update_view = ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(
    StaffEsitorPermissionsMixin, 
    generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        # instance
        super().perform_destroy(instance)


product_destroy_view = ProductDestroyAPIView.as_view()

# Mixins combo view
class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):  # HTTP -> get
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = "this is a single view doing cool stuff"
        serializer.save(content=content)

    # def post(): #HTTP -> post


product_mixin_view = ProductMixinView.as_view()
