from django.forms import ModelForm


from eshop.models.orders import Order, Cart, CartItem, DeliveryMethod, PaymentMethod


class DevliveryMethodForm(ModelForm):
    class Meta:
        model = DeliveryMethod
        fields = "__all__"


class PaymentMethodForm(ModelForm):
    class Meta:
        model = PaymentMethod
        fields = "__all__"


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["status"]


# class CartForm(ModelForm):
#     class Meta:
#         model = Cart
#         fields = "__all__"


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
