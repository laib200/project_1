from rest_framework.serializers import ModelSerializer
from .models import Meals,Rating


class UserSerializer(ModelSerializer):
    pass

class MealsSerializer(ModelSerializer):
    class Meta:
        model = Meals
        fields = '__all__'

class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

