from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from allauth.account.views import PasswordChangeView
from django.utils.translation import gettext_lazy as _
from users.models import CustomUser, DeliveryInformation


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name"]


class CustomUserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_(
            "Raw passwords are not stored, so there is no way to see this "
            "user’s password, but you can change the password using "
            '<a href="{}">this form</a>.'
        ),
    )

    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "phone", "email", ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        password = self.fields.get("password")
        if password:
            password.help_text = password.help_text.format("/accounts/password/set/")
            
class DeliveryInformationForm(ModelForm):
    
    class Meta:
        model = DeliveryInformation
        exclude = ['user',]
