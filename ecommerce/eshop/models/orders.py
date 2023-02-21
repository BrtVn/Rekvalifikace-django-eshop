from django.db import models
import datetime

STATUS = (
    (0,"Draft"),
    (1,"Placed"),
    (1,"Pending"),
    (2,"Payed")
)

class Order(models.Model):
    product = models.ManyToManyField("Product")
    customer = models.ForeignKey("CustomUser", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    address = models.CharField (max_length=50, default='', blank=True)
    phone = models.CharField (max_length=50, default='', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        verbose_name = 'Objednávka'
        verbose_name_plural = 'Objednávky'
    
    def place_order(self):
        self.save()
    
    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')
    
    def __str__(self) -> str:
        return f"{self.customer}: {self.id}"
    
