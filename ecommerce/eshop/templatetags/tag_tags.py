from django import template
from eshop.models.tag import Tag

register = template.Library()


@register.simple_tag()
def get_tags():
    tags = Tag.objects.all()
    if tags:
        return tags
    return None
