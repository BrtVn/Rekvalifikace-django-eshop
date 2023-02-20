from django.forms import ModelForm
from eshop.models.orders import Order


class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields="__all__"
        exclude=['status']