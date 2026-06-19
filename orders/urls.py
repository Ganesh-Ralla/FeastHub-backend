from django.urls import path
from . import views

urlpatterns = [
    path('order/place-order',views.place_order),
    path('order/history',views.order_history),
]