from django.urls import path, include
from .views import CreateView, UpdateView, DeleteView, ListView, DetailView
# from .views import BookListView, BookDetailView
# from .views import BookViewSet
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'books', BookViewSet)

urlpatterns = [
    path('books/', ListView.as_view(), name='book-list'),
    path('books/<int:pk>/', DetailView.as_view(), name='book-detail'),
    path('books/create/', CreateView.as_view(), name='book-create'),
    path('books/update/<int:pk>/', UpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>', DeleteView.as_view(), name='book-delete'),
    # path('books/', BookListView.as_view(), name='book-list'),
    # path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    # path('', include(router.urls)),
]