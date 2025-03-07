from django.http import JsonResponse ,HttpResponse
from django.forms.models import model_to_dict
from products.models import Product


def api_home(request, *args, **kwargs):
    # جلب منتج عشوائي من قاعدة البيانات باستخدام order_by("?") وأخذ أول نتيجة
    rand_pro = Product.objects.all().order_by("?").first()
    data={}
    # if rand_pro:
    #     data['id']=rand_pro.id
    #     data['title']=rand_pro.title
    #     data['content']=rand_pro.content
    #     data['price']=rand_pro.price
    #is semilar to
    if rand_pro:
        data = model_to_dict(rand_pro) #لو عايز تعمل فلتر للحجات الي تظهر
    return JsonResponse(data)  
