from django.forms import ModelForm
from blog.models.comments import Comment

class CommentForm(ModelForm):
    
    class Meta:
        model = Comment
        fields = ["name", "email", "body"]