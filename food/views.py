from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CategorySerializer,FoodSerializer
from .models import Categories,FoodItem


# Create your views here.

@api_view(['GET'])
def view_food(request):
    category = Categories.objects.all()
    serializer = CategorySerializer(category,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['POST'])
def add_food_item(request):
    serializer = FoodSerializer(data=request.data,many=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def food_by_category(request):
    query = request.GET.get('q','').strip()
    if not query:
        return Response([])
    food = FoodItem.objects.filter(category__category_name__icontains=query)
    serializer = FoodSerializer(food,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def search_food(request):
    query = request.GET.get('q','').strip()

    if not query:
        return Response([])
    foods = FoodItem.objects.filter(name__icontains=query)

    serializer = FoodSerializer(foods,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def get_food_by_id(request,pk):
    food = FoodItem.objects.get(pk=pk)
    serializer = FoodSerializer(food)

    return Response(serializer.data,status=status.HTTP_200_OK)

