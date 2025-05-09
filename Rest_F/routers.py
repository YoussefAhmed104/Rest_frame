from rest_framework.routers import DefaultRouter
from products.viewsets import ProductViewSet, ProductMixinsViewSet


router = DefaultRouter()
router.register("products", ProductMixinsViewSet, basename="products")
print(router.urls)
urlpatterns = router.urls
