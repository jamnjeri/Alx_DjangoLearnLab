from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Notification
from .serializers import NotificationSerializer

# Create your views here.
class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(recipient=self.request.user)
    