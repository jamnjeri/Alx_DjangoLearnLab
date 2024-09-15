from django import forms
from taggit.forms import TagWidget
from .models import Comment, Post

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
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': TagWidget(attrs={'class': 'form-control'})  # Add widget class if necessary
        }
