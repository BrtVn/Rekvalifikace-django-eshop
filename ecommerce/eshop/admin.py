from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models.product_category import ProductCategory
from .models.products import Product
from .models.tag import Tag
from .models.product_price_list import ProductPriceList
from .models.product_inventory import ProductInventory
from .models.users import CustomUser, DeliveryInformation
from .models.orders import Order
from .models.messages import Message
# Register your models here.


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'phone']

    def save(self, commit=True):
        if self.is_valid():
            user = super().save(commit=False)
            user.set_password(self.cleaned_data["password"])
            if commit:
                user.save()
            return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ['email', 'is_admin', 'first_name',
                  'last_name', 'phone', 'is_customer']

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        self.Meta.fields.remove('password')


class DeliveryInformationInline(admin.StackedInline):
    model = DeliveryInformation
    can_delete = False
    verbose_name = 'Adresa'
    verbose_name_plural = 'Adresy'


class UserCustomAdmin(UserAdmin):
    inlines = (DeliveryInformationInline,)
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ['email', 'is_admin', 'first_name',
                    'last_name', 'phone', 'is_customer']
    list_filter = ['is_admin', 'first_name',
                   'last_name', 'phone', 'is_customer']
    fieldsets = (
        (None, {'fields': ['email', 'password',
         'first_name', 'last_name', 'phone']}),
        ('Permissions', {'fields': ['is_admin', 'is_customer']}),
    )

    add_fieldsets = (
        (None, {
            'fields': ['email', 'password', 'first_name', 'last_name', 'phone']}
         ),
    )
    search_fields = ['email', 'first_name', 'last_name', 'phone']
    ordering = ['email']
    filter_horizontal = []


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'quantity', 'status', 'created_on')
    list_filter = ("created_on",)
    search_fields = ['customer', 'product']


admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(ProductPriceList)
admin.site.register(ProductInventory)
admin.site.register(CustomUser, UserCustomAdmin)
# admin.site.register(Customer, CustomCustomer)
# admin.site.register(Order)
admin.site.register(Message)
