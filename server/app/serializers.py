from rest_framework.serializers import ModelSerializer
from .models import Meals, Rating
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}, "required": True}

class MealsSerializer(ModelSerializer):
    class Meta:
        model = Meals
        fields = ["title", "description", "number_of_ratings", "average_rating"]


class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"
