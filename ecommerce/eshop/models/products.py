from django.db import models
from django.utils.safestring import mark_safe

class Product(models.Model):
    product_sku = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=False)
    product_name = models.CharField(max_length=50)
    product_description = models.TextField()
    #product_image = models.ImageField(upload_to="eshop/uploads/products")
    product_category = models.ForeignKey(
        "ProductCategory", on_delete=models.CASCADE, default=1)
    # product_inventory = models.ForeignKey("ProductInventory", on_delete=models.CASCADE, default=1)
    product_inventory = models.IntegerField(default=0)
    # product_price_list = models.ForeignKey("ProductPriceList", on_delete=models.CASCADE, default=1)
    product_price = models.FloatField(default=0)
    original_price = models.FloatField(default=0)
    product_tag = models.ManyToManyField("Tag", blank=True)
    product_evaluation = models.FloatField(default=0)

    
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __init__(self, *args, **kwargs):
        super(Product, self).__init__(*args, **kwargs)

    def __str__(self) -> str:
        return self.product_name

    class Meta:
        verbose_name = 'Produkt'
        verbose_name_plural = 'Produkty'

    @staticmethod
    def return_all_products():
        return Product.objects.all()
    
    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter (id__in=ids)

class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True
        )
    image = models.ImageField(blank=True, upload_to="eshop/uploads/products")
    
    class Meta:
        verbose_name = 'Produktový obrázek'
        verbose_name_plural = 'Produktové obrázky'

    def __str__(self):
        return self.product.product_name
    
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""
        
class ProductVariant(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE
        )
    size = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    
    class Meta:
        verbose_name = 'Varianta produktu'
        verbose_name_plural = 'Varianty produktu'

    def __str__(self):
        return self.product.product_name