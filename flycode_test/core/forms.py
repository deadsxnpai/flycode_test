from django import forms
from .models import Comment,Book

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'text')

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors', 'archived']