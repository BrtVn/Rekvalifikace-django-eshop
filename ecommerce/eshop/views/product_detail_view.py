from django.shortcuts import render, redirect
from django.views import generic

from eshop.models.products import Product
from eshop.views.place_order_view import PlaceOrderView

class CurrentProductView(generic.DetailView):

    model = Product
    template_name = "eshop/product_detail.html"

    def get(self, request, pk):
        try:
            product = self.get_object()
        except:
            return redirect("index")
        return render(request, self.template_name, {"product": product})
    
    
    
