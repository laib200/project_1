from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
import uuid

# Create your models here.
class Meals(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    meal = models.ForeignKey(Meals, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self) -> str:
        return self.meal.title

    class Meta:
        unique_together = (("user", "meal"),)
        index_together = (("user", "meal"),)



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def TokenCerated(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
