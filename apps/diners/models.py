from django.db import models
import uuid

class Diner(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Nombre del restaurante", max_length=100)
    theme = models.CharField("Tema de colores", max_length=50, blank=True, null=False)
    background_image_url = models.URLField("Imagen de fondo", blank=True, null=True)
    logo = models.ImageField("Logo del restaurante", upload_to="logos/")
    address = models.CharField("Dirección", max_length=255)
    phone_number = models.CharField("Teléfono", max_length=20, blank=True, null=False)
    email = models.EmailField("Correo electrónico", blank=True, null=False)
    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)

    def __str__(self):
        return self.name

class QRCode(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    diner = models.OneToOneField(Diner, on_delete=models.CASCADE, related_name="qr_code", verbose_name="Restaurante")
    qr_url = models.URLField("URL del código QR")

    def __str__(self):
        return f"QR de {self.diner.name}"
    
class SocialMedia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    diner = models.ForeignKey(Diner, on_delete=models.CASCADE, related_name="social_media_urls", verbose_name="Restaurante")
    name = models.CharField("red social", max_length=50)
    url = models.URLField("URL de la pagina")

    def __str__(self):
        return f"{self.diner.name} - {self.name}"
