from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms.users_forms import CustomUserCreationForm, AdminCustomUserChangeForm
from users.models import CustomUser, DeliveryInformation, BillingInformation
from django.utils.translation import gettext_lazy as _


class DeliveryInformationInline(admin.TabularInline):
    model = DeliveryInformation
    # can_delete = False
    verbose_name = "Dodací údaj"
    verbose_name_plural = "Dodací údaje"
    # show_change_link = True
    extra = 1


class BillingInformationInline(admin.TabularInline):
    model = BillingInformation
    # can_delete = False
    verbose_name = "Fakturační údaj"
    verbose_name_plural = "Fakturační údaje"
    # show_change_link = True
    extra = 1


class CustomUserAdmin(UserAdmin):
    inlines = (DeliveryInformationInline, BillingInformationInline,)
    add_form = CustomUserCreationForm
    form = AdminCustomUserChangeForm
    model = CustomUser
    list_display = (
        "email",
        "phone",
        "first_name",
        "last_name",
        "is_admin",
        "is_customer",
        "is_staff",
        "is_active",
        "preferred_billing_information",
        "preferred_delivery_information",
    )
    list_filter = (
        "email",
        "phone",
        "first_name",
        "last_name",
        "is_admin",
        "is_customer",
        "is_staff",
        "is_active",
        "preferred_billing_information",
        "preferred_delivery_information",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                    "first_name",
                    "last_name",
                    "phone",
                    "profile_image",
                    "preferred_billing_information",
                    "preferred_delivery_information",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_admin",
                    "is_customer",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)
