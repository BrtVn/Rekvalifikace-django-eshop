from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms.users_forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import CustomUser, DeliveryInformation
from django.utils.translation import gettext_lazy as _


class DeliveryInformationInline(admin.TabularInline):
    model = DeliveryInformation
    #can_delete = False
    verbose_name = 'Adresa'
    verbose_name_plural = 'Adresy'
    #show_change_link = True
    extra = 1


class CustomUserAdmin(UserAdmin):
    inlines = (DeliveryInformationInline,)
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "phone",  "first_name", "last_name", "is_admin", "is_customer",
                    "is_staff", "is_active", )
    list_filter = ("email", "phone",  "first_name", "last_name", "is_admin", "is_customer",
                   "is_staff", "is_active", )
    fieldsets = (
        (None, {"fields": ("email", "password",
         "first_name", "last_name", "phone",)}),
        (_("Permissions"), {"fields": ("is_staff",
         "is_active", "is_admin", "is_customer", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
         ),
    )
    search_fields = ("email",)
    ordering = ("email",)

        



admin.site.register(CustomUser, CustomUserAdmin)
