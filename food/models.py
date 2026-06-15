from tkinter.constants import CASCADE

from django.db import models

# Create your models here.
class Categories(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField(blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    serves = models.IntegerField()
    rating = models.FloatField()
    stock = models.PositiveIntegerField(default=10)

    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='food_items')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name