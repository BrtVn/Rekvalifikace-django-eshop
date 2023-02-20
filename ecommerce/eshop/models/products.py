from django.db import models


class Product(models.Model):
    product_sku = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=False)
    product_name = models.CharField(max_length=50)
    product_description = models.TextField()
    product_image = models.ImageField(upload_to="eshop/uploads/products")
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
