from tkinter.font import names
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)





urlpatterns=[
    path('auth/', obtain_auth_token),
    path('token/', TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('token/', TokenVerifyView.as_view(),name='token_verify_pair'),
    path('token/', TokenRefreshView.as_view(),name='token_refresh_pair'),
    path('apihome/',views.api_home,name='api_home'),
    
]