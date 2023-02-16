from products.models import Product
from products.serializers import ProductSerializer
from rest_framework import generics,mixins
 




class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    lookup_field='pk'

    def perform_update(self,serializer):
        instance = serializer.save()
        if serializer.is_valid:
            if not instance.contenst:
                instance.contenst= instance.title


class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    lookup_field='pk'

    def perform_destroy(self,instance):
        super().perform_destroy(instance)




# Using mixin for knowledege not recommended for normal use 
class ProductMixinView(mixins.CreateModelMixin, mixins.ListModelMixin,mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def get(self,request,*args,**kwargs):
        print(args,kwargs)
        pk = kwargs.get('pk')  # this can be used instead of writing pk=None in parameter as before

        if pk is not None:
            return self.retrieve(request,*args,**kwargs)

    def post(self ,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
        ## we can still do this ->perform_create(self,serializer):

    def update(self,request,*args,**kwargs):
        
        return self.update(request,*args,**kwargs)
         
        

