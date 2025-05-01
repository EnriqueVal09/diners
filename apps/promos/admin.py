from django.contrib import admin
from django.utils.html import format_html

from .models import Promo

@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    list_display = ('title', 'diner', 'active', 'created_at')
    list_filter = ('active', 'diner')
    search_fields = ('title',)
    ordering = ('-created_at',)
