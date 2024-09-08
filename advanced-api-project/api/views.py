from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter, NumberFilter
from rest_framework import filters

# Define the FilterSet class for filtering books by title, author, and publication_year
class BookFilter(FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')
    author = CharFilter(field_name='author__name', lookup_expr='icontains')  # Assuming 'author' is a related field
    publication_year = NumberFilter(field_name='publication_year')

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

# Create your views here.
class ListView(generics.ListAPIView):
    # View to list all books.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

    # Filtering, searching, and ordering added
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_class = BookFilter
    search_fields = ['title', 'author__name']  # Search by book title or author's name
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering

class DetailView(generics.RetrieveAPIView):
    # View to retrieve a specific book.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

class CreateView(generics.CreateAPIView):
    # View to create a new book.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class UpdateView(generics.UpdateAPIView):
    # View to update an existing book.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class DeleteView(generics.DestroyAPIView):
    # View to delete an existing book.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# This view lists all books or someone can create a new book
# class BookListView(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [AllowAny]

# #  This view retrieves, updates or deletes a single book instance
# class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

#     def get_permissions(self):
#         if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
#             self.permission_classes = [IsAuthenticated]
#         else:
#             self.permission_classes = [AllowAny]
#         return super().get_permissions()

# ModelViewSet in DRF is a powerful and flexible view that automatically provides a full set of CRUD operations by default based on the queryset and serializer you provide
# List:           GET /books/
# Create:         POST /books/
# Retrieve:       GET /books/<id>/
# Update:         PUT /books/<id>/      or   PATCH /books/<id>/ 
# Destroy:        DELETE /books/<id>/

# Updated to use viewsets instead:
# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

#     # Customizing the View Behavior
#     def create(self, request, *args, **kwargs):
#         # Custom logic before creating a book
#         response = super().create(request, *args, **kwargs)
#         # Custom logic after creating a book
#         return response
    
#     def update(self, request, *args, **kwargs):
#         # Custom logic before updating a book
#         response = super().update(request, *args, **kwargs)
#         # Custom logic after updating a book
#         return response
    
#     # Returns the permission classes based on the request method.
#     def get_permissions(self):
#         if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
#             self.permission_classes = [IsAuthenticated]
#         else:
#             self.permission_classes = [AllowAny]
#         return super().get_permissions()

