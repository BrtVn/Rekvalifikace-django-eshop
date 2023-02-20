from django.db import models
import datetime


class ProductInventory(models.Model):
    inventory_name = models.CharField(max_length=50)
    inventory_description = models.TextField()
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    # modified = models.DateTimeField()

    class Meta:
        verbose_name = "Sklad produktu"
        verbose_name_plural = "Sklad produktů"

    def __str__(self) -> str:
        return self.inventory_name
