from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer
from django.http import JsonResponse


@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)