from django.contrib import admin
from .models import Categories,FoodItem


# Register your models here.
admin.site.register(Categories)


@admin.register(FoodItem)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['name','serves','price','category','stock']