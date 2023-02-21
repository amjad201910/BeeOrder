from django.contrib import admin

from .models import Cart, CP


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'Created_on', 'Address', 'Price')
    list_filter = ('user', 'Created_on')


@admin.register(CP)
class CPAdmin(admin.ModelAdmin):
    list_display = ('id', 'Meal', 'Cart', 'Quantity', 'Price')
    list_filter = ('Meal', 'Cart')
