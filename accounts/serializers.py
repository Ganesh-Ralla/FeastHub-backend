from django.contrib.auth.models import User
from rest_framework import serializers
from cart.serializers import CartSerializer
from orders.serializers import OrderSerializer


class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8,style={'input_type':'password'})
    cart = CartSerializer(read_only=True)
    orders = OrderSerializer(read_only=True,many=True)

    class Meta:
        model = User
        fields = ['id','first_name','last_name','email','username','password','cart','orders']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)