from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext_lazy as _
from users.models import CustomUser, DeliveryInformation
from django.forms import inlineformset_factory


class CustomerCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            "first_name",
            "last_name",
            "phone",
            "email",

        ]


class CustomerChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_(
            "Raw passwords are not stored, so there is no way to see this "
            "user’s password, but you can change the password using "
            '<a href="{}">this form</a>.'.format(
                "/accounts/password/set/")
        ),
    )
    #

    class Meta:
        model = CustomUser
        fields = [
            "first_name",
            "last_name",
            "phone",
            "email",
        ]
