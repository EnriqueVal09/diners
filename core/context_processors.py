from apps.diners.models import Diner
from apps.menus.models import Category

def diner_context(request):
    diner = Diner.objects.first()
    return {"diner": diner}

def category_context(request):
    categories = Category.objects.all()
    return {"categories": categories}
