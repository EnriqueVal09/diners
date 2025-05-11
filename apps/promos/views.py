from django.shortcuts import render
from django.views.generic import ListView

from .models import Promo
from apps.diners.models import Diner

class PromoListView(ListView):
    model = Promo
    template_name = "promos/promos_list.html"
    context_object_name = "promos"

    def get_queryset(self):
        diner = Diner.objects.first()
        return Promo.objects.filter(
            diner=diner, 
            active=True
            ).order_by("-created_at").prefetch_related("diner")
    
