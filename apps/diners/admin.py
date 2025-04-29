from django.contrib import admin

from .models import Diner, QRCode

@admin.register(Diner)
class DinerAdmin(admin.ModelAdmin):
    list_display = ('name', 'theme_color', 'created_at')
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(QRCode)
class QRCodeAdmin(admin.ModelAdmin):
    list_display = ('diner', 'url')
    search_fields = ('diner__name',)

