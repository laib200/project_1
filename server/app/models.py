from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Meals(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=360)

    def number_of_ratings(self):
        ratings = Rating.objects.filter(meal =self)
        return len(ratings)

    def average_rating(self):
        ratings = Rating.objects.all()
        total = 0
        for rating in ratings:
            total += rating.stars
        if len(ratings) > 0: 
            return total / len(ratings)
        else:
            return 0

    def __str__(self) -> str:
        return self.title


class Rating(models.Model):
    meal = models.ForeignKey(Meals, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self) -> str:
        return self.meal.title

    class Meta:
        unique_together = (("user", "meal"),)
        index_together = (("user", "meal"),)
