from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cart.models import CartItems,Cart
from .models import Orders,OrderItems
from .serializers import OrderSerializer,OrderItemSerializer

# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def place_order(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItems.objects.filter(cart=cart)

    if not cart_items.exists():
        return Response(status=status.HTTP_400_BAD_REQUEST)

    total_price = 0
    for item in cart_items:
        total_price+=item.q_price

    order = Orders.objects.create(user = request.user, total_price=total_price)

    for item in cart_items:
        OrderItems.objects.create(
            order=order,
            food=item.food_items,
            quantity = item.quantity,
            sub_total = item.q_price
        )

    cart_items.delete()
    return Response({'message':"Order placed"},status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_history(request):
    order = Orders.objects.filter(user = request.user).order_by('-id')
    serializer = OrderSerializer(order,many=True)

    return Response(serializer.data,status=status.HTTP_200_OK)

