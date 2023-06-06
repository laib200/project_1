from rest_framework.viewsets import ModelViewSet
from app.serializers import MealsSerializer, RatingSerializer
from app.models import Meals, Rating
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response



class ViewMeals(ModelViewSet):
    queryset = Meals.objects.all()
    serializer_class = MealsSerializer


    @action(detail=True, methods=["post"])
    def rate_meals(self,request,pk=None,):
        if "stars" in request.data:
            meal = Meals.objects.get(id=pk)
            user = request.user
            stars = request.data["stars"]
            try:
                rating = Rating.objects.get(user=user.id, meal=meal.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                response = {"message": ["Rating updated",], "data": serializer.data}
                return Response(response, status=status.HTTP_301_MOVED_PERMANENTLY)
            except:
                rating = Rating.objects.create(meal=meal, user=user, stars=stars) 
                serializer = RatingSerializer(rating, many=False)
                response = {"massage": ["Rating created",], "data": serializer.data}
                return Response(response, status=status.HTTP_201_CREATED)
        else:
            response = {"stars": ["This field is required.",]}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)



class ViewRating(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    http_method_names = "get"
