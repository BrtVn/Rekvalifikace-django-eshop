from django import forms
from django.contrib.auth.forms import AuthenticationForm
from eshop.models.users import CustomUser

class CreateUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "phone", "email", "password"]


class LoginUserForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ["email", "password"]
