from django.contrib import admin

from .models import Diner, QRCode, SocialMediaURL

class QRCodeInlineAdmin(admin.TabularInline):
    model = QRCode
    extra = 0

@admin.register(Diner)
class DinerAdmin(admin.ModelAdmin):
    list_display = ('name', 'theme', 'created_at')
    search_fields = ('name',)
    ordering = ('name',)
    inlines = [QRCodeInlineAdmin]

@admin.register(SocialMediaURL)
class SocialMediaURLAdmin(admin.ModelAdmin):
    list_display = ('name', 'diner', 'url')
    search_fields = ('name', 'diner__name')
    list_filter = ('diner',)


