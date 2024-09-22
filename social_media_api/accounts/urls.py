from django.urls import path
from .views import RegisterUserView, CustomObtainAuthToken, FollowUser, UnfollowUser

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', CustomObtainAuthToken.as_view(), name='login'),
    path('follow/<int:user_id>/', FollowUser.as_view()),
    path('unfollow/<int:user_id>/', UnfollowUser.as_view()),
]