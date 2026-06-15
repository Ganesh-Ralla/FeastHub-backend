from django.contrib import admin
from .models import Cart,CartItems


# Register your models here.
admin.site.register(Cart)


@admin.register(CartItems)
class AdminCartItems(admin.ModelAdmin):
    list_display = ['cart','food_items','quantity']