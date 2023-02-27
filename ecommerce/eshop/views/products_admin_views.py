from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView
from django.forms import inlineformset_factory
from django.db import transaction
from eshop.models.products import Product, ProductImage, ProductVariant
from eshop.forms.products_forms import (
    ProductForm,
    VariantForm,
    ImageForm,
    ProductVariantFormSet,
    ProductImageFormSet,
)


# class ProductInline:
#     model = Product
#     form_class = ProductForm
#     success_url = reverse_lazy("list_products")
#     template_name = "eshop/product_create_or_update.html"

#     def get_context_data(self, **kwargs):
#         data = super().get_context_data(**kwargs)
#         if self.request.POST:
#             data["images"] = ProductImageFormSet(
#                 self.request.POST, self.request.FILES, instance=self.object
#             )
#             data["variants"] = ProductVariantFormSet(
#                 self.request.POST, instance=self.object
#             )
#         else:
#             data["images"] = ProductImageFormSet(instance=self.object)
#             data["variants"] = ProductVariantFormSet(instance=self.object)
#         return data

#     def form_valid(self, form):
#         context = self.get_context_data()
#         images = context["images"]
#         variants = context["variants"]
#         with transaction.atomic():
#             self.object = form.save()
#             if images.is_valid() and variants.is_valid():
#                 images.instance = self.object
#                 images.save()
#                 variants.instance = self.object
#                 variants.save()
#         return super().form_valid(form)


class ProductListView(ListView):
    model = Product
    template_name = "eshop/product_list.html"
    context_object_name = "products"


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("list_products")
    template_name = "eshop/product_create_or_update.html"

    def get_context_data(self, **kwargs):
        data = super(ProductCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data["images_formset"] = ProductImageFormSet(
                self.request.POST, self.request.FILES, instance=self.object
            )
            data["variants_formset"] = ProductVariantFormSet(
                self.request.POST, instance=self.object
            )
        else:
            data["images_formset"] = ProductImageFormSet(instance=self.object)
            data["variants_formset"] = ProductVariantFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        images = context["images_formset"]
        variants = context["variants_formset"]
        with transaction.atomic():
            self.object = form.save()
            if images.is_valid() and variants.is_valid():
                images.instance = self.object
                images.save()
                variants.instance = self.object
                variants.save()
        return super(ProductCreateView, self).form_valid(form)


class ProductUpdateView(UpdateView):  # pylint: disable=too-many-ancestors
    """
    Úprava konkrétního produktu

    Args:
        UpdateView (_type_): _description_

    Returns:
        _type_: _description_
    """

    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("list_products")
    template_name = "eshop/product_create_or_update.html"

    def get_context_data(self, **kwargs):
        data = super(ProductUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data["images_formset"] = ProductImageFormSet(
                self.request.POST, self.request.FILES, instance=self.object
            )
            data["variants_formset"] = ProductVariantFormSet(
                self.request.POST, instance=self.object
            )
        else:
            data["images_formset"] = ProductImageFormSet(instance=self.object)
            data["variants_formset"] = ProductVariantFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        images = context["images_formset"]
        variants = context["variants_formset"]
        with transaction.atomic():
            if images.is_valid() and variants.is_valid():
                self.object = form.save()
                images.instance = self.object
                images.save()
                variants.instance = self.object
                variants.save()
        return super(ProductUpdateView, self).form_valid(form)


# https://www.letscodemore.com/blog/django-inline-formset-factory-with-examples/
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.views.generic import ListView
# from django.views.generic.edit import CreateView, UpdateView

# from eshop.forms.products_forms import ProductForm, ProductVariantFormSet, ProductImageFormSet
# from eshop.models.products import ProductImage, Product, ProductVariant


# class ProductInline():
#     form_class = ProductForm
#     model = Product
#     template_name = "eshop/product_create_or_update.html"

#     def form_valid(self, form):
#         named_formsets = self.get_named_formsets()
#         if not all((x.is_valid() for x in named_formsets.values())):
#             return self.render_to_response(self.get_context_data(form=form))

#         self.object = form.save()

#         # for every formset, attempt to find a specific formset save function
#         # otherwise, just save.
#         for name, formset in named_formsets.items():
#             formset_save_func = getattr(
#                 self, 'formset_{0}_valid'.format(name), None)
#             if formset_save_func is not None:
#                 formset_save_func(formset)
#             else:
#                 formset.save()
#         return redirect('list_products')

#     def formset_variants_valid(self, formset):
#         """
#         Hook for custom formset saving.Useful if you have multiple formsets
#         """
#         variants = formset.save(commit=False)
#         # self.save_formset(formset, contact)
#         # add this 2 lines, if you have can_delete=True parameter
#         # set in inlineformset_factory func
#         for obj in formset.deleted_objects:
#             obj.delete()
#         for variant in variants:
#             variant.product = self.object
#             variant.save()

#     def formset_images_valid(self, formset):
#         """
#         Hook for custom formset saving. Useful if you have multiple formsets
#         """
#         images = formset.save(commit=False)
#         # self.save_formset(formset, contact)
#         # add this 2 lines, if you have can_delete=True parameter
#         # set in inlineformset_factory func
#         for obj in formset.deleted_objects:
#             obj.delete()
#         for image in images:
#             image.product = self.object
#             image.save()


# class ProductCreate(ProductInline, CreateView):

#     def get_context_data(self, **kwargs):
#         context = super(ProductCreate, self).get_context_data(**kwargs)
#         context['named_formsets'] = self.get_named_formsets()
#         return context

#     def get_named_formsets(self):
#         if self.request.method == "GET":
#             return {
#                 'variants': ProductVariantFormSet(prefix='variants'),
#                 'images': ProductImageFormSet(prefix='images'),
#             }
#         else:
#             return {
#                 'variants': ProductVariantFormSet(self.request.POST or None, self.request.FILES or None, prefix='variants'),
#                 'images': ProductImageFormSet(self.request.POST or None, self.request.FILES or None, prefix='images'),
#             }


# class ProductUpdate(ProductInline, UpdateView):

#     def get_context_data(self, **kwargs):
#         context = super(ProductUpdate, self).get_context_data(**kwargs)
#         context['named_formsets'] = self.get_named_formsets()
#         return context

#     def get_named_formsets(self):
#         return {
#             'variants': ProductVariantFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='variants'),
#             'images': ProductImageFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='images'),
#         }


# class ProductList(ListView):
#     model = Product
#     template_name = "eshop/product_list.html"
#     context_object_name = "products"


# def delete_image(request, pk):
#     try:
#         image = ProductImage.objects.get(id=pk)
#     except ProductImage.DoesNotExist:
#         messages.success(
#             request, 'Object Does not exit'
#         )
#         return redirect('update_product', pk=image.product.id)

#     image.delete()
#     messages.success(
#         request, 'Image deleted successfully'
#     )
#     return redirect('update_product', pk=image.product.id)


# def delete_variant(request, pk):
#     try:
#         variant = ProductVariant.objects.get(id=pk)
#     except ProductVariant.DoesNotExist:
#         messages.success(
#             request, 'Object Does not exit'
#         )
#         return redirect('update_product', pk=variant.product.id)

#     variant.delete()
#     messages.success(
#         request, 'Variant deleted successfully'
#     )
#     return redirect('update_product', pk=variant.product.id)
