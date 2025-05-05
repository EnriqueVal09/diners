from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

from .models import Meal, Category
from apps.diners.models import Diner

class CategoryListView(ListView):
    model = Category
    template_name = "meals/full_menu.html"
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

class MealByCategoryListView(ListView):
    model = Meal
    template_name = "meals/meals_by_category.html"
    context_object_name = "meals"

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return Meal.objects.filter(
            category__id=category_id,
            available=True
        ).order_by("name").prefetch_related("options")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agregamos la categoría para mostrar su nombre en el template
        context['category'] = get_object_or_404(Category, id=self.kwargs.get('category_id'))
        return context

