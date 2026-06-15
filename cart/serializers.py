from rest_framework import serializers
from .models import Cart,CartItems
from food.serializers import FoodSerializer

class CartItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItems
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemsSerializer(read_only=True, many=True)
    food_items = FoodSerializer(read_only=True, many=True)
    class Meta:
        model = Cart
        fields = ['user','cart_items','food_items']
