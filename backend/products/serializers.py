from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product
# from .validators import validate_title
from .validators import validate_hello_title
from .validators import unique_product_title

from api.serializers import UserPublicSerializer



class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user',read_only=True)
    
    # url = serializers.SerializerMethodField(read_only=True)
    # edit_url = serializers.SerializerMethodField(read_only=True)
    # url = serializers.HyperlinkedIdentityField(view_name='product-detail',lookup_field='pk')   # hyperlinkidentidentityfield only works with serializers|||this is preferred method
   
    # title = serializers.CharField(validators=[validate_title])
    title= serializers.CharField(validators=[validate_hello_title,unique_product_title])
    body = serializers.CharField(source='contenst') #fou unified design of serializer we have used body with content as body is the field of another app which is not defined here
    class Meta:
        model= Product
        fields=[
            'owner',
            'user',
            'pk',
            'title',
            'path',
        
        # 'contenst',
        'body',
        'price',
        'sale_price',
        
        # 'url',
        # 'edit_url',
  
        ]

    def get_my_user_data(self,obj):
        return {
            'username' : obj.user.username
        }



    # def get_url(self,obj):
    #     # return f"api/v2/products/{obj.pk}/"
    #     request = self.context.get('request')
    #     if request is None:
    #         return None
    #     return reverse("product-detail",kwargs={'pk':obj.pk},request=request)



    # def get_edit_url(self,obj):
        
    #     request = self.context.get('request')
    #     if request is None:
    #         return None
    #     return reverse("product-edit",kwargs={'pk':obj.pk},request=request)



  








# class ProductInLineSerializer(serializers.Serializer):
#     url = serializers.HyperlinkedIdentityField(view_name='product-detail',lookup_field='pk',read_only=True)
#     title = serializers.CharField(read_only = True) 
# # this is same as UserProductInLineSerializer inside userpublic serializer


# class ProductSerializer(serializers.ModelSerializer):
#     owner = UserPublicSerializer(source='user',read_only=True)
#     # related_products = ProductInLineSerializer(source='user.product_set.all',read_only=True,many=True)
#     my_discount = serializers.SerializerMethodField(read_only=True)
#     my_user_data = serializers.SerializerMethodField(read_only=True)
#     # url = serializers.SerializerMethodField(read_only=True)
#     # edit_url = serializers.SerializerMethodField(read_only=True)
#     # url = serializers.HyperlinkedIdentityField(view_name='product-detail',lookup_field='pk')   # hyperlinkidentidentityfield only works with serializers|||this is preferred method
#     # email = serializers.EmailField(write_only=True)

#     # title = serializers.CharField(validators=[validate_title])
#     title= serializers.CharField(validators=[validate_hello_title,unique_product_title])
#     # name= serializers.CharField(source='title')
#     class Meta:
#         model= Product
#         fields=[
#             'owner',
#             'user',
#             'pk',
#             'title',
#             # 'name',
#         'contenst',
#         'price',
#         'sale_price',
#         'my_discount',
#         # 'url',
#         # 'edit_url',
#         # 'email',
#         'my_user_data',
#         # 'related_products',
#         ]

#     def get_my_user_data(self,obj):
#         return {
#             'username' : obj.user.username
#         }






#     # def validate_title(self,value):
#     #     request = self.context.get('request')
#     #     user= request.user
        

#     #     qs = Product.objects.filter(user=user, title__iexact =value)
#     #     if qs.exists():
#     #         raise serializers.ValidationError(f'{value} is already a product name')
#     #     return value
    
#     # def create(self,validated_data):
#     #     email = validated_data.pop('email')
#     #     print(email)
#     #     # return Product.object.create(**validated_data)
#     #     obj =super().create(validated_data)
#     #     return obj
    
#     # def update(self,instance,validated_data):
#     #     instance.title = validated_data.get('title')
#     #     return instance 
        

#     # def get_url(self,obj):
#     #     # return f"api/v2/products/{obj.pk}/"
#     #     request = self.context.get('request')
#     #     if request is None:
#     #         return None
#     #     return reverse("product-detail",kwargs={'pk':obj.pk},request=request)



#     # def get_edit_url(self,obj):
        
#     #     request = self.context.get('request')
#     #     if request is None:
#     #         return None
#     #     return reverse("product-edit",kwargs={'pk':obj.pk},request=request)



#     def get_my_discount(self,obj):
#         # print(obj.id)
#         # if not hasattr(obj,'id'):
#         #     return None
#         if not isinstance(obj,Product):
#             return None
#         return obj.get_discount() 
