from rest_framework.viewsets import ModelViewSet
from app.serializers import Meals,Rating
from app.models import Meals,Rating



class ViewMeals(ModelViewSet):
    queryset = Meals.objects.all()
    serializer_class = Meals

class ViewRating(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = Rating