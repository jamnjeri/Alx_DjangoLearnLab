from django.urls import path, include
from .views import BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

# Create router and register the BookViewSet with it
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

# The API URLS are now determined automatically by the router
urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', include(router.urls)),
]