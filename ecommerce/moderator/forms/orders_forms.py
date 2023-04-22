from django.forms import ModelForm, ModelChoiceField
from django.forms import inlineformset_factory


from eshop.models.orders import Order, Cart, CartItem


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["status"]


class CartForm(ModelForm):
    class Meta:
        model = Cart
        fields = "__all__"


class UpdateCartItemForm(ModelForm):
    class Meta:
        model = CartItem
        fields = ["quantity"]


# CartItemFormSet = inlineformset_factory(
#     Cart,
#     CartItem,
#     form=CartItemForm,
#     extra=1,
#     can_delete=False,
#     can_delete_extra=False,


# )
