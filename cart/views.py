from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from food.models import FoodItem
from .serializers import CartSerializer, CartItemsSerializer
from .models import Cart,CartItems

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_cart(request):
    cart = Cart.objects.get(user = request.user)
    serializer = CartSerializer(cart)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request):
    # get the users cart
    cart = Cart.objects.get(user = request.user)

    # check whether the items already exists
    food_item_id = request.data.get('food_items')
    # print(food_item_id)
    food_item = FoodItem.objects.get(id=food_item_id)
    # print(food_item)
    existing_item = CartItems.objects.filter(cart=cart,food_items=food_item).first()

    if existing_item:
        existing_item.quantity+=1
        food_item.stock-=1
        food_item.save()
        existing_item.q_price = existing_item.quantity * existing_item.food_items.price
        existing_item.save()

        serializer = CartItemsSerializer(existing_item)
        return Response(serializer.data,status=status.HTTP_200_OK)

    serializer = CartItemsSerializer(data=request.data)

    if serializer.is_valid():
        cart_item = serializer.save(cart=cart)
        cart_item.q_price = cart_item.quantity * cart_item.food_items.price
        food_item.stock-=1
        food_item.save()

        cart_item.save()

        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_quantity(request,pk):
    cart = Cart.objects.get(user = request.user)
    cart_item = CartItems.objects.get(cart=cart, pk=pk)

    old_quantity = cart_item.quantity
    new_quantity = int(request.data.get('quantity'))

    difference = new_quantity - old_quantity
    food_item = cart_item.food_items
    # print(food_item)

    if difference>0:
        if food_item.stock<difference:
            return Response({"message":"Not enough stock"})
        food_item.stock-=difference
    elif difference<0:
        food_item.stock+= abs(difference)
    food_item.save()

    cart_item.quantity = new_quantity
    cart_item.q_price = cart_item.quantity * cart_item.food_items.price
    cart_item.save()
    return Response({'Quantity':cart_item.quantity},status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_cart_item(request,pk):
    try:
        cart = Cart.objects.get(user=request.user)
        cart_item = CartItems.objects.get(cart=cart, pk=pk)
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

