from django.db import models
import datetime


class ProductCategory(models.Model):
    category_name = models.CharField(max_length=50)
    # category_parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name="children" )
    category_description = models.TextField()
    created_at = models.DateTimeField(default=datetime.datetime.now)
    # modified = models.DateTimeField()

    class Meta:
        verbose_name = "Kategorie produktu"
        verbose_name_plural = "Kategorie produktů"

    @staticmethod
    def return_all_categories():
        return ProductCategory.objects.all()

    @staticmethod
    def return_category_description(description):
        return ProductCategory.objects.filter(category_description=description)

    def __str__(self) -> str:
        return self.category_name
