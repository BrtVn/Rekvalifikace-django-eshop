from django.views import generic

from eshop.models.tag import Tag


class TagDetailView(generic.DetailView):

    model = Tag
    template_name = "eshop/tag_detail.html"
    context_object_name = "tag"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     product = self.get_object()
    #     images = product.images.all()
    #     variants = product.product_variants.all()
    #     context["images"] = images
    #     context["variants"] = variants
    #     add_item_form = CreateCartItemForm()
    #     add_item_form.fields["quantity"].widget.attrs['style'] = "width: 4em"
    #     add_item_form.fields["product_variant"].queryset = variants

    #     context["add_item_form"] = add_item_form
    #     return context
