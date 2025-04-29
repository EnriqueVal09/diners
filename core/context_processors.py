from apps.diners.models import Diner

def diner_context(request):
    try:
        diner = Diner.objects.first()
    except:
        diner = None
    return {"diner": diner}
