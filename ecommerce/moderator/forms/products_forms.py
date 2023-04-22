from django import forms
from django.forms import inlineformset_factory

from eshop.models.products import Product, ProductImage, ProductVariant, ProductCategory


class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = "__all__"


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class ImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = "__all__"


class VariantForm(forms.ModelForm):
    class Meta:
        model = ProductVariant
        fields = "__all__"


ProductVariantFormSet = inlineformset_factory(
    Product,
    ProductVariant,
    form=VariantForm,
    extra=1,
    can_delete=True,
    can_delete_extra=True,
)
ProductImageFormSet = inlineformset_factory(
    Product,
    ProductImage,
    form=ImageForm,
    extra=1,
    can_delete=True,
    can_delete_extra=True,
)
