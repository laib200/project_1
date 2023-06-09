from rest_framework.routers import DefaultRouter
from django.urls import path,include
from api import views

routers = DefaultRouter()
routers.register('meals',views.ViewMeals,basename='meals')
routers.register('rating',views.ViewRating,basename='rating')

urlpatterns =[
    path('',include(routers.urls))
]   