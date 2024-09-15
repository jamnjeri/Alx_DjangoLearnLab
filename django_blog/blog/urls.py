from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView, 
    CommentUpdateView,
    CommentDeleteView,
    search_posts,
    PostByTagListView,
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    # path('post/<int:post_id>/comments/new/', CommentCreateView, name='add-comment'),
    path('post/<int:pk>/comments/new/', CommentCreateView, name='add-comment'),
    # path('comment/<int:comment_id>/update/', CommentUpdateView, name='edit-comment'),
    path('comment/<int:pk>/update/', CommentUpdateView, name='edit-comment'),
    # path('comment/<int:comment_id>/delete/', CommentDeleteView, name='delete-comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView, name='delete-comment'),
    path('search/', search_posts, name='search'),
    # path('tags/<slug:tag_slug>/', PostByTagListView, name='posts-by-tag'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),
]
