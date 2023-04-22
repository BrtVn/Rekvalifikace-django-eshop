from django.forms import ModelForm
from settings.models.settings import GeneralInfo, Contact


class GeneralInfoForm(ModelForm):
    class Meta:
        model = GeneralInfo
        fields = "__all__"


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        exclude = ["alias"]
