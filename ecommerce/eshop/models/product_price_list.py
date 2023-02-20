from django.db import models
import datetime


class ProductPriceList(models.Model):
    currency = models.CharField(max_length=3, default="CZK")
    price_list_name = models.CharField(max_length=50)
    price_list_description = models.TextField()
    price = models.IntegerField(default=0)
    product = models.ForeignKey(
        "Product", on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    # modified = models.DateTimeField()

    class Meta:
        verbose_name = "Ceník produktu"
        verbose_name_plural = "Ceníky produktů"

    def __str__(self) -> str:
        return self.price_list_name
