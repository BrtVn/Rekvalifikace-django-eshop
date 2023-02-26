"""from django.shortcuts import render, redirect, reverse
from django.views import generic
from eshop.forms.user_form import CreateUserForm, LoginUserForm
from eshop.models.users import CustomUser
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin


class UserViewRegister(generic.edit.CreateView):
    form_class = CreateUserForm
    model = CustomUser
    template_name = "eshop/base_form.html"

    def get(self, request):
        if request.user.is_authenticated:
            messages.info(request, "Already logged in, you can't register")
            return redirect(reverse("index"))
        else:
            form = self.form_class(None)
            url_action = "/register/"
            context = {"form": form,
                       "url_action": url_action}
        return render(request, self.template_name, context)

    def post(self, request):
        if request.user.is_authenticated:
            messages.info(request, "Already logged in, you can't register")
            return redirect(reverse("index"))

        form = self.form_class(request.POST)
        if (form.is_valid()):
            uzivatel = form.save(commit=False)
            password = form.cleaned_data["password"]
            uzivatel.set_password(password)
            uzivatel.save()
            messages.success(request, 'Success')
            login(request, uzivatel)
            return redirect("index")

        messages.error(request, 'Error')
        return render(request, self.template_name, {"form": form})


class UserViewLogin(generic.edit.CreateView):
    form_class = LoginUserForm
    model = CustomUser
    template_name = "eshop/base_form.html"
    # success_message = "Successfully logged in"

    def get(self, request):
        if request.user.is_authenticated:
            messages.info(request, "Already logged in, you can't log in")
            return redirect(reverse("index"))
        else:
            form = self.form_class(None)
            url_action = "/login/"
            context = {"form": form,
                       "url_action": url_action}
        return render(request, self.template_name, context)
    
    def post(self, request):
        if request.user.is_authenticated:
            messages.info(request, "Already logged in, you can't log in")
            return redirect(reverse("index"))
        
        form = self.form_class(request.POST)
        if (form.is_valid()):
            email = form.cleaned_data["email"]
            print(email)
            password = form.cleaned_data["password"]
            print(password)
            user = authenticate(email=email, password=password)
            print(user)
            if user:
                messages.success(request, "Successfully logged in")
                login(request, user)
                return redirect(reverse("index"))

        messages.error(request, 'Error, check your credentials')
        return render(request, self.template_name, {"form": form})


def logout_user(request):
    if request.user.is_authenticated:
        messages.info(request, 'Successfully logged out')
        logout(request)
    else:
        messages.info(request, "You cannot log out if you are not logged in")
    return redirect(reverse("index"))
"""