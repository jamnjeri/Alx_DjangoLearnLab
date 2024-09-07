from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.

# This view lists all books or someone can create a new book
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

#  This view retrieves, updates or deletes a single book instance
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [AllowAny]
        return super().get_permissions()

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

