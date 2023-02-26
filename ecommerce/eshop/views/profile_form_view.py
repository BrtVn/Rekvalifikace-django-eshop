"""from django.shortcuts import render, redirect, reverse
from django.views import generic
from eshop.forms.profile_form import ProfileForm
from django.contrib import messages
from eshop.models.users import CustomUser

class ProfileFormView(generic.edit.UpdateView):
    form_class = ProfileForm
    model = CustomUser
    template_name = "eshop/base_form.html"
    template_name_suffix = '_update_profile_form'
    
    
    def get(self, request):
        if not request.user.is_authenticated:
            messages.info(request, "You can't edit profile when you are not logged in")
            return redirect(reverse("index"))
        else:
            form = self.form_class(None)
            user = self.request.user
            form.fields['first_name'].widget.attrs['placeholder'] = user.first_name
            form.fields['last_name'].widget.attrs['placeholder'] = user.last_name
            form.fields['phone'].widget.attrs['placeholder'] = user.phone
            form.fields['email'].widget.attrs['placeholder'] = user.email
            #form.fields['address_line1'].widget.attrs['placeholder'] = user.customer.address_line1
            #form.fields['address_line2'].widget.attrs['placeholder'] = user.address_line2
            #form.fields['city'].widget.attrs['placeholder'] = user.city
            #form.fields['postal_code'].widget.attrs['placeholder'] = user.postal_code
            #form.fields['country'].widget.attrs['placeholder'] = user.country
            
            url_action = "/profile/"
            context = {"form": form,
                       "url_action": url_action}
        return render(request, self.template_name, context)

    def post(self, request):
        if request.user.is_authenticated:
            messages.info(request, "You can't edit profile when yoou are not logged in")
            return redirect(reverse("index"))  
        
        form = self.form_class(request.POST)
        if (form.is_valid()):
            uzivatel = form.save(commit=False)
            password = form.cleaned_data["password"]
            uzivatel.set_password(password)
            uzivatel.save()
            messages.success(request, 'Success')

            return redirect("index")

        messages.error(request, 'Error')
        return render(request, self.template_name, {"form": form})

"""