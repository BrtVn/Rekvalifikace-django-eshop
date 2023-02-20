from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

import datetime


class Message(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField()
    posted_at = models.DateTimeField(default=datetime.datetime.now)
    """ score = models.FloatField(
        default=0.0,
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)]
    )"""

    class Meta:
        verbose_name = 'Kontaktní formulář'
        verbose_name_plural = 'Kontaktní formuláře'

    def __str__(self) -> str:
        return f"{self.name}'s message @ {self.posted_at}"
