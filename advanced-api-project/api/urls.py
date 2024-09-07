from django.urls import path, include
from .views import BookListView, BookDetailView
# from .views import BookViewSet
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'books', BookViewSet)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    # path('', include(router.urls)),
]