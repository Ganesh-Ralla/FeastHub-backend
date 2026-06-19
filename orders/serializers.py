from rest_framework import serializers
from .models import OrderItems,Orders
from food.serializers import FoodSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    fooditems = FoodSerializer(read_only=True,many=True)
    class Meta:
        model = OrderItems
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    orderitems = OrderItemSerializer(read_only=True,many=True)

    class Meta:
        model = Orders
        fields = ['id','user','total_price','placed_on','orderitems']