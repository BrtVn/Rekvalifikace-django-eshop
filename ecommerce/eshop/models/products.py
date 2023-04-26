from django.db import models

from django.urls import reverse
from ckeditor.fields import RichTextField

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True, null=False)
    product_sku = models.CharField(max_length=50, unique=True)
    product_description = RichTextField()
    product_category = models.ForeignKey(
        "ProductCategory", on_delete=models.CASCADE, default=1
    )
    product_tags = models.ManyToManyField("Tag", blank=True)
    product_evaluation = models.FloatField(default=0)
    product_short_description = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.product_name}"

    class Meta:
        verbose_name = "Produkt"
        verbose_name_plural = "Produkty"

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})  # new

    @property
    def get_product_price_range(self):
        variants = self.product_variants.all()
        variants_prices = []
        for variant in variants:
            if variant:
                variants_prices.append(variant.price)
        if variants_prices:
            min_price = min(variants_prices)
            max_price = max(variants_prices)
            if min_price < max_price:
                price = f"{min_price} - {max_price}"
            elif min_price == max_price:
                price = f"{min_price}"

        return price

    @property
    def is_available(self):
        variants = self.product_variants.all()
        variants_list = []
        for variant in variants:
            if variant.quantity:
                variants_list.append(variant.quantity)
        if variants_list:
            return True
        return False


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True, related_name='images')
    image = models.ImageField(blank=True, upload_to="eshop/uploads/products")

    thumbnail = ImageSpecField(source='image',
                               processors=[ResizeToFit(450, 300)],
                               format='JPEG',
                               options={'quality': 100})
    cart_thumbnail = ImageSpecField(source='image',
                                    processors=[ResizeToFit(120,)],
                                    format='JPEG',
                                    options={'quality': 100})

    detail = ImageSpecField(source='image',
                            processors=[ResizeToFit(600, 700)],
                            format='JPEG',
                            options={'quality': 100})

    class Meta:
        verbose_name = "Produktový obrázek"
        verbose_name_plural = "Produktové obrázky"

    def __str__(self):
        return f"{self.product.product_name} images"


class ProductVariant(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_variants')
    variant = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    original_price = models.DecimalField(
        max_digits=12, decimal_places=2, default=0)

    class Meta:
        verbose_name = "Varianta produktu"
        verbose_name_plural = "Varianty produktu"

    def __str__(self):
        return f"{self.variant} | ${self.price} | {'Available' if self.quantity else 'Sold out'}"


class ProductCategory(models.Model):
    slug = models.SlugField(max_length=200, unique=True, null=False)
    category_name = models.CharField(max_length=50)
    # category_parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name="children" )
    category_description = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Kategorie produktu"
        verbose_name_plural = "Kategorie produktů"

    def __str__(self) -> str:
        return f"{self.category_name}"

    @staticmethod
    def return_all_categories():
        return ProductCategory.objects.all()

    @staticmethod
    def return_category_description(description):
        return ProductCategory.objects.filter(category_description=description)

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})
