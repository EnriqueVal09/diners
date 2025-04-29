from django.contrib import admin

from .models import Category, Meal, MealOption

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'diner', 'order')
    search_fields = ('name',)
    list_filter = ('diner',)

class MealOptionInlineAdmin(admin.TabularInline):
    model = MealOption
    extra = 0

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    search_fields = ('name',)
    list_filter = ('category',)
    inlines = [MealOptionInlineAdmin]
