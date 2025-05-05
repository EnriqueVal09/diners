from apps.diners.models import Diner, SocialMediaURL
from apps.menus.models import Category

def diner_context(request):
    try:
        diner = Diner.objects.first()
    except:
        diner = None
    return {"diner": diner}

def category_context(request):
    try:
        categories = Category.objects.filter(diner=Diner.objects.first())
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

def social_media_url_context(request):
    try:
        diner = Diner.objects.first()  # Si siempre es 1 restaurante activo
        social_media_urls = SocialMediaURL.objects.filter(diner=diner)
    except:
        social_medias = []
    return {"social_media_urls": social_media_urls}
