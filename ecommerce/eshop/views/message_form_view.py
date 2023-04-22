from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from eshop.forms.message_form import ContactForm
from eshop.models.messages import Message
from settings.models.settings import GeneralInfo


class ContactFormView(generic.edit.CreateView):
    form_class = ContactForm
    model = Message
    template_name = "eshop/base_form.html"

    def get(self, request):
        form = self.form_class(None)
        url_action = "/contact/"
        general_info = GeneralInfo.objects.first()
        context = {"form": form,
                   "general_info": general_info,
                   "url_action": url_action}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)

        if (form.is_valid()):
            messages.success(request, 'Message sent')
            form.save()
        else:
            messages.error(request, 'Message error')

        return render(request, self.template_name, {"form": form})
