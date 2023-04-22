from django.db import models
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField
from users.models.users import AbstractAddress


class MaxNumInstancesMixin:
    MAX_NUM_INSTANCES = None

    def full_clean(self, exclude=None, validate_unique=True):
        super().full_clean(exclude, validate_unique)

        if (
            self.pk is None
            and self.__class__.objects.exists()
            and self.__class__.objects.count() >= self.MAX_NUM_INSTANCES
        ):

            raise ValidationError(
                f"Maximum number of instances ({self.MAX_NUM_INSTANCES}) reached",
                code="max_num",
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class GeneralInfo(MaxNumInstancesMixin, models.Model):
    """Model definition for GeneralInfo."""

    MAX_NUM_INSTANCES = 1

    company_name = models.CharField(max_length=50, default="Název společnosti")
    company_info = RichTextField(
        max_length=500, default="Nějaké info o společnosti")
    about_us = RichTextField(default="O nás")
    footer_copyright = RichTextField(
        max_length=250, default="&copy;")
    facebook_url = models.URLField(max_length=200, blank=True)
    twitter_url = models.URLField(max_length=200, blank=True)
    google_url = models.URLField(max_length=200, blank=True)
    instagram_url = models.URLField(max_length=200, blank=True)
    linkedin_url = models.URLField(max_length=200, blank=True)
    github_url = models.URLField(max_length=200, blank=True)

    class Meta:
        """Meta definition for GeneralInfo."""

        verbose_name = "GeneralInfo"
        verbose_name_plural = "GeneralInfos"

    def __str__(self):
        """Unicode representation of GeneralInfo."""
        return f"{self.company_name}"

    @property
    def has_social_accounts(self):
        if (
            (self.facebook_url is not None)
            or (self.twitter_url is not None)
            or (self.google_url is not None)
            or (self.instagram_url is not None)
            or (self.linkedin_url is not None)
            or (self.github_url is not None)
        ):
            return True
        else:
            return False


class Contact(AbstractAddress, MaxNumInstancesMixin, models.Model):
    """Model definition for Contact."""

    email = models.EmailField(max_length=254, default="email@example.com")
    phone = models.CharField(max_length=20, blank=True,
                             default="+420 123 456 789")
    mobile_phone = models.CharField(
        max_length=20, blank=True, default="+420 123 456 789"
    )

    class Meta:
        """Meta definition for Contact."""

        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        """Unicode representation of Contact."""
        return f"{self.name}"

    @property
    def get_sigle_line_address(self):
        return f"{self.address_line1}, {self.city}, {self.postal_code}, {self.country}"
