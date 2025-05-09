from .serializers import ProductSerializer
from .models import Product
from rest_framework import viewsets,mixins


# لو عايز كلاس فيه كل حاجه(get, post, put, delete)
class ProductViewSet(viewsets.ModelViewSet):
    """
    get => list
    get => retrieve
    post => create
    put => update
    patch => partial update
    delete => destroy
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


# لو عايز تخصص كلاس فيه البريمشن الي تختارها 
class ProductMixinsViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):
    
    """
    get => list
    get => retrieve
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
