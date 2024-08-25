from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        # Desired field in your form
        fields = ['title', 'author', 'publication_year']