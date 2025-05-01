import uuid
from django.db import models

class Promo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    diner = models.ForeignKey('diners.Diner', on_delete=models.CASCADE, related_name="promotions", verbose_name="Restaurante")
    title = models.CharField("Título", max_length=100)
    image_url = models.URLField("URL de imagen de la promoción")
    active = models.BooleanField("¿Activa?", default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
