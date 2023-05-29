from rest_framework.serializers import ModelSerializer
from .models import Meals,Rating
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    model = User.objects.all()
    fields = ['id', 'username', 'password']

class MealsSerializer(ModelSerializer):
    class Meta:
        model = Meals
        fields = ['title','description','number_of_ratings','average_rating']

class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

