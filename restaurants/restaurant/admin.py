from django.contrib import admin

from .models import Restaurnat, Category


@admin.register(Restaurnat)
class RestaurnatAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'Image', 'Name', 'Address')
    list_filter = ('user',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'Name', 'Restaurnat')
    list_filter = ('Restaurnat',)
