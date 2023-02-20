from django.forms import ModelForm
from eshop.models.messages import Message

class ReviewForm(ModelForm):
    
    class Meta:
        model = Message
        fields = ["name", "email", "message"]
        #fields = ["name", "email", "message", "score"]