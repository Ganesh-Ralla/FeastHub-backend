from django.urls import path
from . import views


urlpatterns = [
    path('food-items/',views.FoodItems.as_view()),
]