from django import forms
from eshop.models.users import User, Customer


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "phone", "email", "password"]


class LoginUserForm(forms.Form):
    
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["email", "password"]
