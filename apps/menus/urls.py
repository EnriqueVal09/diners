from django.urls import path
from .views import MealListView

urlpatterns = [
    path("", MealListView.as_view(), name="meal-list"),
]
