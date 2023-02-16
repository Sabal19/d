from django.urls import path
from . import views,views2


urlpatterns = [
    # path('',views.apitest,name='apitest'),
    # path('<int:pk>/',views.ProductDetailAPIView.as_view()),
    path('<int:pk>/',views.ProductDetailAPIView.as_view(),name='product-detail'),

    path('',views.ProductListCreateView.as_view()),
    # path('',views.product_alt_view),
    # path('<int:pk>/',views.product_alt_view),
    # path('<int:pk>/update/',views2.ProductUpdateAPIView.as_view()),
    # path('<int:pk>/update/',views2.ProductUpdateAPIView.as_view(),name='product-edit'),
    # path('<int:pk>/delete/',views2.ProductDeleteAPIView.as_view()),
    # path('',views2.ProductMixinView.as_view()),
    # path('<int:pk>/',views2.ProductMixinView.as_view()),
    # path('<int:pk>/update/',views2.ProductMixinView.as_view()),
]