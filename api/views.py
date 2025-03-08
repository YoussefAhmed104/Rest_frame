from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializers



@api_view(["POST","GET"])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data={}
    if instance:
        data = ProductSerializers(instance).data #بيجيب الداتا و يحولها ل Json file و يحفظها في الداتا 
    return Response(data)  
