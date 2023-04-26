from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from eshop.models.orders import CartDiscount
from moderator.forms.discount_code_forms import CartDiscountForm


class CartDiscountListView(LoginRequiredMixin, ListView):
    model = CartDiscount
    template_name = "moderator/discount_codes_list.html"
    context_object_name = "codes"


class CartDiscountCreateView(LoginRequiredMixin, CreateView):
    model = CartDiscount
    form_class = CartDiscountForm
    success_url = reverse_lazy("list_discount_codes")
    template_name = "moderator/discount_code_create_or_update.html"


class CartDiscountUpdateView(
    LoginRequiredMixin, UpdateView
):  # pylint: disable=too-many-ancestors

    model = CartDiscount
    form_class = CartDiscountForm
    success_url = reverse_lazy("list_discount_codes")
    template_name = "moderator/discount_code_create_or_update.html"


class CartDiscountDeleteView(
    LoginRequiredMixin, DeleteView
):  # pylint: disable=too-many-ancestors
    """Smazání konkrétní kategoorie

    Args:
        LoginRequiredMixin (_type_): _description_
        DeleteView (_type_): _description_
    """

    model = CartDiscount
    success_url = reverse_lazy("list_discount_codes")
