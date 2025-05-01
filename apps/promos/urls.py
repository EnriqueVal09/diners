from django.urls import path
from .views import PromoListView

urlpatterns = [
    path("", PromoListView.as_view(), name="promos_list"),
]
