from rest_framework import viewsets,mixins

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    '''
    get -> list ->queryset
    get -> retrieve -> Product Instance Detail View
    post ->create -> new instance
    put -> update
    patch -> Partial Update
    delete -> destroy
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' # this is default 



class ProductGenericViewset(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    '''
    get -> list ->queryset
    get -> retrieve -> Product Instance Detail View
    
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


# Product_list_view = ProductGenericViewset.as_view({'get':'list'})
# Product_retrieve_view=ProductGenericViewset.as_view({'get':'retrieve'})

# these above did't work on putting on routers.py as router.register('productsmixins',viewsets.Product_list_view,basename='products')