from django.contrib import admin
from .models import Orders,OrderItems


# Register your models here.
admin.site.register(Orders)

@admin.register(OrderItems)
class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order','food']