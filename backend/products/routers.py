from rest_framework.routers import DefaultRouter

from products.viewsets import ProductViewSet,ProductGenericViewset


router = DefaultRouter()
router.register('products',ProductViewSet,basename='products')
router.register('productsmixins',ProductGenericViewset,basename='products')


urlpatterns = router.urls
# print(urlpatterns)

#not recommended routers as it isn't granular so use urls.py