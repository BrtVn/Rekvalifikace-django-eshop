from django.forms import ModelForm
from eshop.models.orders import CartDiscount


class CartDiscountForm(ModelForm):
    class Meta:
        model = CartDiscount
        fields = "__all__"
