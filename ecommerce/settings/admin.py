from django.contrib import admin
from settings.models.settings import GeneralInfo, Contact
# Register your models here.


class OnlyChangePermissionMixin:
    # This will help you to disbale add functionality
    def has_add_permission(self, request):
        if not self.model.objects.exists():
            return True
        else:
            return False

    # This will help you to disable delete functionaliyt
    def has_delete_permission(self, request, obj=None):
        return False

    # This will help you to disable change functionality
    def has_change_permission(self, request, obj=None):
        return True


@admin.register(GeneralInfo)
class GeneralInfoAdmin(OnlyChangePermissionMixin, admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(OnlyChangePermissionMixin, admin.ModelAdmin):
    pass
