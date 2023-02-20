from django import template
from eshop.models.products import Product

register = template.Library()


@register.inclusion_tag("eshop/display_products.html")
def show_products(category = None):
    print(category)
    if (category == None):
        products = Product.objects.all()
    else:
        products = Product.objects.filter(product_category__category_name=category)
    
    return {"products": products}
