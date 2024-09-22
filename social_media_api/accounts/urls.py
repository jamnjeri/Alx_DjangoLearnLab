from django.urls import path
from .views import RegisterUserView, CustomObtainAuthToken

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', CustomObtainAuthToken.as_view(), name='login'),
]