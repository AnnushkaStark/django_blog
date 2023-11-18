from django import forms
from .models import Comment

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'text_comment')