from rest_framework import serializers
from .models import Categories,FoodItem

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    food_items = FoodSerializer(many=True, read_only=True)
    class Meta:
        model = Categories
        fields = ['id','category_name','food_items']