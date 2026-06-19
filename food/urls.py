from django.urls import path
from . import views


urlpatterns = [
    path('add-food/',views.add_food_item),
    path('food-items/',views.view_food),
    path('food-items/<int:pk>',views.get_food_by_id),
    path('food/category/',views.food_by_category),
    path('food/search/',views.search_food),


]