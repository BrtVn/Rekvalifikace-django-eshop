from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class Tag(models.Model):
    tag_title = models.CharField(max_length=30, verbose_name="Příznaky")
    slug = models.SlugField(max_length=200, unique=True, null=False)
    bg_color = models.CharField(max_length=7)
    font_color = models.CharField(max_length=7)
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return f"{self.tag_title}"

    class Meta:
        verbose_name = "Příznak"
        verbose_name_plural = "Příznaky"

    def get_absolute_url(self):
        return reverse("tag_detail", kwargs={"slug": self.slug})
