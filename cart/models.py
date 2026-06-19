from django.db import models
from django.contrib.auth.admin import User
from food.models import FoodItem

# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')

    def __str__(self):
        return self.user.username


class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    food_items = models.ForeignKey(FoodItem, on_delete=models.CASCADE, related_name='food_items')

    quantity = models.PositiveIntegerField(default=1)
    q_price = models.FloatField(blank=True,default=0)

    def __str__(self):
        return self.food_items.name
