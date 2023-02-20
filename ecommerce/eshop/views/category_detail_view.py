from django.shortcuts import render, redirect
from django.views import generic

from eshop.models.product_category import ProductCategory
from eshop.models.tag import Tag

class CurrentProductCategoryView(generic.DetailView):

    model = ProductCategory
    template_name = "eshop/category_detail.html"
    def get(self, request, pk):
        try:
            category = self.get_object()
            #tagy = Tag.objects.filter()
        except:
            return redirect("category-tree-index")
        return render(request, self.template_name, {"category": category})
