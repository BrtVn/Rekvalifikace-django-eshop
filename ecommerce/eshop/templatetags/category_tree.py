from django import template
from eshop.models.product_category import ProductCategory

register = template.Library()


@register.inclusion_tag("eshop/category_tree_index.html")
def show_categories():
    categories = ProductCategory.objects.all()
    return {"categories": categories}
