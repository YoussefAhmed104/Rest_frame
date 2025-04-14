from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/", views.product_detail_mixin_view, name="product-detail"),
    path("<int:pk>/update/", views.product_update_view, name="product-update"),
    path("<int:pk>/delete/", views.product_delete_view, name="product-delete"),
    path("create/", views.product_create_mixin_view, name="product-create"),
    path("list/", views.product_mixin_view, name="product-list"),
]
