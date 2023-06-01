
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token 
from rest_framework.routers import DefaultRouter
from api import auth
auth_routers = DefaultRouter()
auth_routers.register('register',auth.ViewRegister,basename='register')
auth_routers.register('login',auth.ViewLogin,basename='login')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token/',  obtain_auth_token),
    path('',include("urls.urls")),
    path('auth/',include(auth_routers.urls)),
]
