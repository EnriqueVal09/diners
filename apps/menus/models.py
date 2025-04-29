from django.db import models
import uuid

from apps.diners.models import Diner

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    diner = models.ForeignKey(Diner, on_delete=models.CASCADE, related_name="categories", verbose_name="Restaurante")
    name = models.CharField("Nombre de la categoría", max_length=100)
    order = models.IntegerField("Orden de visualización", default=0)
    parent_category = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="subcategories",
        verbose_name="Categoría padre"
    )

    def __str__(self):
        return self.name


class Meal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="meals", verbose_name="Categoría")
    name = models.CharField("Nombre del platillo", max_length=100)
    description = models.TextField("Descripción")
    price = models.DecimalField("Precio", max_digits=8, decimal_places=2)
    available = models.BooleanField("Disponible", default=True)
    image_url = models.URLField("URL de imagen del platillo", blank=True, null=True)

    def __str__(self):
        return self.name


class MealOption(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name="options", verbose_name="Platillo")
    name = models.CharField("Nombre de la opción", max_length=100)
    extra_price = models.DecimalField("Precio extra", max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} (+{self.extra_price})"
