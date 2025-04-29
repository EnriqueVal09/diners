from django.db import models
import uuid

class Diner(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Nombre del restaurante", max_length=100)
    theme_color = models.CharField("Color del tema", max_length=20)
    font_family = models.CharField("Tipografía", max_length=50)
    background_image_url = models.URLField("Imagen de fondo", blank=True, null=True)
    logo = models.ImageField("Logo del restaurante", upload_to="logos/")
    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)

    def __str__(self):
        return self.name

class QRCode(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    diner = models.OneToOneField(Diner, on_delete=models.CASCADE, related_name="qr_code", verbose_name="Restaurante")
    qr_url = models.URLField("URL del código QR")

    def __str__(self):
        return f"QR de {self.diner.name}"