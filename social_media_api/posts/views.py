from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from .models import Post, Comment, Like
from notifications.models import Notification
from .serializers import PostSerializer, CommentSerializer
from rest_framework.response import Response
from django.contrib.contenttypes.models import ContentType

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

class LikePostView(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)  # Use get_object_or_404 to fetch the post
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        
        if created:
            # Create a notification for the user whose post was liked
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked',
                target_content_type=ContentType.objects.get_for_model(Post),
                target_object_id=post.id
            )
            return Response({'status': 'liked'}, status=201)
        return Response({'status': 'already liked'}, status=400)

    def destroy(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)  # Using generics.get_object_or_404 here as well
        Like.objects.filter(user=request.user, post=post).delete()
        return Response({'status': 'unliked'}, status=204)
    