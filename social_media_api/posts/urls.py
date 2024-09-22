from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView, LikePostView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view()),
    path('posts/<int:pk>/like/', LikePostView.as_view({'post': 'create'}), name='like-post'),
    path('posts/<int:pk>/unlike/', LikePostView.as_view({'delete': 'destroy'}), name='unlike-post'),
]