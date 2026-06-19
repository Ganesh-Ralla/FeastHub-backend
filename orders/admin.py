from django.contrib import admin
from .models import Orders,OrderItems


# Register your models here.
@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','total_price','placed_on']

@admin.register(OrderItems)
class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order','food','quantity','sub_total']