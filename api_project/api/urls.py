from django.urls import path, include
from .views import BookViewSet
from rest_framework.routers import DefaultRouter

# Create router and register the BookViewSet with it
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

# The API URLS are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]