from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from app.serializers import MealsSerializer,RatingSerializer
from app.models import Meals,Rating
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response



class ViewMeals(ModelViewSet):
    queryset = Meals.objects.all()
    serializer_class = MealsSerializer
    
    @action(detail=False, methods=['post'])
    def rate_meals(self, request,pk=None,):
        if 'stars' in request.data:
            meal = Meals.objects.get(id=pk)
            username =  request.get('username')
            user = User.objects.filter(username=username)
            stars = request.get('stars')
            try:
                pass
            except:
                pass
        else:
            pass

class ViewRating(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer