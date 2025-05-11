from django.views.generic import TemplateView

from apps.diners.models import Diner
from apps.promos.models import Promo
from apps.menus.models import Category

class HomeView(TemplateView):
    template_name = "home/meals_promos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        diner = Diner.objects.first()

        context["promos"] = (
            Promo.objects.filter(diner=diner, active=True)
            .order_by("-created_at")
            .prefetch_related("diner")
        )

        context["categories"] = (
            Category.objects.filter(diner=diner, parent_category__isnull=True)
            .prefetch_related(
                "meals", "subcategories__meals", "subcategories__subcategories__meals"
            )
            .order_by("order", "name")
        )

        return context
