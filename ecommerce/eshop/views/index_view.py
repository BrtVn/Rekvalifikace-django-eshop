from django.shortcuts import render
from django.views import generic
from eshop.models.products import Product
from eshop.models.tag import Tag


class ProductsIndex(generic.ListView):
    model = Product
    # cesta k templatu ze složky templates (je možné sdílet mezi aplikacemi)
    template_name = "eshop/index.html"
    # pod tímto jménem budeme volat list objektů v templatu
    context_object_name = "products"

    def get_queryset(self):
        products = Product.objects.all()
        #context = {"products": products}
        return  products
