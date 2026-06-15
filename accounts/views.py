
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from .serializers import UserSerializers
from cart.models import Cart


# Create your views here.
class RegisterUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def perform_create(self, serializer):
        user = serializer.save()
        Cart.objects.create(user = user)



class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializers
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user