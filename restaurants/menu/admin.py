from django.contrib import admin
from .models import Meal
@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'Name',
        'Restaurnat',
        'Image',
        'Body',
        'Type',
        'Price',
    )
    list_filter = ('Restaurnat', 'Type')
