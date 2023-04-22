from django.db import transaction
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from users.models.users import CustomUser
from users.forms.users_forms import CustomUserChangeForm
from users.forms import DeliveryInformationFormSet, BillingInformationFormSet


class UpdateUserProfileView(LoginRequiredMixin, generic.edit.UpdateView):
    model = CustomUser
    template_name = "users/profile.html"
    context_object_name = "user"
    form_class = CustomUserChangeForm
    success_url = reverse_lazy("profile_detail")

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.POST:
            context["delivery_formset"] = DeliveryInformationFormSet(
                self.request.POST, self.request.FILES, instance=self.object
            )
            context["billing_formset"] = BillingInformationFormSet(
                self.request.POST, self.request.FILES, instance=self.object
            )
        else:
            context["delivery_formset"] = DeliveryInformationFormSet(
                instance=self.object
            )
            context["billing_formset"] = BillingInformationFormSet(
                instance=self.object
            )
        return context

    @transaction.atomic
    def form_valid(self, form):
        context = self.get_context_data()
        delivery_info = context["delivery_formset"]
        billing_info = context["billing_formset"]
        with transaction.atomic():
            if form.is_valid() and delivery_info.is_valid() and billing_info.is_valid():
                self.object = form.save()
                delivery_info.instance = self.object
                delivery_info.save()
                billing_info.instance = self.object
                billing_info.save()
                return super().form_valid(form)
            else:
                print(form.errors)
                print(delivery_info.errors)
                print(billing_info.errors)
                return self.form_invalid(form)
