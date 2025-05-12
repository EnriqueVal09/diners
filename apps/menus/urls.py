from django.urls import path
from .views import MealByCategoryListView, CategoryMealsListView

urlpatterns = [
    path("", CategoryMealsListView.as_view(), name="full-menu"),
    path('category/<uuid:category_id>/', MealByCategoryListView.as_view(), name='meals_by_category'),
]
