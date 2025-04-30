from django.shortcuts import render

from django.views.generic import ListView
from .models import Meal, Category
from apps.diners.models import Diner

class CategoryListView(ListView):
    model = Category
    template_name = "meals/all_meal_list.html"
    context_object_name = "categories"

    def get_queryset(self):
        diner = Diner.objects.first()
        return Category.objects.filter(
            diner=diner,
            parent_category__isnull=True
        ).prefetch_related(
            'meals', 
            'subcategories__meals', 
            'subcategories__subcategories__meals'
        ).order_by('order', 'name')


