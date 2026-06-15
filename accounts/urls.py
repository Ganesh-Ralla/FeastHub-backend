from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from . import views
urlpatterns = [
    path('register-user/',views.RegisterUser.as_view()),
    path('profile/',views.UserDetails.as_view()),


    path('login/',TokenObtainPairView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),
]