from django.shortcuts import render
from django.views import generic
from eshop.forms.review_form import ReviewForm
from eshop.models.messages import Message
from django.contrib import messages


class ReviewFormView(generic.edit.CreateView):
    form_class = ReviewForm
    model = Message
    template_name = "eshop/base_form.html"

    def get(self, request):
        form = self.form_class(None)
        url_action = "/review/"
        context = {"form": form,
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
