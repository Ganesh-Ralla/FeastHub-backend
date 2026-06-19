from django.urls import path
from . import views


urlpatterns = [
    path('cart/',views.view_cart),
    path('cart/add-to-cart/',views.add_to_cart),
    path('cart/item/update-quantity/<int:pk>',views.update_quantity),
    path('cart/item/delete/<int:pk>',views.remove_cart_item),

]