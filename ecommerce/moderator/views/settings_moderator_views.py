from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from settings.models.settings import GeneralInfo, Contact
from moderator.forms.settings_forms import GeneralInfoForm, ContactForm


class GeneralInfoListView(LoginRequiredMixin, ListView):
    model = GeneralInfo
    template_name = "moderator/company_info_list.html"
    context_object_name = "infos"

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = self.model.objects.filter(is_customer=True)
    #     return queryset


class GeneralInfoCreateView(LoginRequiredMixin, CreateView):
    model = GeneralInfo
    form_class = GeneralInfoForm
    success_url = reverse_lazy("list_company_info")
    template_name = "moderator/company_info_create_or_update.html"


class GeneralInfoUpdateView(
    LoginRequiredMixin, UpdateView
):  # pylint: disable=too-many-ancestors

    model = GeneralInfo
    form_class = GeneralInfoForm
    success_url = reverse_lazy("list_company_info")
    template_name = "moderator/company_info_create_or_update.html"


class GeneralInfoDeleteView(
    LoginRequiredMixin, DeleteView
):  # pylint: disable=too-many-ancestors
    """Smazání konkrétního uživatele

    Args:
        LoginRequiredMixin (_type_): _description_
        DeleteView (_type_): _description_
    """

    model = GeneralInfo
    success_url = reverse_lazy("list_company_info")


class ContactListView(LoginRequiredMixin, ListView):
    model = Contact
    template_name = "moderator/moderator_contact_list.html"
    context_object_name = "contacts"

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = self.model.objects.filter(is_customer=True)
    #     return queryset


class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy("list_contact")
    template_name = "moderator/contact_create_or_update.html"


class ContactUpdateView(
    LoginRequiredMixin, UpdateView
):  # pylint: disable=too-many-ancestors

    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy("list_contact")
    template_name = "moderator/contact_create_or_update.html"


class ContactDeleteView(
    LoginRequiredMixin, DeleteView
):  # pylint: disable=too-many-ancestors
    """Smazání konkrétního uživatele

    Args:
        LoginRequiredMixin (_type_): _description_
        DeleteView (_type_): _description_
    """

    model = Contact
    success_url = reverse_lazy("list_contact")
