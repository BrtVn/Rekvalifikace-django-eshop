from django import template
from eshop.models.products import ProductCategory, Product

register = template.Library()


@register.simple_tag()
def get_product_categories():
    """ Return all items in cart or None
    Usage:
    {% load tags %}
    {% get_post_categories as categories %}
    {% if cart %} 
    <ul >          
        {% for item in categories %}
            <li > {{item}} < /li >
        {% endfor %}
    </ul >

    Args:


    Returns:
        _type_: _description_
    """

    categories = ProductCategory.objects.all()
    if categories:
        return categories
    return None


@register.inclusion_tag("eshop/display_products.html")
def show_products(category=None, tag=None):
    if not category and not tag:
        products = Product.objects.all()
    elif category:
        products = Product.objects.filter(
            product_category__category_name=category)
    elif tag:
        products = Product.objects.filter(
            product_tags__tag_title=tag)
    elif category and tag:
        products = Product.objects.filter(
            product_category__category_name=category,
            product_tags__tag_title=tag)

    return {"products": products}
