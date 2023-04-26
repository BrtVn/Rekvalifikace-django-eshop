
"""_summary_

    Returns:
        _type_: _description_
"""
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import redirect, render,  HttpResponseRedirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.core.exceptions import ValidationError
from django.views.generic import ListView, FormView, CreateView, DeleteView, UpdateView, View, DetailView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from eshop.models.orders import Cart, CartItem, Order, CartDiscount
from eshop.forms.cart_forms import (
    CustomerInformationForm,
    CreateCartItemForm,
    UpdateCartItemForm,
    DeliveryInformationForm,
    BillingInformationForm,
    ApplyCartDiscountForm,
    CartDeliveryMethodForm,
    CartPaymentMethodForm,
    CreateOrderForm,
)
from users.models.users import CustomUser, BillingInformation, DeliveryInformation


class CartMixin:
    def get_cart(self):
        status = "DRAFT"
        cart_id = self.request.session.get('cart_id')
        if cart_id:
            try:
                return Cart.objects.get(pk=cart_id, status=status)
            except Cart.DoesNotExist:
                print(
                    f"Cart instance with id {cart_id} and status '{status}' does not exist.")
        return None


class OrderProfileListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "eshop/list_orders.html"
    context_object_name = "orders"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(customer=self.request.user)
        return queryset


class OrderProfileDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "eshop/order_detail.html"
    context_object_name = "order"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = self.get_object()
        context["cart"] = order.cart
        context["cart_items"] = order.cart.items.all()
        context["billing_info"] = BillingInformation.objects.get(
            pk=order.billing_info.pk)
        context["delivery_info"] = DeliveryInformation.objects.get(
            pk=order.delivery_info.pk)
        return context


class CreateOrderView(CartMixin, CreateView):
    model = Order
    form_class = CreateOrderForm
    template_name = "eshop/place_order.html"
    success_url = reverse_lazy('order_detail')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        customer = self.request.user
        if not customer.is_authenticated:
            customer = None

        billing_form_instance = None
        delivery_form_instance = None
        if customer:
            billing_form_instance = customer.preferred_billing_information
            delivery_form_instance = customer.preferred_delivery_information
            context["customer"] = CustomUser.objects.get(pk=customer.id)

        customer_form = CustomerInformationForm(
            instance=customer)
        context["customer_form"] = customer_form

        delivery_form = DeliveryInformationForm(
            instance=delivery_form_instance)
        context["delivery_form"] = delivery_form

        billing_form = BillingInformationForm(
            instance=billing_form_instance)
        context["billing_form"] = billing_form

        return context

    @transaction.atomic
    def form_valid(self, form):

        form = CreateOrderForm(self.request.POST)
        delivery_form = DeliveryInformationForm(self.request.POST)
        billing_form = BillingInformationForm(self.request.POST)
        with transaction.atomic():
            if delivery_form.is_valid() and billing_form.is_valid() and form.is_valid():
                delivery_info = delivery_form.save()
                billing_info = billing_form.save()
                order = form.save(commit=False)
                order.delivery_info = delivery_info
                order.billing_info = billing_info
                order.cart = self.get_cart()

                invalid_items = []
                for item in order.cart.items.all():
                    if item.product_variant.quantity < item.quantity:
                        invalid_items.append(item)
                        messages.error(
                            self.request, f"{item.product_variant} has been sold, please check available item quantity")

                if invalid_items:
                    return redirect('cart')
                else:
                    for item in order.cart.items.all():
                        item.product_variant.quantity -= item.quantity
                        item.product_variant.save()

                order.cart.status = "PLACED"
                order.status = "PLACED"

                customer = self.request.user
                if not customer.is_authenticated:
                    customer = None
                order.customer = customer
                order.total_price = order.cart.get_total_cart_price

                if order.cart.code.is_single_use:
                    order.cart.code.is_active = False
                    order.cart.code.save()
                order.cart.save()
                order.save()
                messages.success(
                    self.request, "Order successfuly finished.")
                return HttpResponseRedirect(self.get_success_url())
            else:
                return self.render_to_response(self.get_context_data(form=form, delivery_form=delivery_form))

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse_lazy('index')


class UserPreferredBillingInformationView(View):
    model = CustomUser
    success_url = reverse_lazy('create_order')

    def get(self, request, *args, **kwargs):
        billing_info_id = kwargs.get("pk")
        if billing_info_id:
            billing_info = get_object_or_404(
                BillingInformation, id=billing_info_id)
            customer = request.user
            customer.preferred_billing_information = billing_info
            customer.save()
        return redirect(self.success_url)


class UserPreferredDeliveryInformationView(View):
    model = CustomUser
    success_url = reverse_lazy('create_order')

    def get(self, request, *args, **kwargs):
        delivery_info_id = kwargs.get("pk")
        if delivery_info_id:
            delivery_info = get_object_or_404(
                DeliveryInformation, id=delivery_info_id)
            customer = request.user
            customer.preferred_delivery_information = delivery_info
            customer.save()
        return redirect(self.success_url)


class CartPaymentMethodView(CartMixin, UpdateView):
    model = Cart
    form_class = CartPaymentMethodForm
    success_url = reverse_lazy('cart')

    def form_valid(self, form):
        cart = form.save(commit=False)
        cart.payment_method = form.cleaned_data["payment_methods"]
        cart.save()
        messages.success(
            self.request, "The payment method was updated.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "Please provide valid payment method.")
        return super().form_invalid(form)


class CartDeliveryMethodView(CartMixin, UpdateView):
    model = Cart
    form_class = CartDeliveryMethodForm
    success_url = reverse_lazy('cart')

    def form_valid(self, form):
        cart = form.save(commit=False)
        cart.delivery_method = form.cleaned_data["delivery_methods"]
        cart.save()
        messages.success(
            self.request, "The delivery method was updated.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "Please provide valid delivery method.")
        return super().form_invalid(form)


class CartListView(CartMixin, ListView):
    model = Cart
    template_name = "eshop/cart.html"
    context_object_name = "cart_items"

    def get_queryset(self):
        cart = self.get_cart()
        if cart:
            return cart.items.all()
        return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.get_cart()
        if cart:
            context["cart"] = cart
            for item in context[self.context_object_name]:
                item.update_item_form = UpdateCartItemForm(instance=item)
                item.update_item_form.fields['quantity'].widget.attrs[
                    'max'] = f"{item.product_variant.quantity}"

            cart_payment_method_form = CartPaymentMethodForm(
                instance=cart,
                initial={
                    'payment_methods': cart.payment_method.pk if cart.payment_method else None,
                }
            )
            cart_delivery_method_form = CartDeliveryMethodForm(
                instance=cart,
                initial={
                    'delivery_methods': cart.delivery_method.pk if cart.delivery_method else None,
                }
            )

            context["cart_delivery_method_form"] = cart_delivery_method_form
            context["cart_payment_method_form"] = cart_payment_method_form
            cart_discound_code_form = ApplyCartDiscountForm()
            context["cart_discound_code_form"] = cart_discound_code_form
        return context


class AddToCartView(CartMixin, CreateView):
    model = CartItem
    form_class = CreateCartItemForm
    success_url = reverse_lazy('cart')

    def form_valid(self, form):
        variant = form.cleaned_data['product_variant']
        quantity = int(form.cleaned_data['quantity'])

        cart = self.get_cart()
        if not cart:
            cart = Cart.objects.create()
            print(cart.id)
            self.request.session['cart_id'] = cart.id

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product_variant=variant,
            price=variant.price,
        )
        if not created:
            cart_item.quantity += quantity
            if not variant.quantity < cart_item.quantity:
                cart_item.save()
                messages.info(
                    self.request, f"The quantity of \"{variant}\" was updated.")
            else:
                messages.warning(
                    self.request, f"You are trying to add more of the item '{variant}' than we currently have in our warehouse. Please check your cart.")
                return redirect(self.request.META.get('HTTP_REFERER'))
        else:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(
                self.request, f"The item \"{variant}\" was added to your cart.")

        # cart.total_price += variant.price * quantity
        cart.save()

        return redirect(self.success_url)

    def form_invalid(self, form):
        messages.error(
            self.request, "Please provide product variant and quantity")
        return redirect('.')


class CartUpdateView(CartMixin, UpdateView):
    model = CartItem
    form_class = UpdateCartItemForm
    success_url = reverse_lazy('cart')

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        cart_item = self.get_object()

        form.instance = cart_item

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        cart = self.get_cart()
        if cart:
            # price = cart.get_total_cart_price
            # cart.set_total_cart_price(price)
            cart.save()
            messages.success(self.request, f"The quantity was updated.")

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "Please provide product variant and quantity")
        return super().form_invalid(form)


class CartDeleteView(CartMixin, DeleteView):
    model = CartItem
    success_url = reverse_lazy('cart')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):

        cart = self.get_cart()
        if cart:
            # price = cart.get_total_cart_price
            # cart.set_total_cart_price(price)
            cart.save()
            messages.info(
                self.request, "The item was removed from your cart.")

        return super().delete(request, *args, **kwargs)


class CartDiscountView(CartMixin, FormView):
    form_class = ApplyCartDiscountForm
    success_url = reverse_lazy('cart')

    def form_valid(self, form):
        code_form = form.cleaned_data["code"]
        cart = self.get_cart()
        code = None
        try:
            code = CartDiscount.objects.get(code=code_form, is_active=True)

        except CartDiscount.DoesNotExist:
            code = None
        if not code:
            messages.error(
                self.request, "Please provide valid discount code.")
            return super().form_valid(form)
        if cart:
            cart.code = code
            cart.save()
            messages.success(
                self.request, "The price of items was updated.")

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "Please provide valid discount code.")
        return super().form_invalid(form)
