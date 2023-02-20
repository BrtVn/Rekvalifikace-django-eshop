from django.forms import ModelForm
from eshop.models.messages import Message

class ContactForm(ModelForm):
    
    class Meta:
        model = Message
        fields = ["name", "email", "message"]