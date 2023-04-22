from django.shortcuts import render
from django.views import generic

from eshop.models.products import ProductCategory


class CategoryTreeIndex(generic.ListView):
    model = ProductCategory
    # cesta k templatu ze složky templates (je možné sdílet mezi aplikacemi)
    template_name = "eshop/category_list.html"
    # pod tímto jménem budeme volat list objektů v templatu
    context_object_name = "categories"

    def get_queryset(self):
        categories = ProductCategory.objects.all()
        return categories
