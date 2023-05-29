from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from app.serializers import MealsSerializer, RatingSerializer
from app.models import Meals, Rating
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny,IsAuthenticatedOrReadOnly


class ViewMeals(ModelViewSet):
    queryset = Meals.objects.all()
    serializer_class = MealsSerializer

    @action(detail=True, methods=["post"])
    def rate_meals(
        self,
        request,
        pk=None,
    ):
        if "stars" in request.data:
            meal = Meals.objects.get(id=pk)

            username = request.data["username"]

            user = User.objects.get(username=username)

            stars = request.data["stars"]

            try:
                rating = Rating.objects.get(user=user.id, meal=meal.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                response = {"message": "Rating updated", "data": serializer.data}
                return Response(response, status=status.HTTP_301_MOVED_PERMANENTLY)
            except:
                rating = Rating.objects.create(meal=meal, user=user, stars=stars)
                serializer = RatingSerializer(rating, many=False)
                response = {"massage": "Rating created", "data": serializer.data}
                return Response(response, status=status.HTTP_201_CREATED)
        else:
            response = {"message": "bad request"}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class ViewRating(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes =[IsAuthenticatedOrReadOnly,]
    http_method_names = ('get')
