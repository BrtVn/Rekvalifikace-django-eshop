from django.forms import ModelForm

from django.forms.widgets import TextInput
from eshop.models.tag import Tag


class TagForm(ModelForm):

    class Meta:
        model = Tag
        fields = "__all__"

        widgets = {
            "bg_color": TextInput(attrs={"type": "color"}),
            "font_color": TextInput(attrs={"type": "color"})
        }
