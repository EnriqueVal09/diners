from apps.diners.models import Diner
from apps.menus.models import Category

def diner_context(request):
    try:
        diner = Diner.objects.first()
    except:
        diner = None
    return {"diner": diner}

def category_context(request):
    try:
        categories = Category.objects.all()
    except:
        categories = None
    return {"categories": categories}
