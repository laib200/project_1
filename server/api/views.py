from rest_framework.viewsets import ModelViewSet
from app.serializers import MealsSerializer,RatingSerializer
from app.models import Meals,Rating



class ViewMeals(ModelViewSet):
    queryset = Meals.objects.all()
    serializer_class = MealsSerializer

class ViewRating(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer