from django.views import generic

from eshop.models.products import Product, ProductImage
from eshop.forms.cart_forms import CreateCartItemForm


class CurrentProductView(generic.DetailView):

    model = Product
    template_name = "eshop/product_detail.html"
    context_object_name = "product"

    # def get_object(self):
    #     return super().get_object()
    #     # return self.model.objects.get(slug=self.kwargs.get('slug'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        images = product.images.all()
        variants = product.product_variants.all()
        context["images"] = images
        context["variants"] = variants
        add_item_form = CreateCartItemForm()
        add_item_form.fields["quantity"].widget.attrs['style'] = "width: 4em"
        add_item_form.fields["product_variant"].queryset = variants

        context["add_item_form"] = add_item_form
        return context

    # def get(self, request, pk):
    #     try:
    #         product = self.get_object()
    #     except:
    #         return redirect("index")
    #     return render(request, self.template_name, {"product": product})
