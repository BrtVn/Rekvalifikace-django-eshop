from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models.product_category import ProductCategory
from .models.products import Product, ProductImage, ProductVariant
from .models.tag import Tag
from .models.product_price_list import ProductPriceList
from .models.product_inventory import ProductInventory
from .models.orders import Order
from .models.messages import Message
# Register your models here.

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    readonly_fields = ('id', 'image_tag',)
    extra = 1
    

class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    readonly_fields = ('id',)
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductVariantInline, ProductImageInline]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'quantity', 'status', 'created_on')
    list_filter = ("created_on",)
    search_fields = ['customer', 'product']


admin.site.register(ProductCategory)
admin.site.register(Tag)
admin.site.register(ProductPriceList)
admin.site.register(ProductInventory)
# admin.site.register(Order)
admin.site.register(Message)
