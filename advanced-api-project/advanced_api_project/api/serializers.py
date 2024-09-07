from rest_framework import serializers
from .models import Author, Book

# Serializer for the Book Model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["title", "publication_year", "author"]

    # Validation to ensure the publication year is not in the future.
    def validate_publication_year(self, value):
        if value > 2024:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# Serializer for the Author Model, including nested BookSerializer.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']