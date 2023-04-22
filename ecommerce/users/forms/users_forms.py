from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, ChoiceField
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext_lazy as _
from django.forms import inlineformset_factory
from users.models import CustomUser, DeliveryInformation, BillingInformation


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name"]


class AdminCustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = [
            "first_name",
            "last_name",
            "phone",
            "email",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Get the current user object
        user = self.instance
        # Limit the choices of the preferred_billing_information field to user-related choices
        self.fields['preferred_billing_information'].queryset = user.billing_informations.all()
        self.fields['preferred_delivery_information'].queryset = user.delivery_informations.all()


class CustomUserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_(
            "Raw passwords are not stored, so there is no way to see this "
            "user’s password, but you can change the password using "
            '<a href="{}">this form</a>.'.format(
                "/accounts/password/set/")
        ),
    )

    class Meta:
        model = CustomUser
        fields = [
            "first_name",
            "last_name",
            "phone",
            "profile_image",
            "preferred_billing_information",
            "preferred_delivery_information",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        password = self.fields.get("password")
        if password:
            password.help_text = password.help_text.format(
                "/accounts/password/set/")
        # Get the current user object
        user = self.instance
        # Limit the choices of the preferred_billing_information field to user-related choices
        self.fields['preferred_billing_information'].queryset = user.billing_informations.all()
        self.fields['preferred_delivery_information'].queryset = user.delivery_informations.all()


class DeliveryInformationForm(ModelForm):
    class Meta:
        model = DeliveryInformation
        fields = "__all__"
        exclude = [
            "user",
        ]


DeliveryInformationFormSet = inlineformset_factory(
    CustomUser,
    DeliveryInformation,
    form=DeliveryInformationForm,
    extra=1,
    can_delete=True,
    can_delete_extra=True,
    max_num=4,
    absolute_max=4,
)


class BillingInformationForm(ModelForm):
    class Meta:
        model = BillingInformation
        fields = "__all__"
        exclude = [
            "user",
        ]


BillingInformationFormSet = inlineformset_factory(
    CustomUser,
    BillingInformation,
    form=BillingInformationForm,
    extra=1,
    can_delete=True,
    can_delete_extra=True,
    max_num=4,
    absolute_max=4,
)
