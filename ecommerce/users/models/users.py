from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from phonenumber_field.modelfields import PhoneNumberField


class CustomUserManager(BaseUserManager):
    # Vytvoří uživatele
    def create_user(self, email, password, **extra_fields):
        print(self.model)

        if email and password:
            email = self.normalize_email(email)
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save()
        else:
            raise ValueError(
                "Users must have an email address and a password.")
        return user

    # Vytvoří admina
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_customer", False)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)

    # Vytvoří zákazníka
    def create_customer(self, email, password, **extra_fields):
        extra_fields.setdefault("is_admin", False)
        extra_fields.setdefault("is_customer", True)
        extra_fields.setdefault("is_active", False)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        if extra_fields.get("is_customer") is not True:
            raise ValueError(_("Customer must have is_customer=True."))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": _("A user with that email address already exists."),
        },
    )
    phone = models.CharField(_("phone number"), max_length=15)
    profile_image = models.ImageField(
        blank=True, upload_to="users/uploads/users")
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    preferred_billing_information = models.OneToOneField(
        "BillingInformation",
        verbose_name=_("Preferred billing information"),
        on_delete=models.SET_NULL,
        # limit_choices_to={'pk': models.OuterRef('user_id')},
        related_name="preferred_billing_informationby_user",
        blank=True,
        null=True,)
    preferred_delivery_information = models.OneToOneField(
        "DeliveryInformation",
        verbose_name=_("Preferred delivery information"),
        on_delete=models.SET_NULL,
        # limit_choices_to=DeliveryInformation.objects.filter(user=self),
        related_name="preferred_delivery_information_by_user",
        blank=True,
        null=True,
    )

    # created_on = models.DateTimeField(_("date joined"), auto_now_add=True)
    updated_on = models.DateTimeField(_("date created"), auto_now=True)

    is_admin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)

    # vzato z class Abstractuser:
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    class Meta:
        verbose_name = "Uživatel"
        verbose_name_plural = "Uživatelé"

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        if self.is_admin:
            role = "admin"
        elif self.is_customer:
            role = "customer"
        else:
            role = "user"
        return f"Jméno: {self.get_full_name} ({self.email}) | Role: {role}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @ property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    # @property
    # def is_staff(self):
    #     return self.is_admin


class AbstractAddress(models.Model):
    alias = models.CharField(
        max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    address_line1 = models.CharField(max_length=500, blank=True, null=True)
    address_line2 = models.CharField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        abstract = True


class DeliveryInformation(AbstractAddress):
    user = models.ForeignKey(
        "CustomUser",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="delivery_informations",
    )
    delivery_phone = models.CharField(_("phone number"), max_length=15)

    class Meta:
        verbose_name = "Dodací údaj"
        verbose_name_plural = "Dodací údaje"

    def __str__(self) -> str:
        return f"Dodací údaje {self.alias} účtu: {self.user.email if self.user else 'AnonymousUser'}"


class BillingInformation(AbstractAddress):
    user = models.ForeignKey(
        "CustomUser",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="billing_informations",
    )
    vat_id = models.CharField(max_length=255, blank=True, null=True)
    tax_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Fakturační údaj"
        verbose_name_plural = "Fakturační údaje"

    def __str__(self) -> str:
        return f"Fakturační údaje {self.alias} účtu: {self.user.email if self.user else 'AnonymousUser'}"
