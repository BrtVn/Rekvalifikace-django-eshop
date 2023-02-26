from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.mail import send_mail

from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    # Vytvoří uživatele
    def create_user(self, email, password, **extra_fields):
        print(self.model)

        if (email and password):
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

    email = models.EmailField(_("email address"),
                              unique=True,
                              error_messages={
        "unique": _("A user with that email address already exists."),
    },)
    phone = models.CharField(_("phone number"), max_length=12, blank=True)

    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)

    #created_on = models.DateTimeField(_("date joined"), auto_now_add=True)
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
            role = 'admin'
        elif self.is_customer:
            role = 'customer'
        else:
            role = 'user'
        return f"Jméno: {self.get_full_name} ({self.email}) | Role: {role}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


"""@property
    def is_staff(self):
        return self.is_admin"""


class DeliveryInformation(models.Model):
    # https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#extending-the-existing-user-model
    name = models.CharField(max_length=50, blank=True)
    user = models.ForeignKey("CustomUser", null=True, on_delete=models.CASCADE)
    #user = models.OneToOneField("CustomUser", null=True, on_delete=models.CASCADE)
    address_line1 = models.CharField(max_length=500, blank=True)
    address_line2 = models.CharField(max_length=500, blank=True)
    city = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=12, blank=True)

    class Meta:
        verbose_name = 'Adresa'
        verbose_name_plural = 'Adresy'

    objects = CustomUserManager()
    
    def __str__(self) -> str:
        return f"Adresy účtu: {self.user.email}"
