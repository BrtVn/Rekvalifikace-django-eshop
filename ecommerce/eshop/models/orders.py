from django.db import models
from django.utils.crypto import get_random_string
from django.core.validators import MinValueValidator
from ckeditor.fields import RichTextField


class DeliveryMethod(models.Model):
    name = models.CharField(max_length=50)
    description = RichTextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.name} ${self.price}"

    # min_cart_price = models.DecimalField(max_digits=8, decimal_places=2)
    # max_cart_price = models.DecimalField(max_digits=8, decimal_places=2)
    # delivery_price = models.DecimalField(max_digits=8, decimal_places=2)
    # estimated_delivery_time = models.PositiveIntegerField()
    # free_from_cart_price = models.DecimalField(
    #     max_digits=6, decimal_places=2, null=True, blank=True)

    # def calculate_delivery_price(self, cart_price):
    #     if cart_price < self.min_cart_price:
    #         return None  # Delivery not available for cart price below minimum
    #     elif cart_price > self.max_cart_price:
    #         return None  # Delivery not available for cart price above maximum
    #     else:
    #         return self.price


class PaymentMethod(models.Model):
    name = models.CharField(max_length=50)
    description = RichTextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.name} ${self.price}"


CART_STATUS = (
    ("DRAFT", "Draft"),
    ("SAVED", "Saved"),
    ("PLACED", "Placed")
)


class Cart(models.Model):
    delivery_method = models.ForeignKey(
        "DeliveryMethod", on_delete=models.PROTECT, related_name='carts', default=1, null=True, blank=True)
    payment_method = models.ForeignKey(
        "PaymentMethod", on_delete=models.PROTECT, related_name='carts', default=1, null=True, blank=True)
    status = models.CharField(
        choices=CART_STATUS, default="DRAFT", max_length=20)

    class Meta:
        verbose_name = 'Košík'
        verbose_name_plural = 'Košíky'

    def __str__(self):
        return f"{self._meta.verbose_name} ({self.get_total_cart_price} / {len(self.get_all_cart_items())})"

    @property
    def get_total_cart_price(self):
        items = self.items.all()
        item_prices = []
        price = 0
        for item in items:
            if item:
                item_prices.append(item.get_total_item_price)
        if item_prices:
            price += sum(item_prices)

        if self.delivery_method:
            price += self.delivery_method.price

        if self.payment_method:
            price += self.payment_method.price
        return price

    @property
    def get_subtotal_cart_price(self):
        items = self.items.all()
        item_prices = []
        price = 0
        for item in items:
            if item:
                item_prices.append(item.get_total_item_price)
        if item_prices:
            price += sum(item_prices)
        return price

    def get_all_cart_items(self):
        return self.items.all()


class CartItem(models.Model):
    cart = models.ForeignKey(
        "Cart", on_delete=models.CASCADE, related_name='items')
    product_variant = models.ForeignKey(
        "ProductVariant", on_delete=models.CASCADE, related_name='variants')
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.quantity} x {self.product_variant.product.product_name}"

    @property
    def get_total_item_price(self):
        if self.quantity:
            return self.quantity * self.price
        return 0


ORDER_STATUS = (
    ("DRAFT", "Draft"),
    ("PLACED", "Placed"),
    ("PENDING", "Pending"),
    ("PAID", "Paid")
)


class Order(models.Model):
    customer = models.ForeignKey(
        "users.CustomUser", on_delete=models.PROTECT, related_name='users', blank=True, null=True)
    delivery_info = models.OneToOneField(
        "users.DeliveryInformation", on_delete=models.PROTECT, null=True, blank=True)
    billing_info = models.OneToOneField(
        "users.BillingInformation", on_delete=models.PROTECT, null=True, blank=True)
    cart = models.OneToOneField("Cart", on_delete=models.CASCADE, default=None)
    note = models.TextField(null=True, blank=True)
    total_price = models.DecimalField(
        max_digits=12, decimal_places=2, default=0)
    status = models.CharField(choices=ORDER_STATUS,
                              default="DRAFT", max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Objednávka'
        verbose_name_plural = 'Objednávky'

    def place_order(self):
        self.save()

    @ staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')

    def __str__(self) -> str:
        return f"Order: {self.id}"


class CartDiscount(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True, default="")
    # discount_type = models.CharField(
    #     max_length=20,
    #     choices=[('percentage', 'Percentage'), ('amount', 'Amount')],
    #     default='percentage'
    # )
    # amount = models.DecimalField(
    #     max_digits=8,
    #     decimal_places=2,
    #     null=True,
    #     blank=True,
    #     default=0,
    #     validators=[MinValueValidator(0)]
    # )
    # percentage = models.DecimalField(
    #     max_digits=5,
    #     decimal_places=2,
    #     null=True,
    #     blank=True,
    #     default=0,
    #     validators=[MinValueValidator(0)]
    # )
    # start_date = models.DateField()
    # end_date = models.DateField()

    # def __str__(self):
    #     return f"{self.name}"

    # def apply_discount(self, price):
    #     if self.discount_type == 'percentage':
    #         discount = price * self.percentage / 100
    #         if discount > self.amount:
    #             return price - discount
    #         else:
    #             return price - self.amount
    #     else:
    #         return price - self.amount

    # def generate_discount_code(self):
    #     return get_random_string(8)
