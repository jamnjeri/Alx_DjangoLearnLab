from django import forms
from .models import Comment, Post
from taggit.forms import TagWidget 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Use the fields that exist in the Comment model

class PostForm(forms.ModelForm):
    tags = forms.CharField(
        widget=TagWidget(),  # Use TagWidget to handle tag inputs
        required=False
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Add 'tags' to the fields