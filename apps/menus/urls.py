from django.urls import path
from .views import CategoryListView, MealByCategoryListView

urlpatterns = [
    path("", CategoryListView.as_view(), name="full-menu"),
    path('category/<uuid:category_id>/', MealByCategoryListView.as_view(), name='meals_by_category'),
]
