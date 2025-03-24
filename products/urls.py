from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/", views.product_detail_view, name="product-detail"),
    path("create/", views.product_create_view, name="product-create"),
]
