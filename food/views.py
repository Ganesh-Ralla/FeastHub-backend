from django.shortcuts import render
from rest_framework import  generics
from .serializers import CategorySerializer
from .models import Categories


# Create your views here.
class FoodItems(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer

