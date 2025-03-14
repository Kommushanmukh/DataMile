from django import forms
from .models import Post
from .models import Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['project_description', 'github_link', 'doubt_description', 'code_part', 'image_upload']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']  # Ensure you use 'text' instead of 'content'

