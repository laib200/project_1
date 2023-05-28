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
            user = User.objects.get(username=username)
            stars = request.get('stars')
            try:
                rating = Rating.objects.get(user=user.id, meal=meal.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating=rating,many=False)
                response = {
                    'message': 'Rating updated',
                    'data': serializer.data 
                }
                return Response(response,status=status.HTTP_200_OK)
            except:
                rating = Rating.objects.create(meal=meal,user=user,stars=stars)
        else:
            response = {
                "message": 'bad request'
            }
            return Response(response,status=status.HTTP_400_BAD_REQUEST)

class ViewRating(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer