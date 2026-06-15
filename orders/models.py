from django.db import models
from cart.models import Cart
from food.models import FoodItem
from django.contrib.auth.models import User


# Create your models here.
class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    total_price = models.FloatField(blank=True)

    placed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class OrderItems(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='orderitems')
    food = models.ForeignKey(FoodItem, on_delete=models.CASCADE, related_name='fooditems')

    def __str__(self):
        return self.food.name




