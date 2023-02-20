from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import datetime


class UserManager(BaseUserManager):
    # Vytvoří uživatele
    def create_user(self, email, password):
        print(self.model)
        if (email and password):
            user = self.model(email=self.normalize_email(email))
            user.set_password(password)
            user.save()
        return user
     # Vytvoří admina

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_admin = True
        user.save()
        return user


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=12, blank=True)
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Uživatel'
        verbose_name_plural = 'Uživatelé'

    objects = UserManager()

    USERNAME_FIELD = "email"

    def __str__(self) -> str:
        return f"Jméno: {self. first_name} {self.last_name} ({self.email}) | Role: {'admin' if self.is_admin else 'customer'}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Customer(models.Model):
    # do budoucna adresy v samoostatné DB
    # https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#extending-the-existing-user-model
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    address_line1 = models.CharField(max_length=500, blank=True)
    address_line2 = models.CharField(max_length=500, blank=True)
    city = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = 'Zákazník'
        verbose_name_plural = 'Zákazníci'
