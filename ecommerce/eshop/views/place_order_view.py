from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from eshop.models.users import Customer
from eshop.models.orders import Order
from eshop.forms.order_form import OrderForm

class PlaceOrderView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'eshop/base_form.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = Customer.objects.get(id=self.kwargs['i'])
        context['customer'] = customer
        return context

    def form_valid(self, form):
        customer = Customer.objects.get(id=self.kwargs['i'])
        form.instance.customer = customer
        return super().form_valid(form)