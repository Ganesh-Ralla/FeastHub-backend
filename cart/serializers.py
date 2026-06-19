from rest_framework import serializers
from .models import Cart,CartItems
from food.serializers import FoodSerializer
from food.models import FoodItem

class CartItemsSerializer(serializers.ModelSerializer):
    food_items = serializers.PrimaryKeyRelatedField(queryset=FoodItem.objects.all())
    food_details = FoodSerializer(source='food_items',read_only=True)
    class Meta:
        model = CartItems
        fields = '__all__'
        read_only_fields = ['cart']


class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemsSerializer(read_only=True, many=True)
    class Meta:
        model = Cart
        fields = ['user','cart_items']
