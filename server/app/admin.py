from django.contrib import admin
from .models import Meals, Rating

# Register your models here.


class RatingAdmin(admin.ModelAdmin):
    list_display = ["id", "meal", "user", "stars"]
    list_filter = ["meal", "user"]
    list_display_links = ["id", "meal", "user", "stars"]


class MealsAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description"]
    search_fields = ["title", "description"]
    list_filter = ["title", "description"]
    list_display_links = ["id", "title", "description"]

admin.site.register(Meals, MealsAdmin)
admin.site.register(Rating, RatingAdmin)
