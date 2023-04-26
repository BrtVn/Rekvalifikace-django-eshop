from django import forms
from django.utils.safestring import mark_safe

from eshop.models.orders import Order, Cart, CartItem, CartDiscount, DeliveryMethod, PaymentMethod
from users.models import DeliveryInformation, BillingInformation, CustomUser
from eshop.models import ProductVariant


class CreateOrderForm(forms.ModelForm):
    agreement = forms.BooleanField(
        required=True, help_text=mark_safe("<i>Odesláním objednávky souhlasíte s obchodními podmínkami a zavazujete se k platbě.</i>"))

    class Meta:
        model = Order
        fields = ("note", "agreement",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['note'].widget.attrs['rows'] = '3'


class AddressForm(forms.ModelForm):
    name = forms.CharField(required=True, max_length=50)
    address_line1 = forms.CharField(required=True, max_length=500)
    address_line2 = forms.CharField(max_length=500, required=False)
    city = forms.CharField(required=True, max_length=100)
    postal_code = forms.CharField(required=True, max_length=50)
    country = forms.CharField(required=True, max_length=50)


class CustomerInformationForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ("email",)


class DeliveryInformationForm(AddressForm):
    class Meta:
        model = DeliveryInformation
        fields = "__all__"
        exclude = [
            "user", "alias",
        ]


class BillingInformationForm(AddressForm):
    class Meta:
        model = BillingInformation
        fields = "__all__"
        exclude = [
            "user", "alias",
        ]


class ApplyCartDiscountForm(forms.Form):
    code = forms.CharField(max_length=20, label="Discount code")

    class Meta:
       # model = CartDiscount
        fields = ["code"]


class CartDeliveryMethodForm(forms.ModelForm):
    delivery_methods = forms.ModelChoiceField(
        queryset=DeliveryMethod.objects.all(),
        widget=forms.RadioSelect(attrs={'type': 'radio'}),
        label='Delivery methods',
        empty_label=None,
    )

    class Meta:
        model = Cart
        fields = ("delivery_methods",)


class CartPaymentMethodForm(forms.ModelForm):
    payment_methods = forms.ModelChoiceField(
        queryset=PaymentMethod.objects.all(),
        widget=forms.RadioSelect(attrs={'type': 'radio'}),
        label='Payment methods',
        empty_label=None,
    )

    class Meta:
        model = Cart
        fields = ("payment_methods",)


class CreateCartItemForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quantity'].widget.attrs['min'] = '1'
        # self.fields['quantity'].widget.attrs['value'] = '1'
        self.fields['quantity'].initial = '1'

    class Meta:
        model = CartItem
        fields = ["product_variant", "quantity"]


class UpdateCartItemForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quantity'].widget.attrs['min'] = '1'

    class Meta:
        model = CartItem
        fields = ["quantity"]
