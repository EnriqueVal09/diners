from django.contrib import admin

from .models import Diner, QRCode

class QRCodeInlineAdmin(admin.TabularInline):
    model = QRCode
    extra = 0

@admin.register(Diner)
class DinerAdmin(admin.ModelAdmin):
    list_display = ('name', 'theme_color', 'created_at')
    search_fields = ('name',)
    ordering = ('name',)
    inlines = [QRCodeInlineAdmin]


