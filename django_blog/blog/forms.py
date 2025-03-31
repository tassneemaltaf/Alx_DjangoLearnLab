from django.forms import ModelForm
from .models import Comment

class CommentForm(ModelForm):
  class Meta:
    model = Comment
    exclude = ['post', 'author', 'created_at', 'updated_at']