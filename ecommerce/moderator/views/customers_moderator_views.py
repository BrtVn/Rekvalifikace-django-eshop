from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models.users import CustomUser
from eshop.models.orders import Order
from moderator.forms.customers_forms import CustomerChangeForm, CustomerCreationForm


class CustomersListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = "moderator/customers_list.html"
    context_object_name = "users"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = self.model.objects.filter(is_customer=True)
        return queryset


class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = CustomUser
    form_class = CustomerCreationForm
    success_url = reverse_lazy("list_customers")
    template_name = "moderator/customer_create_or_update.html"


class CustomerUpdateView(
    LoginRequiredMixin, UpdateView
):  # pylint: disable=too-many-ancestors

    model = CustomUser
    form_class = CustomerChangeForm
    success_url = reverse_lazy("list_customers")
    template_name = "moderator/customer_create_or_update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = self.get_object()
        orders = Order.objects.filter(customer=customer.id)
        context["orders"] = orders
        return context


class CustomerDeleteView(
    LoginRequiredMixin, DeleteView
):  # pylint: disable=too-many-ancestors
    """Smazání konkrétního uživatele

    Args:
        LoginRequiredMixin (_type_): _description_
        DeleteView (_type_): _description_
    """

    model = CustomUser
    success_url = reverse_lazy("list_customers")
