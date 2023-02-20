from django.db import models
import datetime


class Tag(models.Model):
    tag_title = models.CharField(max_length=30, verbose_name="Příznaky")
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.tag_title

    class Meta:
        verbose_name = "Příznak"
        verbose_name_plural = "Příznaky"
