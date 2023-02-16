from pyexpat import model
from django.shortcuts import render
import json
from django.forms.models import model_to_dict
from django.http import JsonResponse,HttpResponse
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer
from django.shortcuts import get_object_or_404

from rest_framework import generics,permissions,authentication
from products.permissions import IsStaffEditiorPermission
from api.authentication import TokenAuthentication
from api.mixins import StaffEditorPermissionMixin,UserQuerySetMixin


class ProductListCreateView(generics.ListCreateAPIView,StaffEditorPermissionMixin,UserQuerySetMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

   
    
    def perform_create(self, serializer):
        print(serializer.validated_data)
        
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('contenst') or None
        # email = serializer.validated_data.pop('email')
        
        if content is None:
            content = title
        

        serializer.save(user = self.request.user,contenst=content)
    
    # def get_queryset(self,*args,**kwargs):
    #     request = self.request
    #     user = request.user
    #     print(user)
    #     qs =super().get_queryset(*args,**kwargs)
    #     if not user.is_authenticated:
    #         return Product.objects.none()

    #     return qs.filter(user=user)  # this section was used before using the mixins called UserQuerySetMixin
       
        # return super().get_queryset(*args,**kwargs) 


        






#for django rest_framework generics listapiview

# class ProductListAPIView(generics.ListAPIView):
# despite This only list api view class, we can use ListCreateAPIView like below

# class ProductListCreateView(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     # authentication_classes =[authentication.SessionAuthentication,authentication.TokenAuthentication]  # if authentication is defined as default in settings.py , it need not to be written here
#     # authentication_classes =[authentication.SessionAuthentication,TokenAuthentication] # this only tokenauthentication is the class defined under api/authentication

#     # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     permission_classes = [IsStaffEditiorPermission]
#     # permission_classes = [permissions.IsAdminUser, IsStaffEditiorPermission]  # Using this we won't need has_permission in permissions.py and also ordering of admin and staff is important in this permission_classes list 


#     # permission_classes = [permissions.DjangoModelPermissions]
    
#     def perform_create(self, serializer):
#         print(serializer.validated_data)
        
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('contenst') or None
        
#         if content is None:
#             content = title
        

#         serializer.save(contenst=content)

# In above ListCreateAPIView, It tries to create when post and tries to list queryset when get




#for django rest_framework generic Createapiview


# class ProductCreateView(generics.CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    
#     def perform_create(self, serializer):
#         print(serializer.validated_data)
        
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('contenst') or None
        
#         if content is None:
#             content = title
        

#         serializer.save(contenst=content)
#send Django signal



#for django rest_framework generic retriveapiview

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    lookup_field='pk'


#for api view and serializer concept using post

# @api_view(['POST'])
# def apitest(request,*args,**kwargs):
#     data={}
#     serializer = ProductSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
        
#         # instance = serializer.save()
#         data = serializer.data
#         return Response(data)
    
#     return Response({"Invalid":"bad data"},status=404)

#In above we received data in post method and we used serializer to convert to dictionary and proper management. In case of invalid serializer it returns the raised exception in the client side. Client sends the data using post method,this function sends to serializer and receives the dictionary format data and returns back to client.
        
    


    

    



# @api_view(['GET'])
# def apitest(request,*args,**kwargs):
#     #The work of above api_view decorator can be done as:
#     # if request.method !='GET':
#     #     return Response({'detail':"Post not allowed"},status=405)
    
#     model_values =Product.objects.all().order_by("?").first()
#     data = {}
#     # data= model_to_dict(model_values,fields=['id','title','price'])  #this can be used to directly convert to dictionary
#     # on adding price field, the data isn't converted to json string using json.dumps
#     if model_values:
#         # data= model_to_dict(model_values,fields=['id','title','price','sale_price']) 

#         data = ProductSerializer(model_values).data


#         # data['id']=model_values.id
#         # data['title'] = model_values.title
#         # data['content'] = model_values.contenst
#         # data['price'] = model_values.price
        
#     # return JsonResponse(data)
#     # return HttpResponse(data)
#     # json_data_str = json.dumps(data)
#     # return HttpResponse(json_data_str,headers={'content-type':'application/json'})
    

#     return Response(data)
