
from django.contrib import admin
from .models.products import Product, ProductImage, ProductVariant, ProductCategory
from .models.tag import Tag
from .models.product_price_list import ProductPriceList
from .models.product_inventory import ProductInventory
from .models.orders import Order, Cart, CartItem, DeliveryMethod, PaymentMethod
from .models.messages import Message
from .forms.tag_forms import TagForm

from users.models.users import DeliveryInformation

from django_reverse_admin import ReverseModelAdmin


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    readonly_fields = (
        "id",
    )
    extra = 1


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    readonly_fields = ("id",)
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductVariantInline, ProductImageInline]
    prepopulated_fields = {'slug': ('product_name',)}


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}


# class DeliveryInformationInline(admin.StackedInline):
#     model = DeliveryInformation
#     extra = 0


# class OrderAdmin(admin.ModelAdmin):
#     inlines = [DeliveryInformationInline]


@admin.register(Order)
class OrderAdmin(ReverseModelAdmin):
    inline_reverse = ['delivery_info', 'billing_info', 'cart']
    inline_type = 'stacked'  # or could be 'stacked'


class CartItemInline(admin.TabularInline):
    model = CartItem
   # readonly_fields = ("id",)
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]


@admin.register(DeliveryMethod)
class DeliveryMethodAdmin(admin.ModelAdmin):
    pass


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    form = TagForm
    prepopulated_fields = {'slug': ('tag_title',)}


admin.site.register(ProductPriceList)
admin.site.register(ProductInventory)
# admin.site.register(Order)
admin.site.register(Message)
