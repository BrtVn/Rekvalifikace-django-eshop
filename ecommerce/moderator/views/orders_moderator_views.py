from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from eshop.models.orders import Order, CartItem, DeliveryMethod, PaymentMethod
from eshop.forms.cart_forms import BillingInformationForm, DeliveryInformationForm
from moderator.forms.orders_forms import OrderForm, UpdateCartItemForm, DevliveryMethodForm, PaymentMethodForm


class PaymentMethodListView(LoginRequiredMixin, ListView):
    model = PaymentMethod
    template_name = "moderator/payment_methods_list.html"
    context_object_name = "payment_methods"


class PaymentMethodCreateView(LoginRequiredMixin, CreateView):
    model = DeliveryMethod
    form_class = PaymentMethodForm
    success_url = reverse_lazy("list_payment_methods")
    template_name = "moderator/payment_method_create_or_update.html"


class PaymentMethodUpdateView(
    LoginRequiredMixin, UpdateView
):  # pylint: disable=too-many-ancestors

    model = PaymentMethod
    form_class = PaymentMethodForm
    success_url = reverse_lazy("list_payment_methods")
    template_name = "moderator/payment_method_create_or_update.html"


class PaymentMethodDeleteView(
    LoginRequiredMixin, DeleteView
):  # pylint: disable=too-many-ancestors
    """Smazání konkrétní kategorie

    Args:
        LoginRequiredMixin (_type_): _description_
        DeleteView (_type_): _description_
    """

    model = PaymentMethod
    success_url = reverse_lazy("list_payment_methods")


class DeliveryMethodListView(LoginRequiredMixin, ListView):
    model = DeliveryMethod
    template_name = "moderator/delivery_methods_list.html"
    context_object_name = "delivery_methods"


class DeliveryMethodCreateView(LoginRequiredMixin, CreateView):
    model = DeliveryMethod
    form_class = DevliveryMethodForm
    success_url = reverse_lazy("list_delivery_methods")
    template_name = "moderator/delivery_method_create_or_update.html"


class DeliveryMethodUpdateView(
    LoginRequiredMixin, UpdateView
):  # pylint: disable=too-many-ancestors

    model = DeliveryMethod
    form_class = DevliveryMethodForm
    success_url = reverse_lazy("list_delivery_methods")
    template_name = "moderator/delivery_method_create_or_update.html"


class DeliveryMethodDeleteView(
    LoginRequiredMixin, DeleteView
):  # pylint: disable=too-many-ancestors
    """Smazání konkrétní kategorie

    Args:
        LoginRequiredMixin (_type_): _description_
        DeleteView (_type_): _description_
    """

    model = DeliveryMethod
    success_url = reverse_lazy("list_delivery_methods")


class AllOrdersListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "moderator/orders_list.html"
    context_object_name = "orders"

    def get_queryset(self):
        return super().get_queryset().order_by("-created_at")

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(customer=self.request.user)
    #     return queryset


class OrderUpdateView(
    LoginRequiredMixin, UpdateView
):  # pylint: disable=too-many-ancestors

    model = Order
    form_class = OrderForm
    success_url = reverse_lazy("moderator_list_orders")
    template_name = "moderator/order_create_or_update.html"
    context_object_name = "order"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = self.get_object()
        cart = order.cart
        context["cart"] = cart
        cart_items = cart.items.all()
        for item in cart_items:
            item.cart_item_update_form = UpdateCartItemForm(instance=item)
            # item.cart_item_update_form.fields['quantity'].widget.attrs[
            #     'max'] = f"{item.product_variant.quantity}"
        context["cart_items"] = cart_items
        context["delivery_address_form"] = DeliveryInformationForm(
            instance=order.delivery_info)
        context["billing_address_form"] = BillingInformationForm(
            instance=order.billing_info)
        return context


class OrderDeleteView(
    LoginRequiredMixin, DeleteView
):  # pylint: disable=too-many-ancestors
    """Smazání konkrétního uživatele

    Args:
        LoginRequiredMixin (_type_): _description_
        DeleteView (_type_): _description_
    """

    model = Order
    success_url = reverse_lazy("moderator_list_orders")


class OrderCartItemUpdateview(LoginRequiredMixin, UpdateView
                              ):
    model = CartItem
    form_class = UpdateCartItemForm
    success_url = reverse_lazy("moderator_list_orders")

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
        cart_item = self.get_object()
        cart_item.cart = None
        messages.success(self.request, f"The quantity was updated.")

        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "Please provide product variant and quantity")
        return super().form_invalid(form)
