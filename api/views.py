from django.http import JsonResponse  # استيراد JsonResponse لإرجاع البيانات كـ JSON
import json  # استيراد مكتبة json للتعامل مع البيانات بصيغة JSON

def api_home(request, *args, **kwargs):
    # request -> HttpRequest -> Django
    # print(dir(request))  # لعرض جميع الخصائص والوظائف المتاحة في كائن الطلب (request)
    
    # طباعة معاملات الاستعلام (Query Parameters) المرسلة مع الطلب عبر URL مثل ?name=Youssef
    print(request.GET)  
    
    # طباعة البيانات المرسلة مع الطلب إذا كان من نوع POST
    print(request.POST)  

    body = request.body  # جلب بيانات الطلب (request body) كـ byte string
    data = {}  # تعريف متغير لحفظ البيانات المستخرجة
    
    try:
        data = json.loads(body)  # تحويل البيانات من JSON string إلى قاموس (Dictionary) في بايثون
    except:
        pass  # تجاوز أي خطأ قد يحدث إذا لم يكن المحتوى بصيغة JSON
    
    print(data)  # طباعة البيانات التي تم استخراجها من الطلب
    
    # تحويل معاملات الاستعلام (Query Parameters) إلى قاموس وإضافتها للبيانات المسترجعة
    data['params'] = dict(request.GET)  
    
    # جلب الهيدرز (Headers) الخاصة بالطلب وتحويلها إلى قاموس
    data['headers'] = dict(request.headers)  
    
    # استخراج نوع المحتوى (Content-Type) من الطلب
    data['content_type'] = request.content_type  
    
    # إرجاع البيانات كـ JSON response
    return JsonResponse(data)  
