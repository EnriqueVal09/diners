from django.shortcuts import render

from django.views.generic import ListView
from .models import Meal

class MealListView(ListView):
    model = Meal
    template_name = "meals/meal_list.html"
    context_object_name = "meals"

    def get_queryset(self):
        return Meal.objects.all()

