from django.db import transaction
from django.views import generic
from users.models.users import CustomUser, DeliveryInformation
from users.forms import DeliveryInformationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from users.forms.users_forms import CustomUserChangeForm, CustomUserCreationForm
from allauth.account.views import PasswordSetView, PasswordChangeView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy


class UpdateUserProfileView(LoginRequiredMixin, generic.edit.UpdateView):
    model = CustomUser
    template_name = 'users/profile.html'
    context_object_name = 'user'
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('profile_detail')

    def get_object(self, queryset=None):
        return self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        delivery_info, created = DeliveryInformation.objects.get_or_create(user=self.request.user)
        context['delivery_form'] = DeliveryInformationForm(instance=delivery_info)
        return context
    

    @transaction.atomic
    def form_valid(self, form):
        delivery_info_form = DeliveryInformationForm(self.request.POST)
        if delivery_info_form.is_valid():
            delivery_info = delivery_info_form.save(commit=False)
            delivery_info.user = self.request.user
            delivery_info.save()
        return super().form_valid(form)

   
      
