from django.urls import path
from .views import RegisterUserView, CustomObtainAuthToken, FollowViewSet

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', CustomObtainAuthToken.as_view(), name='login'),
    path('follow/<int:user_id>/', FollowViewSet.as_view({'post': 'follow_user'})),
    path('unfollow/<int:user_id>/', FollowViewSet.as_view({'post': 'unfollow_user'})),
]