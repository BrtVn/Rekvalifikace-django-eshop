from django import forms
from eshop.models.users import User, Customer

class ProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["first_name", "last_name", "phone", "email", "password"]
        #, "address_line1", "address_line2", "city", "postal_code", "country"
        exclude = None
