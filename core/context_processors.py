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
        bebidas_category = categories.filter(name="Bebidas").first()

        if bebidas_category:
            # Si sí existe la categoría "Bebidas"
            menu_categories = categories.exclude(
                id=bebidas_category.id
            ).exclude(
                parent_category=bebidas_category
            )
            bebida_categories = categories.filter(parent_category=bebidas_category)
        else:
            # Si NO existe la categoría "Bebidas"
            menu_categories = categories
            bebida_categories = []

    except:
        menu_categories = []
        bebida_categories = []

    return {
        "menu_categories": menu_categories,
        "bebida_categories": bebida_categories,
    }

